from .pair import Pair
from math import sqrt


class Coordinate(Pair):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Coordinate({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Coordinate({self.x}, {self.y})"

    def calculate_distance(self, other: "Coordinate") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
