class Worker:
    def report(self):
        return "worker"


class Engineer(Worker):
    def report(self):
        pass


class SeniorEngineer(Engineer):
    def report(self):
        pass


# TODO: print the chained report.
