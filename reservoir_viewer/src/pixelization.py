import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from pandas import DataFrame
from matplotlib import cm, colors

from reservoir_viewer.src.parser.parse_prop_files import parse_file

from .curve import Curve
from .dimension import Dimension
from .snake_curve import SnakeCurve
from .clusterization.xmeans_clustering import XmeansClusterization

np.warnings = warnings


class Pixelization:
    def __init__(self, path: str, curve: str, properties: str) -> None:
        self.path = path
        self.file = parse_file(path, properties)
        self.max_i: int = int(self.file.iloc[-1, 0])
        self.max_j: int = int(self.file.iloc[-1, 1])
        self.num_of_models: int = int(self.file.iloc[-1, 2])
        self.curve: str = curve

    def set_curve(
        self, curve_name: str, number_of_elements: int, dimension: Dimension
    ) -> Curve:
        match curve_name:
            case "snake curve":
                return SnakeCurve(number_of_elements, dimension)
            case _:
                raise Exception("This curve does not exist")

    def read_to_list(self) -> list:
        """
        Read a column into a list data structure.

        Iterates through the first column in the .csv file and converts it into a list.

        Return:
            It return a list with numpy floats of 16 bytes.

        """

        try:
            column = DataFrame(self.file[self.file.columns[3]]).squeeze().tolist()
            # return [np.float16(item) for item in column][::-1]
            return [np.float16(item) for item in column]
        except:
            raise Exception("Something went wrong when trying to read the file.")

    def generate_model_matrix(self):
        """
        NOTE: Each matrix inside needs to be squared
        Separates the list into sublists of the same model.

        Returns:
            Numpy array of shape (num_of_models, max_i, max_j)
        """
        return np.array(self.read_to_list(), dtype=np.float16).reshape(
            self.num_of_models, self.max_i, self.max_j
        )

    def draw(self, max_clusters):
        """
        Draws the pixelization based on the model matrix.

        It reorganizes data into an array following the rules of the Pixelization Visualization technique.
        First, we need to be sure we are dealing with squared models. If it is not squared, we need to be sure we have the
        same amount of NaN values at the beginning and at the end of the array. After calculating those values we iterate
        through the array, stacking the elements based on the depth (models).

        Returns:
            Numpy array with the elements reorganized.
        """
        shape: int = math.ceil(math.sqrt(self.num_of_models))
        prev_value = math.ceil(((shape**2) - self.num_of_models) / 2)
        next_value = math.floor(((shape**2) - self.num_of_models) / 2)
        matrix = self.reorder_matrix_based_on_cluster(
            self.generate_model_matrix(), max_clusters
        )
        dimension = Dimension(shape, shape)
        curve = self.set_curve(self.curve, shape * shape, dimension)

        result = []
        for i in range(self.max_i):
            for j in range(self.max_j):
                list_of_values = []
                for m in range(self.num_of_models):
                    valor = matrix[m][i][j]
                    list_of_values.append(valor)
                list_of_values = np.pad(
                    list_of_values,
                    (prev_value, next_value),
                    "constant",
                    constant_values=np.nan,
                )
                list_of_values = np.array(list_of_values).reshape(shape, shape)
                # Flip every row with odd index - Snake Curve
                list_of_values = curve.parse_matrix(list_of_values)
                result.append(list_of_values)

        return np.array(result)

    def pad_matrix(self, max_clusters):
        """
        It adds NaN value around each submatrix to give a space between each one, making it easier to visualize and distinct the submatrices.

        Returns:
            Numpy array with NaN elements on the edges.
        """
        matrix = self.draw(max_clusters)
        padded_array = list()
        for element in matrix:
            padded_array.append(
                np.pad(element, (1, 1), "constant", constant_values=np.nan)
            )

        return np.array(padded_array)

    def get_min_and_max(self):
        list_of_values = self.read_to_list()
        return np.nanmin(list_of_values), np.nanmax(list_of_values)

    def generate_image(self, path: str, color_map: str, max_clusters) -> None:
        """
        It generates and save the image based on the matrix (multidimensional array) received.

        Returns:
            None.
        """
        array = np.flip(self.pad_matrix(max_clusters), 0)
        array = np.array(np.dstack(np.array_split(array, self.max_i)))
        array = array.reshape(array.shape[0] * array.shape[1], array.shape[2])
        values = self.get_min_and_max()

        try:
            plt.figure(
                figsize=(self.max_i * 0.3, self.max_j * 0.3),
                layout="constrained",
                dpi=500,
            )
            cmap = plt.get_cmap(color_map)
            norm = colors.Normalize(vmin=values[0], vmax=values[1])
            plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), shrink=0.5)
            plt.imshow(
                np.flip(array, 1), cmap=color_map, vmin=values[0], vmax=values[1]
            )
            plt.axis("off")
            plt.savefig(path)
        except:
            raise Exception("Something went down while generating the image.")

    def get_clusters(self, matrix, max_clusters):
        xmeans_instance = XmeansClusterization(matrix, max_clusters)
        return xmeans_instance.cluster_models()

    def reorder_matrix_based_on_cluster(self, matrix, max_clusters):
        reordered_matrix = []
        clusters = self.get_clusters(matrix, max_clusters)
        for cluster in clusters:
            reordered_matrix.append(matrix[cluster])

        return reordered_matrix
