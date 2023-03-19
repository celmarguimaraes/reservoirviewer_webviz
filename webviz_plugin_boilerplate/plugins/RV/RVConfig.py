import re
from .Strategy import Strategy
from .Property import Property
from .WellList import WellList
from .SmallMultiples import SmallMultiples
from .pixelization import Pixelization
from .Clustering import Clustering


class Configuration:
    def __init__(self, configs):
        self.root = configs[0]
        self.benchmark = configs[1]
        self.folder2d = configs[2]
        self.folder_Dist_Matr = configs[3]
        self.chart_type = configs[4]
        self.layout_curve = configs[5]
        self.clust_method = configs[6]
        self.dist_matrix = configs[7]
        self.min_clusters = int(configs[8])
        self.max_clusters = int(configs[9])
        self.num_iterations = int(configs[10])
        self.all_models = configs[19]
        self.hl_models = configs[20]
        self.properties = []
        self.strategies = []
        self.save_dir = configs[21]

        self.properties.append(
            Property(
                configs[11],
                configs[12],
                configs[13],
                configs[14],
                configs[15],
                configs[16],
            )
        )
        self.strategies.append(Strategy(configs[17], configs[18]))

        settingDrawConfigs(self)


def getStrategies(self):
    for strat in self.strategies:
        print("Estrategia: " + strat.getStrategy())


def getProperties(self):
    for prop in self.properties:
        print("Propriedade: " + prop.getProperty())


# def createWellList(self):
#     estrategias = []

#     if (~(self.strategies.empty())):
#         for strategy in self.strategies:
#             name = strategy.getName()
#             path = strategy.getPath()
#             wellList = WellList(name)
#             estrategias.append(wellList)
#             estrategias[i].loadFile(path)

#     return estrategias


def settingDrawConfigs(self):
    for propIndex, p in enumerate(self.properties):
        print("Pegando Propriedade")
        clustering = None
        # TODO this.loadStaticMapModels(propName, self.root/self.file2d/self.getNullBlocks, meanType) (parte do iza)
        file_2d_path = self.root + "/" + self.folder2d + "/" + p.getFile2d()
        print(file_2d_path)
        if self.chart_type == "pixelization":
            print("Executing Pixelization")
            pixelization = Pixelization(file_2d_path, self.layout_curve)
            print("Look we got here somehow")
            pixelization.generate_image(self.save_dir)

        elif self.chart_type == "smallmultiples":
            print("Executing Small Multiples")
            smallMultiples = SmallMultiples(file_2d_path, self.layout_curve)
            smallMultiples.reorder_with_clusters(clustering)
            smallMultiples.draw_small_multiples(propIndex)
        else:
            raise Exception(
                "Tipo de desenho não reconhecido, favor escolher entre Pixelization e Smallmultiples"
            )
