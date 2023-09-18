from GameLogic.Organisms.Animals.Sheep import Sheep
from GameLogic.Coordinate import Coordinate
import random


class Cybersheep(Sheep):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 11
        self.initiative = 4

    def create_child(self, position: Coordinate):
        return Cybersheep(position)

    def is_hogweed_resistant(self):
        return True

    def is_fire_resistant(self):
        return True

    def breed(self, colliding):
        self.position = self.last_position

    def action(self):
        distance, found_hogweed = self.world_reference.find_nearest_hogweed(self.position)
        if found_hogweed is None:
            super().action()
        else:
            valid_moves = self.world_reference.get_valid_moves(self.position, self.reach)
            for dest in valid_moves.copy():
                if self.world_reference.get_distance(dest, found_hogweed) > distance - self.reach:
                    valid_moves.remove(dest)

            self.last_position = self.position
            if len(valid_moves) > 0:
                self.position = random.choice(valid_moves)
