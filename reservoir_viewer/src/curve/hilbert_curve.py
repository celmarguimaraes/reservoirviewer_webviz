from hilbertcurve.hilbertcurve import HilbertCurve as HC
from typing import List
from math import log2
import math

from .curve import Curve
from .curve_utils.coordinate import Coordinate
from .curve_utils.dimension import Dimension


class HilbertCurve(Curve):
    curve_generator: HC

    def __init__(self, num_of_elements: int, dimension: Dimension) -> None:
        if dimension.x != dimension.y:
            raise ValueError('A altura e largura devem iguais.')
        if not self.is_power_of_2(dimension.x) or not self.is_power_of_2(dimension.y):
            raise ValueError('Altura e largura devem ser potência de 2.')
        if num_of_elements > dimension.x * dimension.y:
            raise ValueError('Número de elementos não pode ser maior que a quantidade de coordenadas disponíveis na dimensão.')

        super().__init__(num_of_elements, dimension)
        self.curve_generator = HC(p=log2(dimension.x), n=2)

    @classmethod
    def from_dimension(cls, dimension: Dimension):
        return cls(dimension.x * dimension.y, dimension)

    def is_power_of_2(self, number: int):
        return log2(number) - int(log2(number)) == 0
    

    def get_d(self, coordinate: Coordinate) -> int:
        return self.curve_generator.distance_from_point([coordinate.x, coordinate.y])


    def get_coordinate(self, d: int) -> Coordinate:
        coord = self.curve_generator.point_from_distance(d)
        return Coordinate(coord[0], coord[1])
    