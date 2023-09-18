from math import sqrt

class Coordinate:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Coordinate(self.x * other, self.y * other)

    # ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # <=
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    # <
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    # >=
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    # >
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __str__(self):
        return "(" + self.x.__str__() + ", " + self.y.__str__() + ")"
