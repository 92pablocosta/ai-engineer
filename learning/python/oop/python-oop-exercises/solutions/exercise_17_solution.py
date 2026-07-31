class Person:
    def greet(self):
        return "Hello"


class Student(Person):
    def greet(self):
        return "Hello, teacher!"  # Same method name replaces inherited behavior.


print(Person().greet())
print(Student().greet())
