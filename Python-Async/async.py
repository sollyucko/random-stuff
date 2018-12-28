from collections import deque
from functools import wraps
from threading import Thread
from typing import Any, Callable, Deque, Generator, TypeVar, NoReturn

T = TypeVar('T')
G = Generator['G', Any, Any]


def run_async(f: Callable[[], Any]) -> Thread:
    thread = Thread(target=f)
    thread.run()
    return thread


def add_callback(f: Callable[[], T], success_callback: Callable[[T], ...] = lambda x: None,
                 failure_callback: Callable[[BaseException], ...] = lambda x: None) -> Callable[[], None]:
    @wraps(f)
    def g() -> None:
        try:
            x = f()
        except BaseException as e:
            failure_callback(e)
        else:
            success_callback(x)
    
    return g


def make_task(f: Callable[[], T]) -> Callable[[], Generator[None, Any, T]]:
    @wraps(f)
    def g():
        yield
        return f()
    
    return g


class AsyncManager:
    queue: Deque = deque()
    
    def add_task(self, f: Callable[[], T]) -> None:
        pass
    
    def run_event_loop(self):
        while True:
            f = self.queue.popleft()
            
