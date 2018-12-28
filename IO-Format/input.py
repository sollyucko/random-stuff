from typing import Callable, Iterable, Type, TypeVar

T = TypeVar('T')


def input_value(datatype: Type[T], *, prompt: str = '', error_message: str = '', exception_type: Exception = ValueError,
                constraints: Iterable[Callable[T, bool]] = ()) -> T:
    while True:
        try:
            data = datatype(input(prompt))
            
            if all(map(lambda f: f(data), constraints)):
                return data
        except exception_type:
            pass
        
        print(error_message, end='')
