class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def is_freezing(self):
        return self.celsius <= 0  # This query does not alter state.


temperature = Temperature(0)
print(temperature.is_freezing())
print(temperature.celsius)
