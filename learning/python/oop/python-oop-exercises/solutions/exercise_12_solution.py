class Game:
    def __init__(self):
        self._level = 1

    def set_level(self, level):
        if not 1 <= level <= 5:
            return False
        self._level = level
        return True

    def get_level(self):
        return self._level


game = Game()
print(game.set_level(99))
print(game.get_level())
print(game.set_level(4))
print(game.get_level())
