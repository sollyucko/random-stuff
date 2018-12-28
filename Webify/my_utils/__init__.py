from abc import ABC
from typing import Dict, TypeVar, Union, Generic, Mapping

KT = TypeVar('KT')
VT = TypeVar('VT')


class RecursiveMapping(Generic[KT, VT], Mapping[KT, Union[VT, 'RecursiveMapping[KT, VT]']], ABC):
    pass


class RecursiveDefaultDict(RecursiveMapping[KT, VT], Dict[KT, Union[VT, 'RecursiveDefaultDict[KT, VT]']]):
    def __getitem__(self, key: KT) -> Union['RecursiveDefaultDict[KT, VT]', VT]:
        return self.setdefault(key, RecursiveDefaultDict())
