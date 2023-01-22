from abc import ABC, abstractmethod
from coordinate import Coordinate
from dimension import Dimension


class Curve(ABC):
    def __init__(self, number_of_elements: int, dimension: Dimension):
        self.number_of_elements = number_of_elements
        self.dimension = dimension

    def get_number_of_elements(self) -> int:
        return self.number_of_elements

    def get_dimension(self) -> Dimension:
        return self.dimension

    @abstractmethod
    def get_coordinate(self, d: int) -> Coordinate:
        pass

    @abstractmethod
    def get_d(self, coordinate: Coordinate) -> int:
        pass

    @abstractmethod
    def define_dimension(self, number_of_elements: int) -> Dimension:
        pass
