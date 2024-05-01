from clustering.pair_clustering_algorithms import PairClusteringAlgorithms
from proceedings.model_for_nsc import ModelForNSC

class ProceedingsNSC:
    def __init__(self,
                 algorithms_schema,
                 parallel_feature1,
                 parallel_feature2,
                 list_is_concerned,
                 pair_clusters,
                 state_space1,
                 state_space2
                 ):
        self.pair_models = []
        self.compute_pair_models(algorithms_schema,
                                 parallel_feature1,
                                 parallel_feature2,
                                 pair_clusters,
                                 state_space1,
                                 state_space2)
        self.list_is_concerned = list_is_concerned

    def is_concerned(self, index):
        return self.list_is_concerned[index]

    def get_pair_model(self, index):
        return self.pair_models[index]

    def compute_pair_models(self,
                            algorithms_schema,
                            parallel_feature1,
                            parallel_feature2,
                            pair_clusters,
                            state_space1,
                            state_space2):
        pair_clustering_algorithms = PairClusteringAlgorithms(algorithms_schema=algorithms_schema,
                                                              pair_clusters=pair_clusters,
                                                              parallel_feature1=parallel_feature1,
                                                              parallel_feature2=parallel_feature2,
                                                              state_space1=state_space1,
                                                              state_space2=state_space2)
        for clustering_algorithm1, clustering_algorithm2 in pair_clustering_algorithms.list:
            self.pair_models.append([ModelForNSC(clustering_model=clustering_algorithm1),
                                     ModelForNSC(clustering_model=clustering_algorithm2)])
