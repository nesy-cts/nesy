import pandas as pd

from nested_symmetric_clustering.finite_set.finite_set import FiniteSet

class Cluster(FiniteSet):
    def __init__(self, elements, feature=None):
        super().__init__(elements)
        self.feature = feature

    def apply(self, model_for_nsc):
        model_for_nsc.fit(points_value=self.feature, points_name=self.elements)
        return model_for_nsc.set_of_clusters

    def compute_feature(self, func):
        self.feature = []
        for element in self.elements:
            self.feature.append(func(category=element))

    def get_labels(self, categories):
        return [category in self.elements for category in categories]


class SetOfClusters(FiniteSet):
    def __init__(self, elements, cluster_centers):
        super().__init__(elements)
        self.cluster_centers = cluster_centers

    def sort(self):
        profile = pd.DataFrame(data={'elements': self.elements, 'cluster_centers': self.cluster_centers})
        profile.sort_values(by='cluster_centers', inplace=True, ignore_index=True)
        self.elements = profile.elements.values
        self.cluster_centers = profile.cluster_centers.values
