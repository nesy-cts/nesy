from sklearn.metrics.cluster import adjusted_mutual_info_score
from itertools import product


class PairCluster:
    def __init__(self, cluster1, cluster2):
        self.cluster1 = cluster1
        self.cluster2 = cluster2

    def perform_symmetric_clustering(self, pair_model):
        set_of_clusters1, set_of_clusters2 = self.apply(pair_model=pair_model)
        set_of_clusters1.sort()
        set_of_clusters2.sort()
        return [PairCluster(cluster1=cluster1, cluster2=cluster2)
                for cluster1, cluster2 in zip(set_of_clusters1.elements, set_of_clusters2.elements)]

    def apply(self, pair_model):
        set_of_clusters1 = self.cluster1.apply(model_for_nsc=pair_model[0])
        set_of_clusters2 = self.cluster2.apply(model_for_nsc=pair_model[1])
        return set_of_clusters1, set_of_clusters2

    def compute_features(self, func1, func2):
        self.cluster1.compute_feature(func=func1)
        self.cluster2.compute_feature(func=func2)

    def get_ami(self, categories1, categories2):
        labels1, labels2 = self.get_dual_labels(categories1, categories2)
        return adjusted_mutual_info_score(labels_true=labels1,
                                          labels_pred=labels2)

    def get_dual_labels(self, categories1, categories2):
        labels1 = self.cluster1.get_labels(categories1)
        labels2 = self.cluster2.get_labels(categories2)
        return labels1, labels2

    def get_matches(self):
        return list(product(self.cluster1.elements, self.cluster2.elements))
