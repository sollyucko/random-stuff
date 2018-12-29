from __future__ import annotations

from collections import ChainMap
from dataclasses import dataclass
from datetime import date, datetime, time
from itertools import starmap
from types import MappingProxyType
from typing import Mapping, Iterable, Any
from typing_extensions import Protocol

from my_utils import ChainMapOfIterables
from my_utils.html import Element


class FieldFactory(Protocol):
    def __call__(self, *, name) -> Element:
        pass


FACTORIES: Mapping[Type, FieldFactory] = {
    'str': partial(Element, 'textarea'),
    'int': partial(Element, 'input', type='number', step='1'),
    'float': partial(Element, 'input', type='number'),
}


@dataclass(frozen=True)
class Form(Element):
    _field_factories_: Mapping[str, FieldFactory] = MappingProxyType({})
    _fields_: Sequence[Element] = ()

    def __init__(self, _fields_: Iterable[Any] = (), attributes: Mapping[str, str] = MappingProxyType({}),
                 **more_attributes):
        combined_fields = tuple(chain(starmap(lambda name, f: f(name=name), self._field_factories_.items()), _fields_))
        combined_attributes = ChainMap(self.attributes, attributes, more_attributes)
        super().__init__('form', combined_fields, combined_attributes)
        object.__setattr__(self, '_fields_', combined_fields)

    def __init_subclass__(cls, **attributes):
        try:
            cls._field_factories_ = dict(cls._field_factories_)
        except AttributeError:
            cls._field_factories_ = {}

        for name, annotation in cls.__annotations__.items():
            annotation_str = str(annotation).lower()

            try:
                factory = FACTORIES[annotation_str]
            except KeyError:
                factory = partial(Element, 'input', annotation_str)

            cls._field_factories_[name] = factory

        for name, value in vars(cls).items():
            if not name.startswith('_'):
                cls._field_factories_[name] = value

        cls._field_factories_ = MappingProxyType(cls._field_factories_)

        try:
            cls.attributes = dict(cls.attributes)
            cls.attributes.update(attributes)
            cls.attributes = MappingProxyType(cls.attributes)
        except AttributeError:
            cls.attributes = MappingProxyType(attributes)

    def _prefill_from_environ(self, environ: wsgi.Environ,
                              should_fill: Callable[Element, bool] = lambda el: el.tag != 'input' or el.attributes.get(
                                  'type') != 'password') -> Iterable[Element]:
        values_dict = {key: iter(values)
                       for key, values
                       in ChainMapOfIterables(parse_qs(environ.get('QUERY_STRING', '')),
                                              parse_qs(environ['wsgi.input'].read()))
                          .items()}

        for field in self._fields_:
            values = values_dict.get(field.attributes.get('name'))

            if values:
                yield field.with_attrs({'name': str(next(values))})
            else:
                yield field

    def prefill_from_environ(self, environ: wsgi.Environ,
                             should_fill: Callable[Element, bool] = lambda el: el.tag != 'input' or el.attributes.get(
                                 'type') != 'password') -> Form:
        return Form(self._prefill_from_environ(environ, should_fill), self.attributes)
