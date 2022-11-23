import math
from curve import Curve
from dimension import Dimension
from coordinate import Coordinate

class SnakeCurve(Curve):
    def __init__(self, num_of_elements:int, dimension:Dimension) -> None:
        super().__init__(num_of_elements, dimension)

    def get_d(self, coordinate:Coordinate) -> int:
        d:int = coordinate.y * self.get_dimension().x

        #NOTE:Talk to Professor about this. (5, 5) == (4, 4)
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

    def define_dimension(self, number_of_elements:int) -> Dimension:
       d = math.ceil(math.sqrt(number_of_elements))
       return Dimension(d, d)

