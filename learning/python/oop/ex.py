class Employee:
    def describe(self):
        print("Employee")


class Developer(Employee):
    def describe(self):
        super().describe()
        print("Developer")
        