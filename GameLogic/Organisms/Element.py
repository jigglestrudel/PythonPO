import random
from abc import abstractmethod

from GameLogic.Organism import Organism
from GameLogic.Coordinate import Coordinate


class Element(Organism):
    def __init__(self, position):
        super().__init__(position)
        self.initiative = 100
        self.spread_chance = 50
        self.life_span = 5

    @abstractmethod
    def create_copy(self, position: Coordinate):
        pass

    def action(self):
        if self.life_span <= 0:
            self.die(None)
            return
        spread_tiles = self.world_reference.get_valid_moves(self.position)
        for dest in spread_tiles:
            if random.randint(0, 100) < self.spread_chance:
                seeds = self.create_copy(dest)
                self.world_reference.add_organism(seeds)
                self.world_reference.add_event(str(seeds) + " spreads from " + str(self))
                colliding = self.world_reference.get_colliding_organism(seeds)
                if colliding is not None:
                    seeds.collision(colliding)
        self.life_span -= 1

    def collision(self, other):
        other.die(self)

    def is_hogweed_resistant(self):
        return True

    def die(self, killer):
        if killer is None:
            self.world_reference.add_event(str(self) + " has been destroyed")
        else:
            self.world_reference.add_event(str(self) + " has been destroyed by " + str(killer))
        super().die(killer)


