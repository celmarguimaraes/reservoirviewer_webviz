from dimension import Dimension
import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
from matplotlib import pyplot as plt
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

    #TEST: This method is not complete. Test purposes only.
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
                #FIX: this does not work if num_of_models is not squared
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
        initial = self.pad_matrix()
        # initial = np.split(initial, self.num_of_models)
        # array = np.array(np.dstack(np.array_split(initial, self.num_of_models)))
            # print(len(initial))
            # array = np.split(initial, self.num_of_models)
            # for elements in array:
                # print(len(elements))

            # exit(0)
        print(len(initial))
        test = np.dstack(np.array_split(initial, self.max_i))
        with open("27.csv", 'w') as file:
            for item in test:
                write = csv.writer(file)
                write.writerows(item)

        try:
            df = pd.read_csv("27.csv")
            plt.imshow(df, cmap='rainbow')
            plt.savefig('test.png')
        except:
            raise Exception("Something went down while generating the image.")


if __name__=="__main__":
    # pixelization = Pixelization("tests_files/arithmetic-mean.csv")
    pixelization = Pixelization("intermediary_file.csv")
    # print(pixelization.draw())
    # print(len(pixelization.draw()[3173]))
    # print(pixelization.pad_matrix())
    pixelization.generate_csv_file()
    # pixelization.pad_array()
    # print(pixelization.draw())
    # print(pixelization.generate_model_matrix())
    # print(pixelization.draw().reshape((9, -3, 9), order='C'))
    # print(pixelization.read_to_list())
    # draw = pixelization.draw()
    # draw = np.array_split(draw, 9)
    # draw = np.dstack(draw)
    # print(np.array(draw))
    # print(np.dstack(np.split(pixelization.draw(), 9)))

