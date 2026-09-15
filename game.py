from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Forest's Eye"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Jeffy")

    goblin2 = Goblin("Scribble")

    hero = Hero("Lauriel")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    print(f"{hero.name} has answered the call.")


if __name__ == "__main__":
    main()
