import re
from .Strategy import Strategy
from .Property import Property
from .WellList import WellList
from .SmallMultiples import SmallMultiples


class Configuration:
    def __init__(self, configs):
        self.root = configs[0]
        self.benchmark = configs[1]
        self.folder2d = configs[2]
        self.folderDistMatr = configs[3]
        self.chartType = configs[4]
        self.layoutCurve = configs[5]
        self.lustMethod = configs[6]
        self.distMatrix = configs[7]
        self.minClusters = int(configs[8])
        self.maxClusters = int(configs[9])
        self.numIterations = int(configs[10])
        self.allModels = configs[13]
        self.hlModels = configs[14]
        self.strategies = []
        self.properties = []

        parseStringFirst(self, configs[11], "Property")
        parseStringFirst(self, configs[12], "Strategy")

        settingDrawConfigs(self, self.strategies)


def getStrategies(self):
    for strat in self.strategies:
        print("Estrategia: "+strat.getStrategy())


def getProperties(self):
    for prop in self.properties:
        print("Propriedade: "+prop.getProperty())


def parseStringFirst(self, strats, typeOfRegex):
    stringStrats = strats
    arrayStrats = []

    arrayStrats = eval(f"{stringStrats}")
    for strat in arrayStrats:
        parseStringSecond(self, strat, typeOfRegex)


def parseStringSecond(self, strats, typeOfRegex):
    stringStrats = strats
    arrayStrats = []

    arrayStrats = stringStrats.split(";")

    if (typeOfRegex == "Property"):
        property = Property(arrayStrats)
        self.properties.append(property)
    elif (typeOfRegex == "Strategy"):
        strategy = Strategy(arrayStrats)
        self.strategies.append(strategy)


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


# TODO LEMBRAR DE MUDAR NOME (PENSAR EM UM NOME DECENTE)
def settingDrawConfigs(self, estrategias):
    for p in self.properties:
        print("pegando propriedade")
        distMatrixFileName = self.distMatrix
        meanType = p.convertMeanType()
        # TODO this.loadStaticMapModels(propName, self.root/self.file2d/self.getNullBlocks, meanType)
        if (distMatrixFileName == "MODELS3D_ALL_PROP" or distMatrixFileName == "MODELS3D_PROP"):

            # TODO FAZER FILE WRITER
            distMatrixPath = self.root + "/" + self.folderDistMatr + "/" + distMatrixFileName

            # TODO Clustering clusteringData = self.clusterConfig.clusterReservoirsMatrixFile(distMatrixPath, false)
            # TODO self.clusterConfig.reorderReservoirByClusters(clusteringData)

        elif (distMatrixFileName == "FEATVECTORS_PROP"):

            # TODO FAZER FILE WRITER

            # TODO featureVecFile = self.clusteringConfig.createReservoirFeatureVecMatrix()
            # TODO Clustering clusteringData = self.clusterConfig.clusterReservoirsFeatMatrix(featureVecFile)
            # TODO self.clusterConfig.reorderReservoirByClusters(clusteringData)
            print("Feature Vectors")

        if (self.chartType == "pixelization"):
            print('pixelization')
        elif (self.chartType == "smallmultiples"):
            print('small multiples')
            smallMultiples = SmallMultiples(self.folder2d, self.layoutCurve)
        else:
            print(
                'Tipo de desenho não reconhecido, favor escolher entre pixelization e small multiples')
            # TODO  FAZER ILLEGAL EXCEPTION

    def loadStaticMapModels(self, propertyName, propertyFile, indexOfValueField):
        # PARTE DO IZA
        print("modelos do iza carregando")
