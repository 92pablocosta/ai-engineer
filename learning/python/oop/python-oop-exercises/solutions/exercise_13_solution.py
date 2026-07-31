class Employee:
    def introduce(self):
        return f"I am {self.name}"


class Manager(Employee):
    pass  # The subclass needs no new behavior yet.


manager = Manager()
manager.name = "Lin"
print(manager.introduce())
