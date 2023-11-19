import math
from .curve import Curve
from .curve_utils.dimension import Dimension
from .curve_utils.coordinate import Coordinate

class SnakeCurve(Curve):
    def __init__(self, number_of_elements:int, dimension:Dimension) -> None:
        super().__init__(number_of_elements, dimension)

    @classmethod
    def from_dimension(cls, dimension:Dimension) -> 'SnakeCurve':
        return cls(dimension.x * dimension.y, dimension)

    def get_d(self, coordinate:Coordinate) -> int:
        d:int = coordinate.y * self.get_dimension().x

        if coordinate.x * coordinate.y == self.get_number_of_elements():
            return -1

        if coordinate.y % 2 == 0:
            d += coordinate.x
        else:
            d+= (self.get_dimension().x - 1) - coordinate.x

        return d if d < self.get_number_of_elements() else -1
        

    def get_coordinate(self, d:int) -> Coordinate:
        dimension:Dimension = self.get_dimension()
        y:int = int(d / dimension.x)
        x:int = int(d - y * dimension.x)
        if y % 2 == 1:
            x = (dimension.x - 1) - x

        return Coordinate(x, y)
