from GameLogic.Organisms.Plant import Plant
from GameLogic.Coordinate import Coordinate


class Dandelion(Plant):
    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 0

    def create_seeds(self, position: Coordinate):
        return Dandelion(position)

    def action(self):
        for _ in range(3):
            super().action()

