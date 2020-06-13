class Circle:
    all_circles = []
    pi = 3.14159

    def __init__(self, r=1):
        self.radius = r
        self.__class__.all_circles.append(self)

    def area(self):
        return self.radius * self.radius * self.__class__.pi

    @staticmethod
    def total_area():
        """計算all_circles"""
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total


if __name__ == "__main__":
    c = Circle()
    print(c.area())
    c1 = Circle(3)
    print(Circle.total_area())
