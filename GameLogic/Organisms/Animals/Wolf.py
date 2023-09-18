from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate


class Wolf(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 9
        self.initiative = 5

    def create_child(self, position: Coordinate):
        return Wolf(position)
