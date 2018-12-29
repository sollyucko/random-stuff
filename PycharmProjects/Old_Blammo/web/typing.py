from typing import Callable, Dict, Iterable, List, Tuple

__all__ = ['WSGIApp']

'''({str -> str}, (str, [(str, str)]) -> (str) -> None) -> Iterable[str]'''
WSGIApp = Callable[[Dict[str, str], Callable[[str, List[Tuple[str, str]]], Callable[[str], None]]], Iterable[str]]
