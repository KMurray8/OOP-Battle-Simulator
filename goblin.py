import random
from enemy import Enemy


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100, 15)

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)