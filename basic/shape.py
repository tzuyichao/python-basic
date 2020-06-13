class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side


if __name__ == "__main__":
    s = Square()
    s.move(1, 1)
    print("x={}, y={}".format(s.x, s.y))
