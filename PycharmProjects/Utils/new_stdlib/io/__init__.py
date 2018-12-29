from abc import ABC, abstractmethod
from io import BufferedIOBase, IOBase, RawIOBase, TextIOBase, SEEK_CUR
from typing import Generic, TypeVar

T = TypeVar('T')


class Truncatable(ABC):
    @abstractmethod
    def truncate(self) -> None:
        pass


class Restartable(ABC):
    @abstractmethod
    def restart(self):
        pass


class AbsoluteSeekable(Restartable):
    @abstractmethod
    def seek(self, location: int) -> None:
        pass
    
    @property
    @abstractmethod
    def position(self):
        pass
    
    def restart(self):
        return self.seek(0)


class ForwardSeekable(ABC):
    @abstractmethod
    def seek_forward(self, location: int) -> None:
        pass


class BackwardSeekable(ABC):
    @abstractmethod
    def seek_backward(self, location: int) -> None:
        pass


class Readable(Generic[T], ForwardSeekable):
    @abstractmethod
    def read(self, length: int = None) -> T:
        if length == 0:
            return
        else:
            super().read(length)
    
    def seek_forward(self, location: int) -> None:
        self.read(location)


class Writable(Generic[T], ABC):
    @abstractmethod
    def write(self, data: T) -> None:
        pass


class Closeable(ABC):
    def close(self) -> None:
        pass


def wrap_file_object(file: IOBase) -> object:
    bases = set()
    class_attributes = dict()
    data_type = None
    
    if isinstance(file, TextIOBase):
        data_type = str
    elif isinstance(file, (BufferedIOBase, RawIOBase)):
        data_type = bytes
    
    if file.readable():
        def read(self: Readable, length: int = None) -> str:
            if length == None:
                return file.read()
            else:
                return file.read(length)
        
        bases.add(Readable)
        class_attributes['read'] = read

    if file.writable():
        def write(self: Writable, data: data_type):
            file.write(data)
    
        bases.add(Writable)
        class_attributes['write'] = write
    
    if file.seekable():
        def seek_forward(self: ForwardSeekable, position: int) -> None:
            file.seek(position, SEEK_CUR)
        
        def seek_backward(self: BackwardSeekable, position: int) -> None:
            file.seek(-position, SEEK_CUR)
        
        def seek(self: AbsoluteSeekable, position: int) -> None:
            if position >= 0:
                file.seek(position)
            else:
                file.seek(-(position - 1))
        
        @property
        def position(self: AbsoluteSeekable) -> int:
            return file.tell()
        
        bases.update({ForwardSeekable, BackwardSeekable, AbsoluteSeekable})
        class_attributes.update({
            'seek_forward': seek_forward,
            'seek_backward': seek_backward,
            'seek': seek,
            'position': position,
        })

    def close(self: Writable) -> None:
        file.close()

    bases.add(Closeable)
    class_attributes['close'] = close

    return type('FileObjectWrapper', tuple(bases), class_attributes)()
