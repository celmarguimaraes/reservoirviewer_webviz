from pyclustering.cluster.xmeans import xmeans
from .clusterization_utils import ClusterizationUtils


class XmeansClusterization:
    def __init__(self, data, max_clusters):
        self.data = data
        self.max_clusters = max_clusters

    def cluster_models(self):
        utils = ClusterizationUtils(self.data)
        feature_vector = utils.create_feature_vector()
        xmeans_instance = xmeans(data=feature_vector, kmax=self.max_clusters)
        xmeans_instance.process()

        clusters = xmeans_instance.get_clusters()
        print(clusters)

        return clusters
