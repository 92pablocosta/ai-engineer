class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")

class Cow(Animal):
    def speak(self):
        print("Moo!!")

class Duck(Animal):
    def speak(self):
        print("Quack!")

def make_it_speak(item): # duck typing
    item.speak()


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()

print(Cat.mro())
