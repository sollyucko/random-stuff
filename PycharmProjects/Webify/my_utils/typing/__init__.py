from __future__ import annotations

from inspect import Signature


def callable_typing_from_signature(signature: Signature):
    def __call__(): pass
    __call__

    cls = type('', {__call__}, (Protocol,))
