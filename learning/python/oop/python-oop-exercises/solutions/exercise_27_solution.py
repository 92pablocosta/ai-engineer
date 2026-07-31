class Worker:
    def report(self):
        return "worker"


class Engineer(Worker):
    def report(self):
        return f"{super().report()} -> engineer"


class SeniorEngineer(Engineer):
    def report(self):
        return f"{super().report()} -> senior"  # Follows the MRO upward.


print(SeniorEngineer().report())
