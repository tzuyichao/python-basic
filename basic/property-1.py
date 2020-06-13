class Rectangle:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, new_x):
        if new_x < 0:
            raise ValueError("new x < 0")
        self._x = new_x

    @y.setter
    def y(self, new_y):
        if new_y < 0:
            raise ValueError("new y < 0")
        self._y = new_y


if __name__ == "__main__":
    r = Rectangle(5, 3)
    try:
        r.x = -10
    except Exception as e:
        print(e)
