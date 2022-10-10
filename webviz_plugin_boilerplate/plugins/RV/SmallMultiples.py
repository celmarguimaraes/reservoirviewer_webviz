import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import csv

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
        model = [[[0 for m in range(self.num_of_models)] for j in range(self.max_j)] for i in range(self.max_i)]
        
        with open(self.path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            
            for m in range(self.num_of_models):
                for i in range(self.max_i):
                    for j in range(self.max_j):
                        model[i][j][m] = row[0]
                        print(f'Processed {line_count} lines.')
                

        for m in range(self.num_of_models):
            draw_image(m)

    def draw_image(self, grid):
        plt.imshow(grif, cmap='jet', interpolation='none', vmin=0, vmax=255)
        plt.colorbar()
        plt.savefig("teste.png")
