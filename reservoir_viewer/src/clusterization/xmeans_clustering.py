from pyclustering.cluster.xmeans import xmeans
from .clusterization_utils import ClusterizationUtils


class XmeansClusterization:
    def __init__(self, data, max_clusters, min, max):
        self.data = data
        self.max_clusters = max_clusters
        self.min = min
        self.max = max

    def cluster_models(self):
        utils = ClusterizationUtils(self.data)
        feature_vector = utils.create_feature_vector(self.min, self.max)
        xmeans_instance = xmeans(data=feature_vector, kmax=self.max_clusters)
        xmeans_instance.process()

        clusters = xmeans_instance.get_clusters()

        return clusters
