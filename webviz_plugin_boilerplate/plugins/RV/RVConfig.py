import re
from .Strategy import Strategy
from .Property import Property
from .WellList import WellList
from .SmallMultiples import SmallMultiples
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

        self.properties.append(Property(configs[11], configs[12], configs[13], configs[14], configs[15], configs[16]))
        self.strategies.append(Strategy(configs[17],configs[18]))

        settingDrawConfigs(self, self.strategies)


def getStrategies(self):
    for strat in self.strategies:
        print("Estrategia: "+strat.getStrategy())


def getProperties(self):
    for prop in self.properties:
        print("Propriedade: "+prop.getProperty())
        

def createWellList(self):
    estrategias = []

    if (~(self.strategies.empty())):
        for strategy in self.strategies:
            name = strategy.getName()
            path = strategy.getPath()
            wellList = WellList(name)
            estrategias.push_back(wellList)
            estrategias[i].loadFile(path)

    return estrategias


def settingDrawConfigs(self, estrategias):
    for propIndex, p in enumerate(self.properties):
        print("pegando propriedade")
        meanType = p.convertMeanType()
        clustering = None
        # TODO this.loadStaticMapModels(propName, self.root/self.file2d/self.getNullBlocks, meanType) (parte do iza)
        if (self.dist_matrix == "MODELS3D_ALL_PROP" or self.dist_matrix == "MODELS3D_PROP"):
            print("Distance Matrix: Feature Vectors")

            # TODO FAZER FILE WRITER
            dist_matrixPath = self.root + "/" + self.folder_Dist_Matr + "/" + self.dist_matrix
            clustering = Clustering(self.clust_method, self.dist_matrix, self.min_clusters, self.max_clusters, self.num_iterations)

        elif (self.dist_matrix == "FEATVECTORS_PROP"):
            print("Distance Matrix: Feature Vectors")

            # TODO FAZER FILE WRITER

            # TODO featureVecFile = self.clusteringConfig.createReservoirFeatureVecMatrix()
            # TODO Clustering clusteringData = self.clusterConfig.clusterReservoirsFeatMatrix(featureVecFile)
            # TODO self.clusterConfig.reorderReservoirByClusters(clusteringData)

        if (self.chart_type == "pixelization"):
            print('Executing Pixelization')
        elif (self.chart_type == "smallmultiples"):
            print('Executing Small Multiples')
            smallMultiples = SmallMultiples(self.folder2d, self.layout_curve)
            smallMultiples.reorder_with_clusters(clustering)
            smallMultiples.draw_small_multiples(propIndex)
        else:
            print(
                'Tipo de desenho não reconhecido, favor escolher entre pixelization e small multiples')
            # TODO  FAZER ILLEGAL EXCEPTION

    def loadStaticMapModels(self, propertyName, propertyFile, indexOfValueField):
        # PARTE DO IZA
        print("modelos do iza carregando")
