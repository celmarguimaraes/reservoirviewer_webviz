from .pair import Pair


class Coordinate(Pair):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y
