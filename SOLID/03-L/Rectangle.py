class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

    @property
    def area(self):
        return self._width*self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
