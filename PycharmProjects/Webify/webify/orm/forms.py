from __future__ import annotations

from collections import ChainMap
from dataclasses import Field, dataclass, fields
from functools import partial
from itertools import chain, starmap
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    Iterable,
    Mapping,
    MutableSet,
    MutableSequence,
    Sequence,
    Tuple,
)
from urllib.parse import parse_qs

from typing_extensions import Protocol

from my_utils.html import Element
from my_utils.mappings import ChainMapOfIterables
from my_utils.type_stubs import wsgi


class FieldFactory(Protocol):
    def __call__(self, *, name) -> Element:
        ...


FACTORIES: MutableSequence[Tuple[MutableSet[str], FieldFactory]] = [
    ({"textarea", "multiline", "long", "para"}, partial(Element, "textarea", "")),
    ({"str", "text"}, partial(Element, "input")),
    ({"int", "nat", "whole"}, partial(Element, "input", type="number", step="1")),
    ({"float", "real", "num"}, partial(Element, "input", type="number")),
    ({"bool", "check", "toggle", "switch"}, partial(Element, "input", type="checkbox")),
]


def get_field_factory(field: Field):
    try:
        return field.metadata["form_element_factory"]  # type: ignore
    except (AttributeError, KeyError):
        pass

    annotation: Any = field.type

    try:
        annotation = annotation.__name__
    except AttributeError:
        pass

    annotation = annotation.lower()

    for substrings, field_factory in FACTORIES:
        for substring in substrings:
            if substring in annotation:
                return field_factory

    return partial(Element, "input", type=annotation)


@dataclass(init=False)
class FormResult(Element):
    _field_factories_: Mapping[str, FieldFactory] = MappingProxyType({})
    _fields_: Sequence[Element] = ()

    def __init__(
        self,
        _fields_: Iterable[Any] = (),
        attributes: Mapping[str, str] = MappingProxyType({}),
        **more_attributes
    ):
        combined_fields = tuple(
            chain(
                starmap(lambda name, f: f(name=name), self._field_factories_.items()),
                _fields_,
            )
        )
        combined_attributes = ChainMap(self.attributes, attributes, more_attributes)
        super().__init__("form", combined_fields, combined_attributes)
        object.__setattr__(self, "_fields_", combined_fields)

    def __init_subclass__(cls, **attributes):
        cls = dataclass(cls, init=False)

        def __init__(self, **kwargs):
            pass

        try:
            field_factories = dict(cls._field_factories_)
        except AttributeError:
            field_factories = {}

        for field in fields(cls):
            field_factories[field.name] = get_field_factory(field)

        cls._field_factories_ = MappingProxyType(field_factories)

        try:
            attributes_dict = dict(cls.attributes)
            attributes_dict.update(attributes)
            cls.attributes = MappingProxyType(attributes_dict)
        except AttributeError:
            cls.attributes = MappingProxyType(attributes)

    def _prefill_from_environ(
        self,
        environ: wsgi.Environ,
        should_fill: Callable[[Element], bool] = lambda el: el.tag != "input"
        or el.attributes.get("type") != "password",
    ) -> Iterable[Element]:
        values_dict = {
            key: iter(values)
            for key, values in ChainMapOfIterables(
                parse_qs(environ.get("QUERY_STRING", "")),
                parse_qs(environ["wsgi.input"].read()),
            ).items()
        }

        for field in self._fields_:
            if should_fill(field):
                values = values_dict.get(field.attributes.get("name"))

                if values is None:
                    continue

                try:
                    value = next(values)
                except StopIteration:
                    yield field
                else:
                    yield field.with_attrs({"value": str(value)})
            else:
                yield field

    def prefill_from_environ(
        self,
        environ: wsgi.Environ,
        should_fill: Callable[[Element], bool] = lambda el: el.tag != "input"
        or el.attributes.get("type") != "password",
    ) -> "FormObject":
        return FormObject(
            self._prefill_from_environ(environ, should_fill), self.attributes
        )
