import matplotlib.pyplot as plt
from sklearn.metrics.cluster import adjusted_mutual_info_score

from nested_symmetric_clustering.pair_cluster import PairCluster
from proceedings.proceedings_nsc import ProceedingsNSC
from metrics.pairwise_reduction_measure import pairwise_reduction_measure
from metrics.jaccard_index import jaccard_index

def default_mapping(element):
    return 'new_' + element

def get_classification(set_of_clusters, state_space):
    classification = [0]*len(state_space)
    for i, cluster in enumerate(set_of_clusters):
        for element in cluster:
            classification[state_space.index(element)] = i
    return classification

class NestedSymmetricClustering:
    def __init__(self, state_space1, state_space2, mapping_by_default=False):
        self.mapping = None
        self.state_space1 = state_space1
        self.state_space2 = state_space2
        self.pair_clusters = [PairCluster(cluster1=state_space1, cluster2=state_space2)]

        self.realizing_space1 = self.state_space1.realizing_spaces[0]
        self.realizing_space2 = self.state_space2.realizing_spaces[0]

        self.proceedings = None

        self.prms = [0]
        self.crossed_jaccard_indexes = [1]
        self.tailored_amis = [1]

        if mapping_by_default:
            self.mapping = default_mapping

    def compute_proceedings(self, algorithms_schema, feature_name, list_is_concerned):
        parallel_feature1, parallel_feature2 = self.get_parallel(feature_name)
        self.proceedings = ProceedingsNSC(algorithms_schema=algorithms_schema,
                                          parallel_feature1=parallel_feature1,
                                          parallel_feature2=parallel_feature2,
                                          list_is_concerned=list_is_concerned,
                                          pair_clusters=self.pair_clusters,
                                          state_space1=self.state_space1,
                                          state_space2=self.state_space2)

    def proceed(self, algorithms_schema, feature_name, list_is_concerned):
        self.compute_proceedings(algorithms_schema, feature_name, list_is_concerned)
        self.one_step_on(feature_name)

    def get_parallel_realizing_spaces(self):
        return self.state_space1.realizing_spaces[1], self.state_space2.realizing_spaces[1]

    def get_parallel(self, feature_name):
        realizing_space1, realizing_space2 = self.get_parallel_realizing_spaces()
        parallel_feature1 = realizing_space1.get_for_all_state_space(feature_name)
        parallel_feature2 = realizing_space2.get_for_all_state_space(feature_name)
        return parallel_feature1, parallel_feature2

    def one_step_on(self, feature_name):
        new_dual_clusters = []
        for ind, dual_cluster in enumerate(self.pair_clusters):
            if self.proceedings.is_concerned(index=ind):
                pair_model = self.proceedings.get_pair_model(index=ind)
                dual_cluster.compute_features(func1=self.realizing_space1.get_function_computing(feature_name),
                                              func2=self.realizing_space2.get_function_computing(feature_name))
                dual_clusters = dual_cluster.perform_symmetric_clustering(pair_model=pair_model)
                new_dual_clusters.extend(dual_clusters)
            else:
                new_dual_clusters.append(dual_cluster)
        self.pair_clusters = new_dual_clusters

    def compute_features(self, feature_name, proceedings):
        for ind, dual_cluster in enumerate(self.pair_clusters):
            if proceedings.is_concerned(index=ind):
                dual_cluster.compute_features(func1=self.realizing_space1.get_function_computing(feature_name),
                                              func2=self.realizing_space2.get_function_computing(feature_name))

    def compute_prm(self):
        self.prms.append(pairwise_reduction_measure(n1=len(self.state_space1.elements),
                                                    n2=len(self.state_space2.elements),
                                                    pair_of_clusters=self.pair_clusters))

    def compute_crossed_jaccard(self, new_nesy):
        matches1 = self.compute_possible_matches()
        matches2 = new_nesy.compute_possible_matches()
        self.crossed_jaccard_indexes.append(jaccard_index(set1=matches1,
                                                          set2=matches2))

    def compute_possible_matches(self):
        matches = []
        for pair_cluster in self.pair_clusters:
            matches.extend(pair_cluster.get_matches())
        return matches

    def display(self):
        print('last PRM : ', self.prms[-1])
        print('last tailored ami : ', self.tailored_amis[-1])
        print('last crossed realizing-space jaccard index : ', self.crossed_jaccard_indexes[-1])
        print('number of pair of clusters :', len(self.pair_clusters))
        for pair_cluster in self.pair_clusters:
            print([len(pair_cluster.cluster1.elements), len(pair_cluster.cluster2.elements)])
        # plt.plot(self.tailored_amis, label='Tailored AMI')
        plt.plot(self.prms, label='PRM')
        plt.plot(self.crossed_jaccard_indexes, label=' Jaccard Index')
        plt.xlabel('Number of Symmetric Clustering')
        plt.legend()
        plt.show()

    def compute_tailored_AMI(self):
        set_of_clusters1, set_of_clusters2 = self.get_true_and_predicted_clusters()
        classification1 = get_classification(set_of_clusters=set_of_clusters1,
                                             state_space=self.state_space2.elements)
        classification2 = get_classification(set_of_clusters=set_of_clusters2,
                                             state_space=self.state_space2.elements)
        self.tailored_amis.append(adjusted_mutual_info_score(labels_true=classification1,
                                                             labels_pred=classification2))

    def get_true_and_predicted_clusters(self):
        set_of_clusters1 = []
        set_of_clusters2 = []
        for pair_cluster in self.pair_clusters:
            set_of_clusters1.append([self.mapping(e) for e in pair_cluster.cluster1.elements])
            set_of_clusters2.append(pair_cluster.cluster2.elements)
        return set_of_clusters1, set_of_clusters2
