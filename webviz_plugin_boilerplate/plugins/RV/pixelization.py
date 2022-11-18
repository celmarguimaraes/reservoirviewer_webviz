# from dimension import Dimension
import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

class Pixelization:
    def __init__(self, path:str) -> None:
        self.path = path
        #NOTE: This is throwing a warning because the column is read as data
        self.file = DataFrame(pd.read_csv(path))
        self.max_i:int = int(pd.to_numeric(self.file.columns[0]))
        self.max_j:int = int(pd.to_numeric(self.file.columns[1]))
        self.num_of_models:int = int(pd.to_numeric(self.file.columns[2]))
    
    def read_to_list(self) -> list:
        try:
            column = DataFrame(self.file[self.file.columns[0]]).squeeze().tolist()
            return [np.float64(item) for item in column]
        except:
            raise Exception('Something went wrong when trying to read the file.')

    # Separate each model in a matrix for itself
    def generate_model_matrix(self):
        #NOTE: Each matrix inside needs to be squared
        return np.array(self.read_to_list(), dtype=np.float64).reshape(self.num_of_models, self.max_i, self.max_j)

    def draw(self):
        shape:int = math.ceil(math.sqrt(self.num_of_models))
        prev = math.ceil(((shape ** 2) - self.num_of_models) / 2)
        next = math.floor(((shape ** 2) - self.num_of_models) / 2)
        matrix = self.generate_model_matrix()
        result = []
        for i in range(self.max_i):
            for j in range(self.max_j):
                list = [] #NOTE: Com base nesse vetor eu vou usar a curva.
                for m in range(self.num_of_models):
                    valor = matrix[m][i][j]
                    list.append(valor)
                list = np.pad(list, ((prev, next)), 'constant', constant_values=(np.nan))
                list = np.array(list).reshape(shape, shape)
                result.append(list)

        return np.array(result)

    def pad_matrix(self):
        matrix = self.draw()
        padded_array = []
        for element in matrix:
            padded_array.append(np.pad(element, ((1, 1)), 'constant', constant_values=(np.nan)))

        return np.array(padded_array)


    def generate_csv_file(self) -> None:
        array = self.pad_matrix()
        array = np.array(np.dstack(np.array_split(array, self.max_i)))
        array = array.reshape(array.shape[0] * array.shape[1], array.shape[2])
        print(f'Shape of the array: {array.shape}')
        print("Original array")
        print(array)
        print("Inverted array")
        print(array[::-1])

        try:
            plt.figure(figsize=(self.max_j, self.max_i), layout="constrained")
            plt.imshow(array[::-1], cmap='jet', vmin=0, vmax=256)
            plt.savefig('/home/izael/git/rvweb-python/tests_files/test_file.png')
        except:
            raise Exception("Something went down while generating the image.")


if __name__=="__main__":
    pixelization = Pixelization("/home/izael/git/rvweb-python/tests_files/intermediary_file.csv")
    pixelization.generate_csv_file()

