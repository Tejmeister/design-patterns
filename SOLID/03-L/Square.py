from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # These setters create problem and violate the LSP
    # To conform to LSP the solution could be to not use Square class itself as Square as a separate entity
    # is not needed actually
    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value
