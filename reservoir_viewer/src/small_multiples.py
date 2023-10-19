import csv
import math
import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import gridspec
from pandas import DataFrame
from .clusterization.xmeans_clustering import XmeansClusterization

np.warnings = warnings


class SmallMultiples:
    def __init__(self, path):
        self.path = path
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            lineCount = 0
            for row in csv_reader:
                if lineCount == 0:
                    self.max_i: int = pd.to_numeric(row[0])
                    self.max_j: int = pd.to_numeric(row[1])
                    self.num_of_models: int = pd.to_numeric(row[2])
                lineCount = lineCount + 1
        # self.curve: Curve = curve
        self.final_grid = self.read_file(path)

    def get_min_max_values(self):
        linearized = np.array(self.final_grid).reshape(
            self.num_of_models * self.max_i * self.max_j
        )
        return np.nanmin(linearized), np.nanmax(linearized)

    def read_file(self, path):
        df = DataFrame(pd.read_csv(path))
        column = DataFrame(df[df.columns[0]]).squeeze().tolist()
        column_list = [np.float16(item) for item in column]
        return np.array(column_list, dtype=np.float16).reshape(
            self.num_of_models, self.max_i, self.max_j
        )

    def get_clusters(self, matrix, iterations, max_clusters):
        xmeans_instance = XmeansClusterization(matrix, iterations, max_clusters)
        return xmeans_instance.cluster_models()

    def reorder_with_clusters(self, matrix, iterations, max_clusters):
        reordered_matrix = []
        clusters = self.get_clusters(matrix, iterations, max_clusters)
        for cluster in clusters:
            reordered_matrix.append(matrix[cluster])

        return reordered_matrix

    def draw_small_multiples(self, save_dir, color_map, iterations, max_clusters):
        fig = plt.figure(figsize=(self.max_j, self.max_i))
        grid = self.reorder_with_clusters(self.final_grid, iterations, max_clusters)
        dimension = math.ceil(math.sqrt(self.num_of_models))
        limit_values = self.get_min_max_values()

        gs = gridspec.GridSpec(dimension, dimension, wspace=0.01, hspace=0.01)

        count = 0
        for i in range(dimension):
            for j in range(dimension):
                if count < self.num_of_models:
                    ax = plt.subplot(gs[i, j])
                    ax.imshow(
                        grid[count],
                        cmap=color_map,
                        interpolation="none",
                        vmin=limit_values[0],
                        vmax=limit_values[1],
                    )

                    ax.set_xlim(-10, self.max_j + 10)
                    ax.set_ylim(-10, self.max_i + 10)

                    ax.set_xticks([])
                    ax.set_yticks([])
                    fig.add_subplot(ax)
                    count = count + 1
                else:
                    break

        plt.savefig(save_dir)
