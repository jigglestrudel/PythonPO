from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate
import random


class Tortoise(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 2
        self.initiative = 1

    def create_child(self, position: Coordinate):
        return Tortoise(position)

    def action(self):
        if random.randint(0, 4) == 4:
            super().action()

    def did_bounce_off_attack(self, attacker):
        if attacker.strength < 5:
            return True
        return False


