from sklearn import metrics
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np


class Clustering:
    def __init__(self, method, dist_matrix, min_clusters, max_clusters, numIter):
        self.method = method
        self.dist_matrix = dist_matrix
        self.min_clusters = min_clusters
        self.max_clusters = max_clusters
        self.num_iterations = numIter
        self.cluster_dict = {}

    def getMethod(self): return self.method 
    def getdist_matrix(self): return self.dist_matrix 
    def getMin(self): return self.min 
    def getMax(self): return self.max 
    def get_dict(self): return self.cluster_dict 
    def getnum_iterations(self): return self.num_iterations 

    def clusterGrid(self, grid):
        print('Clustering Grid')
        print("Min clusters: ", self.min_clusters,", max Clusters: ", self.max_clusters)
        inertias = []
        map_inertia = {}
        K = range(self.min_clusters, self.max_clusters)
        accumulated_inertia = 0
        best_k = 0
        
        for k in K:
            # Building and fitting the model
            kmean_model = KMeans(n_clusters=k).fit(grid)
            inertias.append(kmean_model.inertia_)
            map_inertia[k] = kmean_model.inertia_
            
        for idx, k in enumerate(map_inertia):
            # Choosing best K
            accumulated_inertia = np.sum(inertias[0:idx])
            inertias_sum = np.sum(inertias)
            
            if (accumulated_inertia/inertias_sum >= 0.65 ):
                best_k = k
                break
        
        # Clustering with best K
        print("Chosen number of clusters: ", best_k)
        kmean_model = KMeans(n_clusters=best_k).fit(grid)
        kmean_model.fit(grid)
        y_kmeans = kmean_model.predict(grid)

        for idx, g in enumerate(grid):
            # Generate a dict with the cluster of each model
            self.cluster_dict[idx] = y_kmeans[idx] 
            