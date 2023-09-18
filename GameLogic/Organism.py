from abc import ABC
from abc import abstractmethod
from GameLogic.Coordinate import Coordinate
from GameLogic.World import World


class Organism(ABC):
    world_reference: World

    def __init__(self, position):
        self._strength = 0
        self._initiative = 0
        self._position = position
        self.age = 0
        self.world_reference = None

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def action(self):
        pass

    def age_up(self):
        self.age += 1

    def die(self, killer):
        self.world_reference.remove_organism(self)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: Coordinate):
        self._position = position

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, s: int):
        self._strength = s

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, i: int):
        self._initiative = i

    def is_hogweed_resistant(self):
        return True

    def is_fire_resistant(self):
        return False

    def __str__(self):
        return self.__class__.__name__ + " at " + str(self.position)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['world_reference']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

