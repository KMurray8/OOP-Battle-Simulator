from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Forest's Eye"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        heroDamage = hero.attack()
        enemy.take_damage(heroDamage)

        if enemy.is_alive():
            enemyDamage = enemy.attack()
            hero.take_damage(enemyDamage)

    if hero.is_alive():
        print (f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print("     ")
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Jeffy")
    goblin2 = Goblin("Scribble")
    hero = Hero("Lauriel")

    print(f"{hero.name} enters the arena with {hero.health} health.")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("      ")
    battle(hero, goblin)





if __name__ == "__main__":
    main()
