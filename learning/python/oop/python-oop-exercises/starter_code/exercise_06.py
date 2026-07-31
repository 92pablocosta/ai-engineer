class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def is_freezing(self):
        if self.celsius <= 0:
            return True
        


temperature = Temperature(0)
print(temperature.is_freezing())
print(temperature.celsius)
