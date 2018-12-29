from math import inf
from numbers import Complex


class Range:
    def __init__(self, start: Complex = 0, stop: Complex = inf, step: Complex = 1, include_start: bool = True, include_end: bool = False):
        self.is_start = True    
        self.current = start
        self.stop = stop
        self.step = step
        self.include_start = include_start
        self.include_end = include_end
    
    def __repr__(self):
        return (f'{self.__class__.__name__}({self.current}, {self.stop}, {self.step}, '
                f'{self.include_start or not self.is_start}, {self.include_end})')
    
    def __iter__(self):
        return Range(self.current, self.stop, self.step, self.include_start or not self.is_start, self.include_end)
    
    def __next__(self):
        try:
            if self.current == self.stop:
                if self.include_end:
                    return self.current
                else:
                    raise StopIteration
            elif self.step == 0:
                return self.current
            elif self.include_start and self.is_start:
                return self.current
            elif self.current / self.step > self.stop / self.step:
                raise StopIteration
            else:
                return self.current
        finally:
            self.is_start = False
            self.current += self.step
