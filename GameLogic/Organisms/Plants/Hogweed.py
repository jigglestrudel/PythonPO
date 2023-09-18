from GameLogic.Organisms.Plant import Plant
from GameLogic.Coordinate import Coordinate
from GameLogic.Organism import Organism


class Hogweed(Plant):
    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.spread_chance = 5
        self.strength = 99

    def create_seeds(self, position: Coordinate):
        return Hogweed(position)

    def collision(self, other: Organism):
        super().collision(other)
        if not other.is_hogweed_resistant():
            other.die(self)

    def action(self):
        targets = self.world_reference.get_valid_moves(self.position, 1)
        for position in targets:
            victim = self.world_reference.find_organism_at_position(position)
            victim: Organism
            if victim is not None and not victim.is_hogweed_resistant():
                victim.die(self)
        super().action()



