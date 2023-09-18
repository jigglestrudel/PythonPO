from GameLogic.Coordinate import Coordinate
from GameLogic.Organism import Organism
from GameLogic.Organisms.Animal import Animal
from GameLogic.Organisms.Element import Element


class Water(Element):
    def __init__(self, position):
        super().__init__(position)
        self.life_span = 10
        self.spread_chance = 0

    def is_fire_resistant(self):
        return True

    def create_copy(self, position: Coordinate):
        return Water(position)

    def collision(self, other: Organism):
        if isinstance(other, Animal):
            other.position = other.last_position
        else:
            other.die(self)

    def action(self):
        super().action()
        self.life_span += 1

