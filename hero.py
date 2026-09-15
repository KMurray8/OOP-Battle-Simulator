import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 16

    def attack(self):
        ### Returns a random value 1 through this hero's attack power. ###
        return(random.randint(1, self.attack_power))

    def take_damage(self, damage):
        ### Subtract damage, doesn't let fall below 0. ###
