class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B start")
        super().process()
        print("B end")


class C(B):
    def process(self):
        print("C start")
        super().process()
        print("C end")


C().process()  # Calls move down the MRO, then returns outward.
