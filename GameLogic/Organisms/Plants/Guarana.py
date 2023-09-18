from GameLogic.Organisms.Plant import Plant
from GameLogic.Coordinate import Coordinate
from GameLogic.Organism import  Organism

class Guarana(Plant):
    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 0

    def create_seeds(self, position: Coordinate):
        return Guarana(position)

    def collision(self, other: Organism):
        super().collision(other)
        other.strength += 3



