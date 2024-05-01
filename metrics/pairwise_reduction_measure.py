

def pairwise_reduction_measure(n1, n2, pair_of_clusters):
    nb_possible_matches = 0
    for pair_cluster in pair_of_clusters:
        nb_possible_matches += len(pair_cluster.cluster1.elements) * len(pair_cluster.cluster2.elements)
    return (n1 * n2 - nb_possible_matches) / (n1 * n2 - max(n1, n2))
