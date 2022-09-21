from curve import Curve
from coordinate import Coordinate
import pandas as pd
import math
from pandas import DataFrame

class Pixelization:
    def __init__(self, path:str, curve:Curve) -> None:
        self.path = path
        file = DataFrame(pd.read_csv(path))
        self.max_i:int = int(pd.to_numeric(file.columns[0]))
        self.max_j:int = int(pd.to_numeric(file.columns[1]))
        self.num_of_models:int = int(pd.to_numeric(file.columns[2]))
        self.curve:Curve = curve
    
    # Getters
    def get_max_i(self) -> int:
        return self.max_i

    def get_max_j(self) -> int:
        return self.max_j

    def get_num_of_models(self) -> int:
        return self.num_of_models

    def get_curve(self) -> Curve:
        return self.curve

    def get_number_of_elements(self) -> int:
        return self.max_i * self.max_j * self.num_of_models

    def draw(self) -> None:
        subcell:int = math.ceil(math.sqrt(self.num_of_models))
        for i in range(1, self.max_i):
            for j in range(1, self.max_j):
                for x_axis in range(1, subcell):
                    for y_axis in range(1, subcell):
                        print(self.curve.get_d(Coordinate(x_axis, y_axis)))


