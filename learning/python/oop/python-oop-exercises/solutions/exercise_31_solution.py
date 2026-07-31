class Delivery:
    def __init__(self, label):
        self.label = label

    def estimate_days(self):
        return 0


class StandardDelivery(Delivery):
    def estimate_days(self):
        return 5


class ExpressDelivery(Delivery):
    def estimate_days(self):
        return 2


for delivery in [StandardDelivery("standard"), ExpressDelivery("express")]:
    print(f"{delivery.label}: {delivery.estimate_days()} days")
