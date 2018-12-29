from functools import partial
from itertools import product, starmap

from PIL import Image, ImageDraw
from mpmath import *


def convert_image(image: Image.Image) -> Image.Image:
    return image.convert('L').point(lambda x: 0 if x < 128 else 255, 'L')


def calculate_fractal_dimension_helper(image: Image.Image, box_size: int):
    box_size = int(box_size)
    boxes = count_partial_boxes(image, box_size)
    ans = log(boxes) / log(min(image.height, image.width) / box_size)
    print(box_size, boxes, ans)
    return ans


def calculate_fractal_dimension(image: Image.Image) -> float:
    direction = min(image.height, image.width)
    return float(limit(partial(calculate_fractal_dimension_helper, image), 1, direction=direction))


def any_but_not_all(iterable):
    at_least_one_true = False
    not_all_true = False
    
    for x in iterable:
        at_least_one_true = at_least_one_true or x
        not_all_true = not_all_true or not x
        
        if at_least_one_true and not_all_true:
            return True
    
    return False


def is_partial_box(image: Image.Image, box_size: int, start_x: int, start_y: int):
    return any_but_not_all(starmap(Image.Image.getpixel, product(
        (image,),
        product(
            range(start_x, min(image.width, start_x + box_size)),
            range(start_y, min(image.height, start_y + box_size))
        )
    )))


def count_partial_boxes(image: Image.Image, box_size: int) -> float:
    return sum(starmap(is_partial_box, product((image,), (box_size,), range(0, image.width, box_size),
                                               range(0, image.height, box_size))))


def calc_from_path(image_path: str):
    return calculate_fractal_dimension(convert_image(Image.open(image_path)))


def decorate_image(image: Image.Image, box_size: int):
    count = 0
    
    for x, y in product(range(0, image.width, box_size), range(0, image.height, box_size)):
        if is_partial_box(image, box_size, x, y):
            count += 1
            for x2, y2 in product(range(x, min(image.width, x + box_size)), range(y, min(image.height, y + box_size))):
                image.putpixel((x2, y2), 100 if image.getpixel((x2, y2)) else 50)
    
    ImageDraw.Draw(image).text((0, 0),
                               f'Box size: {box_size}\nBox count: {count}\nDimension: {log(count) / log(min(image.height, image.width) / box_size)}',
                               200)
