from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate
import random

class Antelope(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 4
        self.initiative = 4
        self.reach = 2

    def create_child(self, position: Coordinate):
        return Antelope(position)

    def did_run_away(self):
        if random.randint(0, 1) == 1:
            valid_runs = self.world_reference.get_empty_tiles(self.position)

            self.last_position = self.position
            if len(valid_runs) > 0:
                position = random.choice(valid_runs)
                self.world_reference.add_event(str(self) + " runs away to " + str(position))
                self.position = position
                return True
        return False

