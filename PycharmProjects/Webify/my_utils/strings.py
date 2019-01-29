from collections import Iterable
from typing import AnyStr


def buffered_join(iterable: Iterable, joiner: str) -> Iterable[str]:
    iterator = iter(iterable)
    
    yield str(iterator)
    
    for x in iterator:
        yield joiner
        yield str(x)


def before_first(string: AnyStr, substring: AnyStr) -> AnyStr:
    return string[:string.find(substring)]  # [0:i)


def after_last(string: AnyStr, substring: AnyStr) -> AnyStr:
    return string[string.rfind(substring)+1:]  # (i:n)
