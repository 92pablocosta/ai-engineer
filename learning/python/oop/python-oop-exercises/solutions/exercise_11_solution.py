class Person:
    def set_age(self, age):
        if age < 0:
            raise ValueError("age cannot be negative")
        self.age = age


person = Person()
try:
    person.greet()
except AttributeError:
    print("missing method: AttributeError")
try:
    person.set_age(-1)
except ValueError:
    print("invalid age: ValueError")
