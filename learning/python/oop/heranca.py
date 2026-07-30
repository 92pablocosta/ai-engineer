class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

car = Car()
car.start()
