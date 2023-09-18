import random

from GameLogic.Coordinate import Coordinate


class World:
    def __init__(self, w, h):
        self._w = w
        self._h = h
        self._world_organisms = []
        self._human = None
        self._round_count = 0
        self._history = []

        self.human_direction = "None"

    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, w):
        self._w = w

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, h):
        self._h = h

    def fill_with_wolves(self):
        for x in range(self._w):
            for y in range(self._h):
                if x == self._w//2 and y == self._h//2:
                    self.spawn_human()
                    continue
                if random.randint(0, 5) < 4:
                    continue
                self.add_organism(globals()[random.choice(["Antelope", "Cybersheep", "Fox",
                                                           "Sheep", "Tortoise", "Wolf",
                                                           "Dandelion", "Grass", "Guarana",
                                                           "Hogweed", "Nightshade"])](Coordinate(x, y)))

    def clear(self):
        self._round_count = 0
        for org in self._world_organisms.copy():
            self.remove_organism(org)
        self._history.clear()

    def add_organism(self, organism_to_add):
        organism_to_add.world_reference = self
        self._world_organisms.append(organism_to_add)

    def remove_organism(self, organism_to_kill):
        if organism_to_kill in self._world_organisms:
            self._world_organisms.remove(organism_to_kill)
        else:
            # raise Exception("Organism not in World")
            pass

    def find_organism_at_position(self, position):
        for org in self._world_organisms:
            if org.position == position:
                return org
        return None

    # TO BE ABSTRACT
    def get_distance(self, start: Coordinate, end: Coordinate):
        return abs(start.x - end.x) + abs(start.y - end.y)

    # TO BE ABSTRACT
    def get_valid_moves(self, position: Coordinate, distance: int = 1):
        valid_moves = []
        for dx in range(-distance, distance + 1):
            for dy in range(-distance, distance + 1):
                offset = Coordinate(dx, dy)
                if Coordinate(0, 0) <= position + offset < Coordinate(self._w, self._h) and \
                        self.get_distance(position, position + offset) == distance:
                    valid_moves.append(position + offset)
        return valid_moves

    def get_empty_tiles(self, position: Coordinate, distance: int = 1):
        empty_tiles = []
        for dx in range(-distance, distance + 1):
            for dy in range(-distance, distance + 1):
                offset = Coordinate(dx, dy)
                if Coordinate(0, 0) <= position + offset < Coordinate(self._w, self._h) and \
                        self.get_distance(position, position + offset) == distance and \
                        self.find_organism_at_position(position + offset) is None:
                    empty_tiles.append(position + offset)
        return empty_tiles

    def get_colliding_organism(self, organism):
        for org in self._world_organisms:
            if org != organism and org.position == organism.position:
                return org
        return None

    def manage_organisms(self):
        self._history.clear()
        self._round_count += 1
        self.add_event("Turn " + str(self._round_count) + ":")

        self._world_organisms.sort(key=lambda organism: organism.age, reverse=True)
        self._world_organisms.sort(key=lambda organism: organism.initiative, reverse=True)

        if self._human not in self._world_organisms:
            self._human = None
        else:
            self._human.check_superpower()

        org: Organism
        for org in self._world_organisms.copy():

            # check if still alive
            if org in self._world_organisms:
                org.action()

                colliding = self.get_colliding_organism(org)
                if colliding is not None:
                    org.collision(colliding)

                org.age_up()

    def get_world_state(self):
        print(len(self._world_organisms))

    def is_organism_alive(self, organism):
        return organism in self._world_organisms

    def add_event(self, e):
        self._history.append(e)

    def get_events(self):
        return self._history

    def spawn_human(self):
        if self.find_organism_at_position(Coordinate(self._w//2, self._h//2)) is not None:
            self.remove_organism(self.find_organism_at_position(Coordinate(self._w//2, self._h//2)))
        self._human = Human(Coordinate(self._w//2, self._h//2))
        self.add_organism(self._human)

    def human_set_direction(self, direction ):
        if self._human is not None and self._human in self._world_organisms:
            self._human.direction = direction

    def human_activate(self):
        if self._human is not None and self._human in self._world_organisms:
            self._human.superpower_activate()

    def human_get_turns_left(self):
        if self._human is not None and self._human in self._world_organisms:
            return self._human.superpower_turns_left

    def find_nearest_hogweed(self, position: Coordinate) -> [int, Coordinate]:
        list_of_hogweeds = []
        org: Organism
        for org in self._world_organisms:
            if isinstance(org, Hogweed):
                list_of_hogweeds.append((self.get_distance(position, org.position), org.position))
        list_of_hogweeds.sort()
        if len(list_of_hogweeds) > 0:
            return list_of_hogweeds[0]
        else:
            return None, None

    def make_organisms_yours(self):
        org: Organism
        for org in self._world_organisms:
            org.world_reference = self


from GameLogic.Organism import Organism
from GameLogic.Organisms.Plants.Hogweed import Hogweed
from GameLogic.Organisms.Animals.Wolf import Wolf
from GameLogic.Organisms.Animals.Sheep import Sheep
from GameLogic.Organisms.Animals.Cybersheep import Cybersheep
from GameLogic.Organisms.Animals.Antelope import Antelope
from GameLogic.Organisms.Animals.Fox import Fox
from GameLogic.Organisms.Animals.Tortoise import Tortoise
from GameLogic.Organisms.Plants.Grass import Grass
from GameLogic.Organisms.Plants.Guarana import Guarana
from GameLogic.Organisms.Plants.Dandelion import Dandelion
from GameLogic.Organisms.Plants.Nightshade import Nightshade
from GameLogic.Organisms.Animals.Human import Human
