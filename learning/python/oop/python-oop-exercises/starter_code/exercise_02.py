class Car:
    def __init__(self, brand):
        self.brand = brand
        self.mileage = 0

toyota = Car("Toyota")
honda = Car("Honda")

toyota.mileage = 120

print(toyota.mileage)
print(honda.mileage)
