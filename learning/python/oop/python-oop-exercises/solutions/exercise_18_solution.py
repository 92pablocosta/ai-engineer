class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        return self.width * self.height


rectangle = Rectangle()
rectangle.width = 3
rectangle.height = 4
print(rectangle.area())
