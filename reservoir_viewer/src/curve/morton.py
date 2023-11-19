import math
from .curve import Curve
from .curve_utils.dimension import Dimension
from .curve_utils.coordinate import Coordinate
from zCurve import zCurve
from math import log2
from typing import List

class MortonCurve(Curve):
    '''
    Cuva de Morton também conhecida como curva Z. Possui o seguinte layout
    _____    ____
        /   /    /
      /    /   /
    /____/   /___
                /
     -----------                
    /____    ____
        /   /    /
      /    /   /
    /____/   /___
             
           
    '''
    map_d_to_xy: List[Coordinate]
    map_xy_to_d: List[List[int]]

    def __init__(self, num_of_elements: int, dimension: Dimension) -> None:
        if not self.is_power_of_2(dimension.x) or not self.is_power_of_2(dimension.y):
            raise ValueError('Altura e largura devem ser potência de 2')
        if num_of_elements > dimension.x * dimension.y:
            raise ValueError('Número de elementos não pode ser maior que a quantidade de coordenadas disponíveis na dimensão.')
        
        super().__init__(num_of_elements, dimension)
        self.map_xy_to_d = [[None for _ in range(self.dimension.x)] for _ in range(self.dimension.y)]
        self.map_d_to_xy = [None for _ in range(self.number_of_elements)]
        self.fill_map()

    @classmethod
    def from_dimension(cls, dimension: Dimension):
        return cls(dimension.x * dimension.y, dimension)
    

    def is_power_of_2(self, number: int):
        return log2(number) - int(log2(number)) == 0


    def get_number_of_bits(self, number: int):
        binary_number = bin(number)
        num_of_bits = len(binary_number) - 2
        return num_of_bits

    def fill_map(self):
        max_len = self.get_number_of_bits(self.number_of_elements - 1)
        for i in range(self.number_of_elements):
            coord = zCurve.deinterlace(i, dims=2, total_bits=max_len)
            self.map_d_to_xy[i] = Coordinate(coord[0], coord[1])
            self.map_xy_to_d[coord[0]][coord[1]] = i


    def get_d(self, coordinate: Coordinate) -> int:
        return self.map_xy_to_d[coordinate.get_x()][coordinate.get_y()]
        

    def get_coordinate(self, d: int) -> Coordinate:
        return self.map_d_to_xy[d]
