from functools import partial, wraps
from inspect import signature
from types import FunctionType
from typing import Any, Callable, Generic, Iterable, Mapping, TypeVar, Union, overload
from typing_extensions import Protocol

from my_utils.iterables import Reiterable

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
U = TypeVar("U")
U_contra = TypeVar("U_contra", contravariant=True)
V = TypeVar("V")
V_contra = TypeVar("V_contra", contravariant=True)
W = TypeVar("W")
W_contra = TypeVar("W_contra", contravariant=True)


def tee(x: T, funcs: Iterable[Callable[[T], Any]]) -> T:
    for f in funcs:
        f(x)

    return x


def tee_f(funcs: Iterable[Callable[[T], Any]]) -> Callable[[T], T]:
    def decorator(x: T) -> T:
        return tee(x, funcs)

    return decorator


@overload
def compose() -> Callable[[T], T]:
    ...


@overload
def compose(__callable: Callable[[T], U]) -> Callable[[T], U]:
    ...


@overload
def compose(
    __callable_1: Callable[[T], U], __callable_2: Callable[[U], V]
) -> Callable[[T], V]:
    ...


@overload
def compose(
    __callable_1: Callable[[T], U],
    __callable_2: Callable[[U], V],
    __callable_3: Callable[[V], W],
) -> Callable[[T], W]:
    ...


@overload
def compose(
    __callable_1: Callable[[T], U],
    __callable_2: Callable[[U], V],
    __callable_3: Callable[[V], W],
    *__callables: Callable[[W], W]
) -> Callable[[T], W]:
    ...


@overload
def compose(
    __callable_1: Callable[[T], U],
    __callable_2: Callable[[U], V],
    __callable_3: Callable[[V], W],
    *__callables: Callable[[Any], Any]
) -> Callable[[T], Any]:
    ...


def compose(*callables: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def f(arg):
        for callable in reversed(callables):
            arg = callable(arg)

        return arg

    return f


@overload
def wrap(outer: Callable[[U], V]) -> Callable[[Callable[[T], U]], Callable[[T], V]]:
    ...


@overload
def wrap(outer: Callable[[T], U]) -> Callable[[Callable[..., T]], Callable[..., U]]:
    ...


def wrap(outer: Callable[[T], U]) -> Callable[[Callable[..., T]], Callable[..., U]]:
    def decorator(inner: Callable[..., T]) -> Callable[..., U]:
        @wraps(inner)
        def wrapped(*args, **kwargs) -> U:
            return outer(inner(*args, **kwargs))

        return wrapped

    return decorator


def constant(x: T) -> Callable[..., T]:
    def f() -> T:
        return x

    return f


identity: Callable[[T], T] = compose()


def call_is_valid(
    func: Callable, args: Iterable[Any], kwargs: Mapping[str, Any]
) -> bool:
    sig = signature(func)

    try:
        sig.bind(args, kwargs)
    except TypeError:
        return False
    else:
        return True

    # Who needs version control when you have comments? :P
    #
    # new_fn = FunctionType(CodeType(
    #      func.__code__.co_argcount,        # For args
    #      func.__code__.co_kwonlyargcount,  # For args
    #      func.__code__.co_nlocals,         # For args?
    #     empty.__code__.co_stacksize,       # For code
    #      func.__code__.co_flags,           # For args
    #     empty.__code__.co_code,            # For code
    #     empty.__code__.co_consts,          # For code
    #      func.__code__.co_names,           # For args?
    #      func.__code__.co_varnames,        # For args?
    #      func.__code__.co_filename,
    #      func.__code__.co_name,
    #     empty.__code__.co_firstlineno,     # For code
    #     empty.__code__.co_lnotab           # For code
    # ), {})
    #
    # new_fn.__defaults__ = func.__defaults__
    # new_fn.__kwdefaults__ = func.__kwdefaults__
    #
    # try:
    #     new_fn(*args, **kwargs)
    # except TypeError:
    #     return False
    # else:
    #     return True


def call_converted(f, kwargs):
    return f(**{k: f.__annotations__[k](v) for k, v in kwargs.items()})


class _Curried_1(Generic[T_co, U_contra], Protocol):
    @overload
    def __call__(self) -> "_Curried_1[T_co, U_contra]":
        ...

    @overload
    def __call__(self, u: U_contra) -> T_co:
        ...


class _Curried_2(Generic[T_co, U_contra, V_contra], Protocol):
    @overload
    def __call__(self) -> "_Curried_2[T_co, U_contra, V_contra]":
        ...

    @overload
    def __call__(self, u: U_contra) -> _Curried_1[T_co, V_contra]:
        ...

    @overload
    def __call__(self, u: U_contra, v: V_contra) -> T_co:
        ...


class _Curried_3(Generic[T_co, U_contra, V_contra, W_contra], Protocol):
    @overload
    def __call__(self) -> "_Curried_3[T_co, U_contra, V_contra, W_contra]":
        ...

    @overload
    def __call__(self, u: U_contra) -> _Curried_2[T_co, V_contra, W_contra]:
        ...

    @overload
    def __call__(self, u: U_contra, v: V_contra) -> _Curried_1[T_co, W_contra]:
        ...

    @overload
    def __call__(self, u: U_contra, v: V_contra, w: W_contra) -> T_co:
        ...


@overload
def curry(f: Callable[[], T]) -> T:
    ...


@overload
def curry(f: Callable[[U], T]) -> _Curried_1[T, U]:
    ...


@overload
def curry(f: Callable[[U, V], T]) -> _Curried_2[T, U, V]:
    ...


@overload
def curry(f: Callable[[U, V, W], T]) -> _Curried_3[T, U, V, W]:
    ...


def curry(f: Callable[..., T]) -> Union[T, Callable[..., T]]:
    @wraps(f)
    def curried(*args, **kwargs):
        if call_is_valid(f, args, kwargs):
            return f(*args, *kwargs)
        else:
            return partial(curried, *args, **kwargs)

    return curried()
