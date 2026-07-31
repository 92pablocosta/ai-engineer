class Vehicle:
    def describe(self):
        return "vehicle"


class Bicycle(Vehicle):
    def describe(self):
        pass  # TODO: extend the parent description with super().


# TODO: print Bicycle().describe().
