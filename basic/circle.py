class Circle:
    def __init__(self):
        self.radius = 1
    def area(self):
        return self.radius*self.radius*3.14159

if __name__ == "__main__":
    c = Circle()
    print(c.area())