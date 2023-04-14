import csv
import math
import os
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
from webviz_config.webviz_assets import WEBVIZ_ASSETS
import pathlib
from pathlib import Path
=======

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py
from matplotlib import gridspec


class SmallMultiples:
    def __init__(self, path, curve, generated_img_folder):
        self.generated_img_folder = generated_img_folder
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
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
        self.colorMap = 'jet'
        print("i, j, num of models: ", self.max_i,
              self.max_j, self.num_of_models)
        self.grid = self.read_file(path)
        self.sorting_dict = {}
        self.new_grid_sorting = [m for m in range((self.num_of_models))] # Stores the index of the models to sort them after clustering

=======
        # self.curve: Curve = curve
        self.colorMap = "jet"
        print("i, j, k: ", self.max_i, self.max_j, self.num_of_models)
        self.final_grid = self.read_file(path)
        self.final_dict = {}
        self.new_grid_order = []
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py

    # Getters
    def get_max_i(self) -> int:
        return self.max_i


    def get_max_j(self) -> int:
        return self.max_j


    def get_num_of_models(self) -> int:
        return self.num_of_models

    # def get_curve(self) -> Curve:
    #     return self.curve


    def read_file(self, path):
        file_content = []
        count_line = 0

        with open(path) as csv_file:
            for i in range(1):
                next(csv_file)
            for line in csv_file:
                line.strip()
                if line == "nan" or line == "nan\n":
                    file_content.append(-1)
                else:
                    file_content.append(int(float(line.strip())))
                count_line = count_line + 1

        file_content = np.array(file_content)
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
        grid = file_content.reshape(self.num_of_models, self.max_i*self.max_j) # Reshape the grid to 2 dimensions in order to cluster it

        return grid

=======
        grid = file_content.reshape(self.num_of_models, self.max_i * self.max_j)

        return grid

    def mergeSort(self, alist, cluster_dict):
        if len(alist) > 1:
            mid = len(alist) // 2
            left_half = alist[:mid]
            right_half = alist[mid:]

            self.mergeSort(left_half, cluster_dict)
            self.mergeSort(right_half, cluster_dict)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if cluster_dict[left_half[i]] < cluster_dict[right_half[j]]:
                    alist[k] = left_half[i]
                    i = i + 1
                else:
                    alist[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                alist[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                alist[k] = right_half[j]
                j = j + 1
                k = k + 1
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py

    def reorder_with_clusters(self, clustering):
        clustering.clusterGrid(self.grid)
        cluster_dict = clustering.get_dict()
        
        self.new_grid_sorting = sorted(self.new_grid_sorting, key=cluster_dict.get)
        self.new_grid_sorting = np.array(self.new_grid_sorting)

        self.grid = self.grid[self.new_grid_sorting] # Organize the grid by the new indexes
        self.sorting_dict = {k: cluster_dict[k] for k in self.new_grid_sorting}


    def draw_small_multiples(self, prop_index):
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
        grid = self.grid.reshape(self.num_of_models, self.max_i, self.max_j) # Reshape the grid back to 3 dimensions
        
        fig = plt.figure(figsize=(self.max_i, self.max_j))
        dimension = math.ceil(math.sqrt(self.num_of_models))

        gs = gridspec.GridSpec(dimension, dimension,
                               wspace=0.01, hspace=0.01) # Create grid to each model
=======
        fig = plt.figure(figsize=(self.max_j, self.max_i))
        grid = self.final_grid.reshape(self.num_of_models, self.max_i, self.max_j)
        dimension = math.ceil(math.sqrt(self.num_of_models))

        gs = gridspec.GridSpec(dimension, dimension, wspace=0.01, hspace=0.01)
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py

        count = 0
        for i in range(dimension):
            for j in range(dimension):
                if count < self.num_of_models:
                    ax = plt.subplot(gs[i, j])
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
                    rotated = np.rot90(grid[count], 3, (0, 1)) # Rotate image
                    flipped = np.flip(rotated, 1) # Mirror image 
                    ax.imshow(flipped, cmap='jet',
                              interpolation='none', vmin=0, vmax=256)

                    ax.set_xlim(-10, self.max_i+10) # Add width to image
                    ax.set_ylim(-10, self.max_j+10) # Add height to image
=======
                    ax.imshow(
                        grid[count], cmap="jet", interpolation="none", vmin=0, vmax=256
                    )

                    ax.set_xlim(-10, self.max_j + 10)
                    ax.set_ylim(-10, self.max_i + 10)
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py

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
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
                if (index < self.num_of_models-1):
                    if self.sorting_dict[self.new_grid_sorting[index]] != self.sorting_dict[self.new_grid_sorting[index+1]]: # If right model is from a different cluster
                        ax.spines['right'].set_visible(True)
                        ax.spines['right'].set_linestyle('dashed')
                if (index < self.num_of_models-dimension):
                    if self.sorting_dict[self.new_grid_sorting[index]] != self.sorting_dict[self.new_grid_sorting[index+dimension]]: # If bottom model is from a different cluster
                        ax.spines['bottom'].set_visible(True)
                        ax.spines['bottom'].set_linestyle('dashed')
=======
                if index < self.num_of_models - 1:
                    if (
                            self.final_dict[self.new_grid_order[index]]
                            != self.final_dict[self.new_grid_order[index + 1]]
                    ):
                        ax.spines["right"].set_visible(True)
                        ax.spines["right"].set_linestyle("dashed")
                if index < self.num_of_models - dimension:
                    if (
                            self.final_dict[self.new_grid_order[index]]
                            != self.final_dict[self.new_grid_order[index + dimension]]
                    ):
                        ax.spines["bottom"].set_visible(True)
                        ax.spines["bottom"].set_linestyle("dashed")
>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py

                # Border of the image
                if ax.get_subplotspec().is_first_row():
                    ax.spines["top"].set_visible(True)
                if ax.get_subplotspec().is_last_row():
                    ax.spines["bottom"].set_visible(True)
                if ax.get_subplotspec().is_first_col():
                    ax.spines["left"].set_visible(True)
                if ax.get_subplotspec().is_last_col():
<<<<<<< HEAD:webviz_plugin_boilerplate/plugins/RV/SmallMultiples.py
                    ax.spines['right'].set_visible(True)

        # Saving image
        path = self.generated_img_folder + "//sm"+str(prop_index)+".png"
        print("Path of the generated file: ", path)

=======
                    ax.spines["right"].set_visible(True)

        full_path = os.path.realpath(__file__)
        path = os.path.dirname(full_path) + "//generated//sm" + str(prop_index) + ".png"
        print("Path of the generated file: ", path)

>>>>>>> develop:webviz_plugin_boilerplate/plugins/RV/small_multiples.py
        plt.savefig(path)
