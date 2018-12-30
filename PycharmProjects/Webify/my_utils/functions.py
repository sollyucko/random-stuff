from functools import wraps
from types import CodeType, FunctionType
from typing import Any, Callable, Iterable, Mapping, TypeVar

T = TypeVar('T')


def tee(x: T, funcs: Iterable[Callable[[T], Any]]) -> T:
    for f in funcs:
        f(x)
    
    return x


def tee_f(funcs: Iterable[Callable[[T], Any]]) -> Callable[[T], T]:
    def decorator(x: T) -> T:
        return tee(x, funcs)
    
    return decorator


def constant(x: T) -> Callable[..., T]:
    def f() -> T:
        return x
    
    return f


def ignore_extra_args(f: FunctionType) -> Callable[..., T]:
    arg_count = f.__code__.co_argcount
    arg_names = set(f.__code__.co_varnames)
    
    @wraps(f)
    def g(*args, **kwargs):
        return f(*args[:arg_count], **{key: value for key, value in kwargs.items() if key in arg_names})
    
    return g


def empty() -> None:
    pass


def identity(x: T) -> T:
    return x


def call_is_valid(func: FunctionType, args: Iterable[Any], kwargs: Mapping[str, Any]) -> bool:
    new_fn = FunctionType(CodeType(
         func.__code__.co_argcount,        # For args
         func.__code__.co_kwonlyargcount,  # For args
         func.__code__.co_nlocals,         # For args?
        empty.__code__.co_stacksize,       # For code
         func.__code__.co_flags,           # For args
        empty.__code__.co_code,            # For code
        empty.__code__.co_consts,          # For code
         func.__code__.co_names,           # For args?
         func.__code__.co_varnames,        # For args?
         func.__code__.co_filename,
         func.__code__.co_name,
        empty.__code__.co_firstlineno,     # For code
        empty.__code__.co_lnotab           # For code
    ), {})
    
    new_fn.__defaults__ = func.__defaults__
    new_fn.__kwdefaults__ = func.__kwdefaults__
    
    try:
        new_fn(*args, **kwargs)
    except TypeError:
        return False
    else:
        return True


def call_converted(f, kwargs):
    return f(**{k: f.__annotations__[k](v) for k, v in kwargs.items()})
