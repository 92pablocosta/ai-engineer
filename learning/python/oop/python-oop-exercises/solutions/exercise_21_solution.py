class Circle:
    def draw(self):
        return "circle"


class Square:
    def draw(self):
        return "square"


for shape in [Circle(), Square()]:
    print(shape.draw())  # Same call, different object behavior.
