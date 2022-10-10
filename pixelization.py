from curve import Curve
from snake_curve import SnakeCurve
from dimension import Dimension
from coordinate import Coordinate
import pandas as pd
import numpy as np
import math
from pandas import DataFrame

class Pixelization:
    def __init__(self, path:str, curve:Curve) -> None:
        self.path = path
        self.file = DataFrame(pd.read_csv(path))
        self.max_i:int = int(pd.to_numeric(self.file.columns[0]))
        self.max_j:int = int(pd.to_numeric(self.file.columns[1]))
        self.num_of_models:int = int(pd.to_numeric(self.file.columns[2]))
        self.curve:Curve = curve
    
    def read_to_list(self) -> list:
        try:
            column = DataFrame(self.file[self.file.columns[0]]).squeeze().tolist()[1:]
            return [float(item) for item in column]
        except:
            raise Exception('Something went wrong when trying to read the file.')

    def generate_matrix(self):
        #NOTE: Each matrix inside needs to be squared
        return np.array(self.read_to_list()).reshape(self.num_of_models, 9, 3)

    #TEST: This method is not complete. Test purposes only.
    def draw(self) -> None:
        matrix = self.generate_matrix()
        for i in range(self.max_i):
            for j in range(self.max_j):
                for m in range(self.num_of_models):
                    valor = matrix[m][i][j]
                    print(valor, " ")
                print("\n")
            print("\n")

if __name__=="__main__":
    pixelization = Pixelization("intermediary_file.csv", SnakeCurve(27, Dimension(9, 3)))
    # print(pixelization.draw())
    print(pixelization.generate_matrix())
    pixelization.draw()

