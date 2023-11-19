from typing import List
import math

from ..curve_utils.dimension import Dimension
from .zhang_utils import PseudoHilbert
from ..curve import Curve
from ..curve_utils.coordinate import Coordinate


class ZhangCurve(Curve):
    map_d_to_xy: List[Coordinate]
    map_xy_to_d: List[List[int]]
    curve_generator: PseudoHilbert
    
    def __init__(self, num_of_elements: int, dimension: Dimension):
        # if num_of_elements > dimension.x * dimension.y:
        #     raise ValueError('Número de elementos não pode ser maior que a quantidade de coordenadas disponíveis na dimensão.')
        super().__init__(num_of_elements, dimension)
        self.curve_generator = PseudoHilbert(dimension.x, dimension.y)

    @classmethod
    def from_dimension(cls, dimension: Dimension):
        return cls(dimension.x * dimension.y, dimension)
        
    
    def get_d(self, coordinate: Coordinate) -> int:
        return self.curve_generator.coordinate_to_index[coordinate.x][coordinate.y]
    

    def get_coordinate(self, d: int) -> Coordinate:
        coord = self.curve_generator.index_to_coordinate[d]
        return Coordinate(coord[0], coord[1])
    