class Person:
    def set_age(self, age):
        if age < 0:
            raise ValueError("age cannot be negative")
        self.age = age


person = Person()
# TODO: trigger and catch a missing method error and an invalid age error.
