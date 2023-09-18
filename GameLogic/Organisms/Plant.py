import random
from abc import abstractmethod

from GameLogic.Organism import Organism
from GameLogic.Coordinate import Coordinate


class Plant(Organism):
    def __init__(self, position):
        super().__init__(position)
        self.initiative = 0
        self.spread_chance = 25

    @abstractmethod
    def create_seeds(self, position: Coordinate):
        pass

    def action(self):
        spread_tiles = self.world_reference.get_empty_tiles(self.position)
        if len(spread_tiles) > 0 and random.randint(0, 200) < self.spread_chance:
            seeds = self.create_seeds(random.choice(spread_tiles))
            self.world_reference.add_organism(seeds)
            self.world_reference.add_event(str(seeds) + " sprouts from " + str(self))

    def collision(self, other):
        self.die(other)

    def die(self, killer):
        self.world_reference.add_event(str(self) + " has been eaten by " + str(killer))
        super().die(killer)

