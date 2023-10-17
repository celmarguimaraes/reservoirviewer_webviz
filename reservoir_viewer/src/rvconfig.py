from .pixelization import Pixelization
from .property import Property
from .small_multiples import SmallMultiples


class rvconfig:
    def __init__(self, configs):
        self.root = configs[0]
        self.folder2d = configs[1]
        self.chart_type = configs[2]
        self.layout_curve = configs[3]
        self.clust_method = configs[4]
        self.min_clusters = int(configs[5])
        self.max_clusters = int(configs[6])
        self.num_iterations = int(configs[7])
        self.properties = []
        self.save_dir = configs[10]
        self.color_map = configs[11]

        self.properties.append(
            Property(
                configs[8],
                configs[9],
            )
        )

        settingDrawConfigs(self, self.num_iterations, self.max_clusters)


def getStrategies(self):
    for strat in self.strategies:
        print("Estrategia: " + strat.getStrategy())


def getProperties(self):
    for prop in self.properties:
        print("Propriedade: " + prop.getProperty())


def settingDrawConfigs(self, iterations, max_clusters):
    for propIndex, p in enumerate(self.properties):
        clustering = None
        # TODO this.loadStaticMapModels(propName, self.root/self.file2d/self.getNullBlocks, meanType) (parte do iza)
        file_2d_path = self.root + "/" + self.folder2d + "/" + p.getFile2d()
        print(file_2d_path)
        if self.chart_type == "pixelization":
            print("Executing Pixelization")
            pixelization = Pixelization(file_2d_path, self.layout_curve)
            pixelization.generate_image(
                self.save_dir, self.color_map, iterations, max_clusters
            )

        elif self.chart_type == "smallmultiples":
            print("Executing Small Multiples")
            smallMultiples = SmallMultiples(file_2d_path, self.layout_curve)
            smallMultiples.reorder_with_clusters(clustering)
            smallMultiples.draw_small_multiples(propIndex)
        else:
            raise Exception(
                "Visualization type not recognized. Please choose between Pixelization and Smallmultiples"
            )
