import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 14

    def attack(self):
        """ Returns a random value 1 through this hero's attack power. """
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """ Subtract damage, doesn't let fall below 0. """
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}.")

    def is_alive(self):
        """Returns True when the Hero has health remaining."""
        return self.health > 0

    #def healingPotion(self):
        #if self.health < 15:
            #if random.randint(1,2) == 2:
                #potionStrength = random.randint(1, 50)
                #self.health += potionStrength
                #print(f"{self.name} uses a healing potion, gaining {potionStrength}.")
                #print(f"{self.name}'s Health = {self.health}")