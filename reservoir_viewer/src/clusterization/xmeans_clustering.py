from pyclustering.cluster.xmeans import xmeans

class Xmeans:
    def __init__(self, data, iterations, max_clusters):
        self.data = data
        self.iterations = iterations
        self.max_clusters = max_clusters

    def cluster_models(self):
        xmeans_instance = xmeans(data=self.data, kmax=self.max_clusters, tolerance=self.iterations)
        xmeans_instance.process()

        return xmeans_instance.get_centers()
