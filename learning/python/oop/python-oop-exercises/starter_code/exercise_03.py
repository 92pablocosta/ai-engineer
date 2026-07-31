class Player:
    def __init__(self):
        self.score = 0


first_player = Player()
second_player = Player()
first_player.score = 10
print(first_player.score)
print(second_player.score)

# output
# 10
# 0
# Changing first_player.score does not change second_player.score because they are two different objects.