from clustering.frequency_clustering import FrequencyClustering

class PairClusteringAlgorithms:
    def __init__(self,
                 algorithms_schema,
                 pair_clusters,
                 parallel_feature1,
                 parallel_feature2,
                 state_space1,
                 state_space2):
        self.list = []
        for ((support_clustering_algorithm1, support_clustering_algorithm2),
             pair_cluster) in zip(algorithms_schema, pair_clusters):
            features1 = state_space1.get_features_from(features=parallel_feature1,
                                                        elements=pair_cluster.cluster1.elements)
            features2 = state_space2.get_features_from(features=parallel_feature2,
                                                        elements=pair_cluster.cluster2.elements)
            self.list.append([FrequencyClustering(model=support_clustering_algorithm1,
                                                  adjustment_frequencies=features1),
                              FrequencyClustering(model=support_clustering_algorithm2,
                                                  adjustment_frequencies=features2)])

