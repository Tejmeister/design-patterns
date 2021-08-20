from Rectangle import Rectangle
from Square import Square


def use_it(shape):
    w = shape.width
    shape.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {shape.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
