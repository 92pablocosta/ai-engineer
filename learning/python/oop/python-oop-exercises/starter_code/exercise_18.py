class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    pass  # TODO: override area using width and height.


rectangle = Rectangle()
rectangle.width = 3
rectangle.height = 4
# TODO: print rectangle.area().
