enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

# Local Scope

def drink_portion():
    potion_strength = 2
    print(potion_strength)
# Global Scope
player_health = 10

if __name__ == "__main__":
    increase_enemies()
    print(f"enemies outside function: {enemies}")
    print(player_health)