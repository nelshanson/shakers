from .directions import Direction

class Person:
    
    def __init__(self, direction: Direction, x: int, y: int):
        self._direction = direction
        self._x = x
        self._y = y

    def __repr__(self):
        return "Person({!r}, {}, {})".format(
            self._direction,
            self._x,
            self._y
        )        

    def __str__(self):
        return "{!r}".format(self)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coords(self):
        return (self._x, self._y)

    def move(self):
        if self._direction is Direction.U:
            self._y += 1
        elif self._direction is Direction.D:
            self._y -= 1
        elif self._direction is Direction.R:
            self._x += 1
        else:
            self._x -= 1
