class Person:
    
    def __init__(self, direction: str, r: int, c: int):
        self._direction = direction

        # Note: the internal coordinates are (row, column) which requires
        # a little care when thinking about Person movement since it is
        # the inversion of the usual (x, y) coordinate order. I.e. moving
        # 'up' decreases the row number, 'down' increases the row number
        # 'left' decreases the column number and 'right' increases the
        # column number.
        self._r = r
        self._c = c

    def __repr__(self):
        return "Person({!r}, {}, {})".format(
            self._direction,
            self._r,
            self._c
        )        

    def __str__(self):
        return "{!r}".format(self)

    @property
    def row(self):
        return self._r

    @property
    def col(self):
        return self._c

    @property
    def coords(self):
        return (self._r, self._c)

    def move(self):
        if self._direction is 'U':
            self._r -= 1
        elif self._direction is 'D':
            self._r += 1
        elif self._direction is 'R':
            self._c += 1
        else:
            self._c -= 1
