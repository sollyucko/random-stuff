from __future__ import annotations

from abc import ABC
from collections import ChainMap
from dataclasses import dataclass
from html import escape
from types import MappingProxyType
from typing import Mapping, Sequence


class HTMLifiable(ABC):
    def __html__(self):
        ...


def htmlify(x: HTMLifiable):
    return type(x).__html__(x)


def _render_attr(name, value):
    return f' {escape(name)}="{escape(value)}"'


def _render_child(child: object):
    # noinspection PyBroadException
    try:
        # noinspection PyTypeChecker
        return htmlify(child)
    except Exception:
        return escape(str(child))


@dataclass(frozen=True)
class Element:
    attributes: Mapping[str, str]
    children: Sequence[object]
    tag: str

    def __init__(self, tag: str, children: Iterable[Any] = (), attributes: Mapping[str, str] = MappingProxyType({}), **more_attributes: str):
        if isinstance(children, str):
            children = children,

        object.__setattr__(self, 'tag', tag)
        object.__setattr__(self, 'children', tuple(children))
        object.__setattr__(self, 'attributes', MappingProxyType(ChainMap(attributes, more_attributes)))

    def __html__(self):
        start = f'<{escape(self.tag)}{"".join(_render_attr(name, value) for name, value in self.attributes.items())}'

        if self.children:
            return f'{start}>{"".join(_render_child(child) for child in self.children)}</{escape(self.tag)}>'
        else:
            return f'{start} />'

    def with_attrs(self, attrs: Mapping[str, str]) -> Element:
        return Element(self.tag, self.children, self.attributes, **attrs)
