from typing import Iterable


class Named:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return str(self.args)


class Constant(Named):
    pass


class Function(Named):
    pass


class Class(Named):
    pass


def generate_stub(parsed: Iterable[Named]) -> str:
    return str(list(parsed))
