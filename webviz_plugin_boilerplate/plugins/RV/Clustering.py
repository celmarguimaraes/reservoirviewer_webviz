from sklearn import metrics
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np


class Clustering:
    def __init__(self, method, distMatrix, minClusters, maxClusters, numIter):
        self.method = method
        self.distMatrix = distMatrix
        self.minClusters = minClusters
        self.maxClusters = maxClusters
        self.numIterations = numIter
        self.clusterDict = {}
        
        print("Min clusters, max Clusters: ", self.minClusters," ", self.maxClusters)
        
        print()

    def getMethod(self): return self.method 
    def getDistMatrix(self): return self.distMatrix 
    def getMin(self): return self.min 
    def getMax(self): return self.max 
    def get_dict(self): return self.clusterDict 
    def getNumIterations(self): return self.numIterations 

    def clusterGrid(self, grid):
        distortions = []
        inertias = []
        mapping1 = {}
        mapping2 = {}
        K = range(self.minClusters, self.maxClusters)
        inertiaAcumulada = 0
        bestK = 0
        
        for k in K:
            # Building and fitting the model
            kmeanModel = KMeans(n_clusters=k).fit(grid)
            inertias.append(kmeanModel.inertia_)
            mapping2[k] = kmeanModel.inertia_
            
        for idx, k in enumerate(mapping2):
            inertiaAcumulada = np.sum(inertias[0:idx])
            inercias = np.sum(inertias)
            
            if (inertiaAcumulada/inercias >= 0.85 ):
                bestK = k
                break
        
        kmeanModel = KMeans(n_clusters=bestK).fit(grid)
        kmeanModel.fit(grid)
        y_kmeans = kmeanModel.predict(grid)

        for idx, g in enumerate(grid):
            self.clusterDict[idx] = y_kmeans[idx]
            