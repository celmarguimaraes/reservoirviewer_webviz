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

from .curve.curve_utils.dimension import Dimension
from .curve.pseudo_hilbert_curve import PseudoHilbertCurve
from .curve.hilbert_curve import HilbertCurve
from .curve.zhang_curve.zhang_curve import ZhangCurve
from .curve.snake_curve import SnakeCurve
from .curve.morton import MortonCurve
from .curve.curve_utils.dimension import Dimension
from .curve.curve_utils.coordinate import Coordinate

np.warnings = warnings


class SmallMultiples:
    def __init__(self, path, curve, properties):
        self.path = path
        self.file = parse_file(path, properties)
        self.max_i: int = int(self.file.iloc[-1, 0])
        self.max_j: int = int(self.file.iloc[-1, 1])
        self.num_of_models: int = int(self.file.iloc[-1, 2])
        self.curve: str = curve

    def set_curve(self, curve_name: int, dimension: Dimension):
        match curve_name:
            case "snake curve":
                return SnakeCurve(self.num_of_models, dimension)
            case "hilbert curve":
                return HilbertCurve(self.num_of_models, dimension)
            case "pseudo-hilbert curve":
                return PseudoHilbertCurve(self.num_of_models, dimension)
            case "morton curve":
                return MortonCurve(self.num_of_models, dimension)
            case "zhang curve":
                return ZhangCurve(self.num_of_models, dimension)
            case _:
                raise Exception("This curve does not exist")

    def get_min_max_values(self, grid):
        return np.nanmin(grid), np.nanmax(grid)

    def read_file(self):
        column = DataFrame(self.file[self.file.columns[3]]).squeeze().tolist()
        return [np.float16(item) for item in column]

    def generate_model_matrix(self):
        return np.array(self.read_file(), dtype=np.float16).reshape(
            self.num_of_models, self.max_i, self.max_j
        )

    def get_clusters(self, matrix, max_clusters, min, max):
        xmeans_instance = XmeansClusterization(matrix, max_clusters, min, max)
        return xmeans_instance.cluster_models()

    def reorder_with_clusters(self, matrix, clusters):
        reordered_matrix = []
        for cluster in clusters:
            reordered_matrix.append(matrix[cluster])

        return reordered_matrix

    def get_clusters_linearized(self, clusters):
        clusters_linearized = []
        for cluster in clusters:
            clusters_linearized = clusters_linearized + cluster

        return clusters_linearized

    def get_clusters_dict(self, linearized, clusters):
        linearized_dict = {}
        for i in range(len(linearized)):
            for j in range(len(clusters)):
                if linearized[i] in clusters[j]:
                    linearized_dict[linearized[i]] = j

        return linearized_dict

    def draw_small_multiples(self, save_dir, color_map, max_clusters):
        fig = plt.figure(figsize=(self.max_i, self.max_j))
        grid = self.generate_model_matrix()
        limit_values = self.get_min_max_values(grid)
        clusters = self.get_clusters(
            grid, max_clusters, limit_values[0], limit_values[1]
        )
        linearized_clusters = self.get_clusters_linearized(clusters)
        clusters_dict = self.get_clusters_dict(linearized_clusters, clusters)
        grid_final = self.reorder_with_clusters(grid, linearized_clusters)
        shape = math.ceil(math.sqrt(self.num_of_models))
        dimension = Dimension(shape, shape)
        curve = self.set_curve(self.curve, dimension)

        gs = gridspec.GridSpec(shape, shape, wspace=0.2, hspace=0.01)

        count = 0
        for i in range(shape):
            for j in range(shape):
                if count < self.num_of_models:
                    ax = plt.subplot(gs[i, j])
                    model = curve.get_d(Coordinate(i, j))
                    rotated = np.rot90(grid_final[model], 3, (0, 1))  # Rotate image
                    flipped = np.flip(rotated, 1)  # Mirror image
                    ax.imshow(
                        flipped,
                        cmap=color_map,
                        interpolation="none",
                        vmin=limit_values[0],
                        vmax=limit_values[1],
                    )

                    ax.set_xlim(-5, self.max_i + 5)
                    ax.set_ylim(-5, self.max_j + 5)

                    ax.set_xticks([])
                    ax.set_yticks([])
                    fig.add_subplot(ax)
                    count = count + 1
                else:
                    break

        all_axes = fig.get_axes()

        # Delimit the clusters
        for index, ax in enumerate(all_axes):
            for sp in ax.spines.values():
                sp.set_visible(False)
                if index < self.num_of_models - 1:
                    if (
                        clusters_dict[linearized_clusters[index]]
                        != clusters_dict[linearized_clusters[index + 1]]
                    ):  # If right model is from a different cluster
                        ax.spines["right"].set_visible(True)
                        ax.spines["right"].set_linestyle("dashed")
                if index < self.num_of_models - shape:
                    if (
                        clusters_dict[linearized_clusters[index]]
                        != clusters_dict[linearized_clusters[index + shape]]
                    ):  # If bottom model is from a different cluster
                        ax.spines["bottom"].set_visible(True)
                        ax.spines["bottom"].set_linestyle("dashed")

                # Border of the image
                if ax.get_subplotspec().is_first_row():
                    ax.spines["top"].set_visible(True)
                if ax.get_subplotspec().is_last_row():
                    ax.spines["bottom"].set_visible(True)
                if ax.get_subplotspec().is_first_col():
                    ax.spines["left"].set_visible(True)
                if ax.get_subplotspec().is_last_col():
                    ax.spines["right"].set_visible(True)

        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cmap = plt.get_cmap(color_map)
        norm = colors.Normalize(vmin=limit_values[0], vmax=limit_values[1])
        fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
        plt.savefig(save_dir)
