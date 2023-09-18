from GameLogic.Organisms.Animal import Animal
from GameLogic.Coordinate import Coordinate
import random


class Human(Animal):

    def __init__(self, position: Coordinate):
        super().__init__(position)
        self.strength = 5
        self.initiative = 4
        self.direction = "None"
        self.superpower_turns_left = 0

    def create_child(self, position: Coordinate):
        raise Exception("Human reproduction")

    def superpower_activate(self):
        if self.superpower_turns_left == 0:
            self.superpower_turns_left = 5

    def check_superpower(self):
        self.reach = 1
        if self.superpower_turns_left > 0:
            if self.superpower_turns_left >= 3 or (self.superpower_turns_left > 0 and random.randint(0, 1) == 1):
                self.reach = 2
            self.superpower_turns_left -= 1

    def move_check(self, move: Coordinate):
        if self.direction == "UP":
            return move.x == self.position.x and move.y < self.position.y
        elif self.direction == "DOWN":
            return move.x == self.position.x and move.y > self.position.y
        elif self.direction == "LEFT":
            return move.x < self.position.x and move.y == self.position.y
        elif self.direction == "RIGHT":
            return move.x > self.position.x and move.y == self.position.y
        else:
            return False

    def action(self):
        super().action()
        self.direction = "None"

