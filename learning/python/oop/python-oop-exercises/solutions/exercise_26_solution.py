class Vehicle:
    def describe(self):
        return "vehicle"


class Bicycle(Vehicle):
    def describe(self):
        return f"{super().describe()}: bicycle"


print(Bicycle().describe())
