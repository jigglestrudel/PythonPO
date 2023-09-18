from GameLogic.Coordinate import Coordinate
from GameLogic.Organism import Organism
from GameLogic.Organisms.Element import Element


class Fire(Element):
    def __init__(self, position):
        super().__init__(position)
        self.life_span = 1
        self.spread_chance = 50

    def is_fire_resistant(self):
        return True

    def create_copy(self, position: Coordinate):
        flame = Fire(position)
        flame.life_span = self.life_span -1
        return flame

    def collision(self, other: Organism):
        if not other.is_fire_resistant():
            other.die(self)
            self.life_span = 2
        else:
            self.die(None)

