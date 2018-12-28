from functools import partial
from itertools import count, product
from typing import Callable, Iterable, NamedTuple

from PIL import Image

from d3 import Point


class Element(NamedTuple):
    axis: Callable[[Point, float], Point]
    direction: bool
    
    @property
    def direction_float(self):
        return self.direction * 2 - 1
    
    def apply(self, point: Point) -> Point:
        return self.axis(point, self.direction_float)


def generate_point(start_point: Point, sequence: Iterable[Element]) -> Point:
    point = start_point
    
    for element in sequence:
        point = element.apply(point)
    
    return point


def is_valid_sequence(sequence: Iterable[Element]) -> bool:
    advanced_sequence = iter(sequence)
    
    try:
        next(advanced_sequence)
    except StopIteration:
        return True
    
    for x, y in zip(sequence, advanced_sequence):
        if x.axis == y.axis and x.direction != y.direction:
            return False
    
    return True


def generate_sequences() -> Iterable[Iterable[Element]]:
    elements = (Element(Point.rotate_x, False), Element(Point.rotate_x, True), Element(Point.rotate_y, False),
                Element(Point.rotate_y, True))
    
    for length in count():
        for sequence in product(elements, repeat=length):
            if is_valid_sequence(sequence):
                yield sequence


def generate_points(start_point: Point) -> Iterable[Point]:
    return map(partial(generate_point, start_point), generate_sequences())


if __name__ == '__main__':
    __import__('os').system('rm output/*')
    
    image = Image.new('L', (101, 101), 255)
    frames = [image.copy()]
    start_point = Point(0, 0, 1)
    
    for i, point in zip(range(20), generate_points(start_point)):
        image.putpixel((round(point.x * 50 + 50), round(point.y * 50 + 50)), 0)
        image.save(f'output/{i}.gif')
        frames.append(image.copy())
    
    image.save('output/animation.gif', save_all=True, append_images=frames)
