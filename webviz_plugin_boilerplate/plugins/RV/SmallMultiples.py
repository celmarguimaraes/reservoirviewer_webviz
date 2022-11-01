import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
import math
from webviz_config.webviz_assets import WEBVIZ_ASSETS
from pathlib import Path
from matplotlib import gridspec


class SmallMultiples:
    def __init__(self, path, curve):
        self.path = path
        with open("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//generated//intermediary_file.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lineCount = 0
            for row in csv_reader:
                if lineCount == 0:
                    self.max_i: int = pd.to_numeric(row[0])
                    self.max_j: int = pd.to_numeric(row[1])
                    self.num_of_models: int = pd.to_numeric(row[2])
                lineCount = lineCount + 1
        # self.curve: Curve = curve
        self.colorMap = 'jet'
        print("i, j, k: ", self.max_i, self.max_j, self.num_of_models)
        self.final_grid = self.read_file(
            "C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//intermediary_file.csv")
        self.final_dict = {}
        self.newGridOrder = []

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
        path = "C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//generated//intermediary_file.csv"
        file_content = []
        countLine = 0

        with open(path) as csv_file:
            for i in range(2):
                next(csv_file)
            for line in (csv_file):
                line.strip()
                if (line == "nan" or line == "nan\n"):
                    file_content.append(-1)
                else:
                    file_content.append(int(float(line.strip())))
                countLine = countLine + 1

        print("Reservoir lines in intermediary file: ", countLine)
        file_content = np.array(file_content)
        grid = file_content.reshape(self.num_of_models, self.max_i*self.max_j)

        return grid

    def mergeSort(self, alist, clusterDict):
        if len(alist) > 1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergeSort(lefthalf, clusterDict)
            self.mergeSort(righthalf, clusterDict)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if clusterDict[lefthalf[i]] < clusterDict[righthalf[j]]:
                    alist[k] = lefthalf[i]
                    i = i+1
                else:
                    alist[k] = righthalf[j]
                    j = j+1
                k = k+1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i+1
                k = k+1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j+1
                k = k+1

    def reorder_with_clusters(self, clustering):
        clustering.clusterGrid(self.final_grid)
        self.newGridOrder = [m for m in range((self.num_of_models))]
        clusterDict = clustering.get_dict()
        self.mergeSort(self.newGridOrder, clusterDict)
        self.newGridOrder = np.array(self.newGridOrder)

        self.final_grid = self.final_grid[self.newGridOrder]
        self.final_dict = {k: clusterDict[k] for k in self.newGridOrder}

    def draw_small_multiples(self, prop_index):
        fig = plt.figure(figsize=(self.max_j, self.max_i))
        grid = self.final_grid.reshape(
            self.num_of_models, self.max_i, self.max_j)
        dimension = math.ceil(math.sqrt(self.num_of_models))

        gs = gridspec.GridSpec(dimension, dimension,
                               wspace=0.01, hspace=0.01)

        count = 0
        for i in range(dimension):
            for j in range(dimension):
                if (count < self.num_of_models):
                    ax = plt.subplot(gs[i, j])
                    ax.imshow(grid[count], cmap='jet',
                              interpolation='none', vmin=0, vmax=256)

                    ax.set_xlim(-10, self.max_j+10)
                    ax.set_ylim(-10, self.max_i+10)

                    ax.set_xticks([])
                    ax.set_yticks([])
                    fig.add_subplot(ax)
                    count = count + 1
                else:
                    break

        all_axes = fig.get_axes()

        # show only the outside spines
        for index, ax in enumerate(all_axes):
            for sp in ax.spines.values():
                sp.set_visible(False)
                if (index < self.num_of_models-1):
                    if self.final_dict[self.newGridOrder[index]] != self.final_dict[self.newGridOrder[index+1]]:
                        ax.spines['right'].set_visible(True)
                if (index < self.num_of_models-dimension):
                    if self.final_dict[self.newGridOrder[index]] != self.final_dict[self.newGridOrder[index+dimension]]:
                        ax.spines['bottom'].set_visible(True)

                if ax.get_subplotspec().is_first_row():
                    ax.spines['top'].set_visible(True)
                if ax.get_subplotspec().is_last_row():
                    ax.spines['bottom'].set_visible(True)
                if ax.get_subplotspec().is_first_col():
                    ax.spines['left'].set_visible(True)
                if ax.get_subplotspec().is_last_col():
                    ax.spines['right'].set_visible(True)

        plt.savefig("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//generated//sm"+str(prop_index)+".png")
