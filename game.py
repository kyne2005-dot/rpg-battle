import random
from character import Character

# Each event: (story text, "damage" or "heal", min amount, max amount)
STORY = [
    ("You are traveling down the road and BAM, a major attack from an enemy! You engage in battle.", "damage", 25, 25),
    ("After the fight you stop to rest.", "heal", 10, 10),
    ("You run into another enemy and engage in battle.", "damage", 1, 50),
    ("After the battle you move on and find a chest.", "heal", 1, 50),
    ("You run into another enemy and engage in battle.", "damage", 25, 75),
    ("After the battle you find a super chest.", "heal", 20, 50),
]


def play_event(player, text, kind, low, high):
    print(f"\n{text}")
    amount = random.randint(low, high)
    if kind == "damage":
        player.take_damage(amount)
        print(f"You took {amount} damage!")
    else:
        player.heal(amount)
        print(f"Healing +{amount}!")
    print(player)


def main():
    player = Character("Hero")
    print(player)
    for text, kind, low, high in STORY:
        play_event(player, text, kind, low, high)
        if not player.is_alive():
            print("\nYou died. Game over.")
            return
    print("\nYou survived the road!")


if __name__ == "__main__":
    main()