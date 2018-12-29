import logging
from dataclasses import field
from http import HTTPStatus
from typing import Dict, Callable, Any, Union, Tuple
from wsgiref.util import shift_path_info

from my_utils.typing import wsgi


class HTTPStatusException(Exception):
    status: HTTPStatus
    info: str = ''
    headers: wsgi.ResponseHeaders = field(default_factory=list)


class Node(wsgi.Callable):
    methods: Dict[str, wsgi.Callable]  # Methods should be stored as uppercase.
    subnodes: Dict[str, 'Node']
    subnode_patterns: Dict[Callable[[str], Any], 'Node']  # Requires preservation of insertion order.

    def __init__(self):
        self.methods = {}
        self.subnodes = {}

    def __getitem__(self, key: str) -> 'Node':
        try:
            return self.subnodes[key]
        except KeyError:
            for pattern, subnode in reversed(
                    tuple(self.subnode_patterns.items())):  # The newest patterns have priority.
                # noinspection PyBroadException
                try:
                    pattern(key)
                except Exception:
                    pass
                else:
                    return subnode  # Always returns the node.
            else:
                return self.subnodes.setdefault(key, Node())  # Creates a new node if not found.

    def get(self, key: str) -> Union['Node', Tuple[Any, 'Node']]:
        try:
            return self.subnodes[key]
        except KeyError as ex:
            for pattern, subnode in reversed(
                    tuple(self.subnode_patterns.items())):  # The newest patterns have priority.
                # noinspection PyBroadException
                try:
                    key_object = pattern(key)
                except Exception:
                    pass
                else:
                    return key_object, subnode  # Sometimes returns a (key_object, node) tuple.
            else:
                raise KeyError(f'Key not found in {self!r}') from ex  # Errors if not found.

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.subnodes[key] = value
        else:
            del self.subnode_patterns[key]  # Make sure to add to the end.
            self.subnode_patterns[key] = value

    def update(self, node: 'Node'):
        self.methods.update(node.methods)

        for key, subnode in node.subnodes.items():
            self.subnodes.setdefault(key, Node()).update(subnode)

        for pattern, subnode in node.subnode_patterns.items():
            self.subnode_patterns.setdefault(pattern, Node()).update(subnode)

    def match(self, environ: wsgi.Environ):
        try:
            x = self.get(shift_path_info(environ))

            if isinstance(x, tuple):
                f, arg = x
                return f, (arg,)
            else:
                return x, ()
        except (IndexError, KeyError):
            return self.methods[environ['REQUEST_METHOD']]

    def __call__(self, environ: wsgi.Environ, start_response: wsgi.StartResponse, *args: Any) -> wsgi.Iterable:
        try:
            f, more_args = self.match(environ)
        except KeyError:
            if self.methods:
                start_response('405 Method Not Allowed', ['Allow', ', '.join(self.methods)])
            else:
                start_response('404 Not Found', [])

            return ()

        try:
            return f(environ, start_response, *args, *more_args)
        except HTTPStatusException as ex:
            start_response(ex.status, ex.headers)
            return ex.info,
        except Exception as ex:
            logging.error(ex)
            start_response('500 Internal Error', [])
            return ()
