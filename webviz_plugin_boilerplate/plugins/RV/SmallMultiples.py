import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
import math
from webviz_config.webviz_assets import WEBVIZ_ASSETS
import os
from pathlib import Path





class SmallMultiples:
    def __init__(self, path, curve):
        self.path = path
        with open("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//intermediary_file.csv") as csv_file:
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
        self.final_grid = self.read_file("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//intermediary_file.csv")


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
        model = [[[0 for m in range(self.num_of_models)] for j in range(
            self.max_j)] for i in range(self.max_i)]

        with open(path) as csv_file:
            file_content = []
            for i in range(2):
                next(csv_file)
            for line in (csv_file):
                line.replace("\n", "")
                file_content.append(int(line))

        file_content = np.array(file_content)
        grid = file_content.reshape(self.max_i, self.max_j, self.num_of_models)

        fig, ax = plt.subplots(int(math.sqrt(self.num_of_models)), int(math.sqrt(self.num_of_models)))
        
        count = 0
        for x in range(int(math.sqrt(self.num_of_models))):
            for y in range(int(math.sqrt(self.num_of_models))):
                ax[x, y].imshow(grid[count], cmap='jet', interpolation='none', vmin=0, vmax=10)
                # ax[x, y].grid(grid[count])
                # plt.colorbar()
                count = count + 1 
        
        
            
        plt.savefig("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//generated//teste.png")

            
        image = Path(
            "C:/Users/k/Documents/Unicamp/IC/rv_webviz_celmar/reservoirviewer_webviz/webviz_plugin_boilerplate/plugins/RV/generated/teste.png")

        self.image_url = WEBVIZ_ASSETS.add(image)
        return grid 


    # def draw_image(self, grid, x,y, count):

        # ax[x, y].plot(grid)
        # # plt.imshow(grid, cmap='jet', interpolation='none', vmin=0, vmax=10)
        # plt.colorbar()
        # plt.savefig("C://Users//k//Documents//Unicamp//IC//rv_webviz_celmar//reservoirviewer_webviz//webviz_plugin_boilerplate//plugins//RV//generated//teste.png")
