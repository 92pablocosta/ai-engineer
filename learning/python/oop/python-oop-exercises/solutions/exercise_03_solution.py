class Player:
    def __init__(self):
        self.score = 0


first_player = Player()
second_player = Player()
first_player.score = 10  # This changes only the first instance.
print(first_player.score)
print(second_player.score)
