from GameLogic.Organism import Organism
from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate


class Fox(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 3
        self.initiative = 7

    def move_check(self, move: Coordinate):
        potential_opponent = self.world_reference.find_organism_at_position(move)
        potential_opponent: Organism
        if potential_opponent is not None and potential_opponent.strength > self.strength:
            # self.world_reference.add_event(str(self) + " detects danger at " + str(move))
            return False
        else:
            return True

    def create_child(self, position: Coordinate):
        return Fox(position)
