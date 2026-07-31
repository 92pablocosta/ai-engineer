class Animal:
    def move(self):
        return f"{self.kind} moves"


class Dog(Animal):
    pass


dog = Dog()
dog.kind = "Dog"
print(dog.move())
