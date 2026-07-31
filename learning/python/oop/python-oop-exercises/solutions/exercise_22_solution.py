class Phone:
    def status(self):
        return "phone online"


class Laptop:
    def status(self):
        return "laptop charging"


def announce(device):
    return device.status()  # The function depends on behavior, not class identity.


print(announce(Phone()))
print(announce(Laptop()))
