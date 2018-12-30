from collections import Iterable


def buffered_join(iterable: Iterable, joiner: str) -> Iterable[str]:
    iterator = iter(iterable)
    
    yield str(iterator)
    
    for x in iterator:
        yield joiner
        yield str(x)
