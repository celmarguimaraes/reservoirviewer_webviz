import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import math

class Pixelization:
    def __init__(self, path:str) -> None:
        self.path = path
        self.file = DataFrame(pd.read_csv(path))
        self.max_i:int = int(pd.to_numeric(self.file.columns[0]))
        self.max_j:int = int(pd.to_numeric(self.file.columns[1]))
        self.num_of_models:int = int(pd.to_numeric(self.file.columns[2]))
    
    def read_to_list(self) -> list:
        """
        Read a column into a list data structure.

        Iterates through the first column in the .csv file and converts it into a list.

        Return:
            It return a list with numpy floats of 16 bytes.
            
        """

        try:
            column = DataFrame(self.file[self.file.columns[0]]).squeeze().tolist()
            # return [np.float16(item) for item in column][::-1]
            return [np.float16(item) for item in column]
        except:
            raise Exception('Something went wrong when trying to read the file.')

    def generate_model_matrix(self):
        """
        NOTE: Each matrix inside needs to be squared
        Separates the list into sublists of the same model.

        Returns:
            Numpy array of shape (num_of_models, max_i, max_j)
        """
        return np.array(self.read_to_list(), dtype=np.float64).reshape(self.num_of_models, self.max_i, self.max_j)

    def draw(self):
        """
        Draws the pixelization based on the model matrix.

        It reorganizes data into an array following the rules of the Pixelization Visualization technique.
        First, we need to be sure we are dealing with swuared models. If it is not squared, we need to be sure we have the
        same amount of NaN values at the beginning and at the end of the array. After calculating those values we iterate
        through the array, stacking the elements based on the depth (models).

        Returns:
            Numpy array with the elements reorganized.
        """
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
                # list = np.array(list).reshape(shape, shape)[::-1]
                list = np.array(list).reshape(shape, shape)
                result.append(list)

        return np.array(result)

    def pad_matrix(self):
        """
        It adds NaN value around each submatrix to give a space between each one, making it easier to visualize and distinct the submatrices.

        Returns:
            Numpy array with NaN elements on the edges.
        """
        matrix = self.draw()
        padded_array = []
        for element in matrix:
            padded_array.append(np.pad(element, ((1, 1)), 'constant', constant_values=(np.nan)))

        return np.array(padded_array)


    def generate_image(self) -> None:
        """
        It generates and save the image based on the matrix (multidimensional array) received.

        Returns:
            None.
        """
        # array = self.pad_matrix()[::-1]
        array = np.flip(self.pad_matrix(), 0)
        array = np.array(np.dstack(np.array_split(array, self.max_i)))
        array = array.reshape(array.shape[0] * array.shape[1], array.shape[2])

        try:
            plt.figure(figsize=(self.max_j, self.max_i), layout="constrained")
            plt.imshow(np.flip(array, 1), cmap='jet', vmin=0, vmax=1)
            plt.savefig('/home/izael/git/rvweb-python/tests_files/test_file.png')
        except:
            raise Exception("Something went down while generating the image.")


if __name__=="__main__":
    pixelization = Pixelization("/home/izael/git/rvweb-python/tests_files/sw_new_file.csv")
    pixelization.generate_image()

