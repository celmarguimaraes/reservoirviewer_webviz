from curve import Curve
from snake_curve import SnakeCurve
import pandas as pd
from pandas import DataFrame

class Pixelization:
    def __init__(self, path:str, curve:Curve) -> None:
        self.path = path
        file = DataFrame(pd.read_csv(path))
        self.max_i:int = pd.to_numeric(file.columns[0])
        self.max_j:int = pd.to_numeric(file.columns[1])
        self.num_of_models:int = pd.to_numeric(file.columns[2])
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

