class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
 
    def reset(self):
        self.value = 0


counter = Counter()
counter.increment()
print(counter.increment())
print(counter.value)
counter.reset()
print(counter.value)
