from GameLogic.Organisms.Plant import Plant
from GameLogic.Coordinate import Coordinate
from GameLogic.Organism import Organism


class Nightshade(Plant):
    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.spread_chance = 15
        self.strength = 99

    def create_seeds(self, position: Coordinate):
        return Nightshade(position)

    def collision(self, other: Organism):
        super().collision(other)
        other.die(self)

