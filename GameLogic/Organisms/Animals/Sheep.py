from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate


class Sheep(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 4
        self.initiative = 4

    def create_child(self, position: Coordinate):
        return Sheep(position)
