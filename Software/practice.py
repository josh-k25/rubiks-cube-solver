class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def main():
    r1 = Rectangle(4, 5)
    r2 = Rectangle(10, 2)

    print(r1.width)
    print(r1.height)
    print(r1.area())

    print(r2.width)
    print(r2.height)
    print(r2.area())


if __name__ == "__main__":
    main()