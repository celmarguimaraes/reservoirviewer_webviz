from curve import Curve
from snake_curve import SnakeCurve
from dimension import Dimension
import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
from matplotlib import pyplot as plt

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

    # Separate each model in a matrix for itself
    def generate_model_matrix(self):
        #NOTE: Each matrix inside needs to be squared
        return np.array(self.read_to_list()).reshape(self.num_of_models, self.max_i, self.max_j)

    #TEST: This method is not complete. Test purposes only.
    def draw(self):
        matrix = self.generate_model_matrix()
        result = []
        for i in range(self.max_i):
            for j in range(self.max_j):
                list = []
                for m in range(self.num_of_models):
                    valor = matrix[m][i][j]
                    list.append(valor)
                list = np.array(list).reshape(3, 3)
                result.append(list)

        return np.array(result)

    def generate_csv_file(self) -> None:
        array = self.draw()
        array = np.array(np.dstack(np.array_split(array, self.num_of_models)))
        with open("test.csv", 'w') as file:
            for item in array:
                write = csv.writer(file, delimiter=',')
                write.writerows(item)

        try:
            df = pd.read_csv("test.csv", header=None)
        except:
            raise Exception("Something went down while reading the .csv file.")

        try:
            plt.imshow(df, cmap='jet', interpolation='nearest', vmin=0, vmax=10)
            plt.savefig('test.png')
        except:
            raise Exception("Something went down while generating the image.")


if __name__=="__main__":
    pixelization = Pixelization("intermediary_file.csv", SnakeCurve(27, Dimension(9, 3)))
    pixelization.generate_csv_file()
    # pixelization.pad_array()
    # print(pixelization.generate_model_matrix()[0])
    # print(pixelization.draw().reshape((9, -3, 9), order='C'))
    # print(pixelization.read_to_list())
    # draw = pixelization.draw()
    # draw = np.array_split(draw, 9)
    # draw = np.dstack(draw)
    # print(np.array(draw))


