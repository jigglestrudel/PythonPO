from abc import abstractmethod

from GameLogic.Organism import Organism
from GameLogic.Coordinate import Coordinate
import random


class Animal(Organism):

    def __init__(self, position):
        super().__init__(position)
        self.reach = 1
        self.last_position = position

    @abstractmethod
    def create_child(self, position: Coordinate) -> Organism:
        pass

    def did_run_away(self):
        return False

    def did_bounce_off_attack(self, attacker: Organism):
        pass

    def move_check(self, move: Coordinate):
        return True

    def action(self):
        valid_moves = self.world_reference.get_valid_moves(self.position, self.reach)
        for dest in valid_moves.copy():
            if not self.move_check(dest):
                valid_moves.remove(dest)
        self.last_position = self.position
        if len(valid_moves) > 0:
            self.position = random.choice(valid_moves)

    def breed(self, colliding):
        self.position = self.last_position
        valid_places = self.world_reference.get_valid_moves(self.position, 1)
        valid_places += self.world_reference.get_valid_moves(colliding.position, 1)
        for dest in valid_places.copy():
            if self.world_reference.find_organism_at_position(dest) is not None:
                valid_places.remove(dest)
        if len(valid_places) > 0:
            baby = self.create_child(random.choice(valid_places))
            self.world_reference.add_organism(baby)
            self.world_reference.add_event(str(self) + " and " + str(colliding) + " gave birth to " + str(baby))
        else:
            # self.world_reference.add_event(str(self) + " and " + str(colliding) + " failed to make a baby")
            pass

    def collision(self, colliding: Organism):
        # breeding
        if isinstance(colliding, self.__class__) and isinstance(self, colliding.__class__):
            self.breed(colliding)
        # attack
        elif isinstance(colliding, Animal):
            # antelope check
            if colliding.did_run_away():
                pass

            # tortoise check
            elif colliding.did_bounce_off_attack(self):
                self.position = self.last_position

            # kill check
            elif self.strength >= colliding.strength:
                colliding.die(self)

            # death
            else:
                self.die(colliding)

        else:
            # plant
            colliding.collision(self)

    def die(self, killer):
        self.world_reference.add_event(str(self) + " has been killed by " + str(killer))
        super().die(killer)

    def is_hogweed_resistant(self):
        return False








