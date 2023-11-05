from pyclustering.cluster.xmeans import xmeans
from .clusterization_utils import CLusterizationUtils


class XmeansClusterization:
    def __init__(self, data, max_clusters):
        self.data = data
        self.max_clusters = max_clusters

    def cluster_models(self):
        clusters_list = []
        utils = CLusterizationUtils(self.data)
        feature_vector = utils.create_feature_vector()
        xmeans_instance = xmeans(data=feature_vector, kmax=self.max_clusters)
        xmeans_instance.process()

        clusters = xmeans_instance.get_clusters()

        for cluster in clusters:
            clusters_list = clusters_list + cluster

        return clusters_list
