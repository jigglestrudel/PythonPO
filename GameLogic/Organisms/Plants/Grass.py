from GameLogic.Organisms.Plant import Plant
from GameLogic.Coordinate import Coordinate


class Grass(Plant):
    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 0

    def create_seeds(self, position: Coordinate):
        return Grass(position)

