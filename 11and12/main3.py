"""player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()

print(player_health)

# There is no Block Scope

if 3 > 2:
    a_variable = 10
"""

game_level = 3
def create_enemey():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    else:
        new_enemy = enemies[1]