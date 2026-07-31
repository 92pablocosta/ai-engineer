class Animal:
    def identify(self):
        return "animal"


class Cat(Animal):
    pass


print([cls.__name__ for cls in Cat.mro()])  # Shows the lookup path.
print(Cat().identify())
