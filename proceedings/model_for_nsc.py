import numpy as np
from nested_symmetric_clustering.finite_set.clusters import SetOfClusters, Cluster


def good_format(points_value):
    X = np.array(points_value)
    return X.reshape(-1, 1)


class ModelForNSC:
    def __init__(self, clustering_model):
        self.clustering_model = clustering_model
        self.tailor_clustering_model()
        self.points_value_by_cluster = None
        self.points_name_by_cluster = None
        self.set_of_clusters = None

    def tailor_clustering_model(self):
        self.clustering_model.cluster_centers_ = None
        if not hasattr(self.clustering_model, 'n_clusters'):
            self.clustering_model.n_clusters = None

    def fit(self, points_value, points_name):
        self.clustering_model.fit(good_format(points_value))
        self.compute_set_of_clusters(points_value, points_name)

    def compute_set_of_clusters(self, points_value, points_name):
        self.compute_points_by_clusters(points_value, points_name)

        if self.clustering_model.n_clusters_ is None:
            self.compute_n_clusters()
        if self.clustering_model.cluster_centers_ is None:
            self.compute_cluster_centers()

        self.set_of_clusters = self.get_set_of_clusters()

    def compute_points_by_clusters(self, points_value, points_name):
        self.points_value_by_cluster = self.get_points_by_cluster(points=points_value)
        self.points_name_by_cluster = self.get_points_by_cluster(points=points_name)

    def get_points_by_cluster(self, points):
        points_by_cluster = []
        for ind_cluster in range(self.clustering_model.n_clusters_):
            points_in_cluster = self.get_points_in_cluster(index=ind_cluster,
                                                           points=points)
            points_by_cluster.append(points_in_cluster)
        return points_by_cluster

    def get_points_in_cluster(self, index, points):
        return [point for i, point in enumerate(points) if self.clustering_model.labels_[i] == index]

    def compute_n_clusters(self):
        self.clustering_model.n_clusters_ = np.max(self.clustering_model.labels_) + 1

    def compute_cluster_centers(self):
        self.clustering_model.cluster_centers_ = list(map(np.mean, self.points_value_by_cluster))

    def get_set_of_clusters(self):
        clusters = []
        for names, values in zip(self.points_name_by_cluster, self.points_value_by_cluster):
            clusters.append(Cluster(elements=names, feature=values))
        return SetOfClusters(elements=clusters, cluster_centers=self.clustering_model.cluster_centers_)
