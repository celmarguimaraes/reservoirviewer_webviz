from .pair import Pair


class Dimension(Pair):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
