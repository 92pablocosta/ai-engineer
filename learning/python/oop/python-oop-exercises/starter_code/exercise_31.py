class Delivery:
    def __init__(self, label):
        self.label = label

    def estimate_days(self):
        pass


class StandardDelivery(Delivery):
    pass


class ExpressDelivery(Delivery):
    pass


# TODO: loop through both objects and print their estimates.
