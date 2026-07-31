# Refactor these ideas into a Timer class without global state.
class Timer:
    def __init__(self):
        self.elapsed_seconds = 0

    def tick(self):
        self.elapsed_seconds += 1

    def get_seconds(self):
        return self.elapsed_seconds


timer = Timer()
for _ in range(3):
    timer.tick()
print(timer.get_seconds())
