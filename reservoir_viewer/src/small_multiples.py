import csv
import math
import os
import warnings

import matplotlib.pyplot as plt
from matplotlib import cm, colors
import numpy as np
import pandas as pd
from matplotlib import gridspec
from pandas import DataFrame
from .clusterization.xmeans_clustering import XmeansClusterization

from reservoir_viewer.src.parser.parse_prop_files import parse_file
np.warnings = warnings


class SmallMultiples:
    def __init__(self, path, properties):
        self.path = path
        self.file = parse_file(path, properties)
        self.max_i: int = int(self.file.iloc[-1, 0])
        self.max_j: int = int(self.file.iloc[-1, 1])
        self.num_of_models: int = int(self.file.iloc[-1, 2])
        # self.curve: Curve = curve

    def get_min_max_values(self, grid):
        return np.nanmin(grid), np.nanmax(grid)

    def read_file(self):
        column = DataFrame(self.file[self.file.columns[3]]).squeeze().tolist()
        return [np.float16(item) for item in column]

    def generate_model_matrix(self):
        return np.array(self.read_file(), dtype=np.float16).reshape(
            self.num_of_models, self.max_i, self.max_j
        )

    def get_clusters(self, matrix, max_clusters):
        xmeans_instance = XmeansClusterization(matrix, max_clusters)
        return xmeans_instance.cluster_models()

    def reorder_with_clusters(self, matrix, max_clusters):
        reordered_matrix = []
        clusters = self.get_clusters(matrix, max_clusters)
        for cluster in clusters:
            reordered_matrix.append(matrix[cluster])

        return reordered_matrix

    def draw_small_multiples(self, save_dir, color_map, max_clusters):
        fig = plt.figure(figsize=(self.max_j, self.max_i))
        grid = self.generate_model_matrix()
        limit_values = self.get_min_max_values(grid)
        grid_final = self.reorder_with_clusters(grid, max_clusters)
        dimension = math.ceil(math.sqrt(self.num_of_models))

        gs = gridspec.GridSpec(dimension, dimension, wspace=0.01, hspace=0.01)

        count = 0
        for i in range(dimension):
            for j in range(dimension):
                if count < self.num_of_models:
                    ax = plt.subplot(gs[i, j])
                    ax.imshow(
                        grid_final[count],
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

        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cmap = plt.get_cmap(color_map)
        norm = colors.Normalize(vmin=limit_values[0], vmax=limit_values[1])
        fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
        plt.savefig(save_dir)
