class A:
    def process(self):
        pass


class B(A):
    def process(self):
        pass


class C(B):
    def process(self):
        pass


# TODO: call C().process() and match the documented trace.
