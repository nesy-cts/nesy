from nested_symmetric_clustering.pair_cluster import PairCluster
from nested_symmetric_clustering.finite_set.clusters import Cluster
import copy
import numpy as np

def get_rand_partition(set, k):
    n = len(set)
    L = copy.copy(set)
    rand_partition = []
    nb_per_clusters = [n//k]*(k-1) + [n - (k-1)*(n//k) ]
    for nb in nb_per_clusters:
        rand_cluster = np.random.choice(L, nb, replace=False)
        for e in rand_cluster:
            L.remove(e)
        rand_partition.append(rand_cluster)
    return rand_partition

def get_image(clusters, known_pairs):
    image = []
    for cluster in clusters:
        image_cluster = []
        for e in cluster:
            if e in known_pairs[0]:
                i = known_pairs[0].index(e)
                image_cluster.append(known_pairs[1][i])
        image.append(image_cluster)
    return image

def get_pair_of_clusters(clusters1, clusters2):
    pair_clusters = []
    for cluster1, cluster2 in zip(clusters1, clusters2):
        c1 = Cluster(elements=cluster1)
        c2 = Cluster(elements=cluster2)
        pair_clusters.append(PairCluster(cluster1=c1, cluster2=c2))
    return pair_clusters


class RandomPairClusters:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def get(self, k, known_pairs):
        rand_clusters1 = get_rand_partition(self.set1, k)
        partial_clusters2 = get_image(rand_clusters1, known_pairs)
        rand_clusters2 = self.complete_randomly(partial_clusters2)
        pair_clusters = get_pair_of_clusters(rand_clusters1, rand_clusters2)
        return pair_clusters

    def complete_randomly(self, partial_clusters):
        n = len(partial_clusters)
        missing_elements = self.missing_elements(partial_clusters)
        for e in missing_elements:
            i = np.random.randint(n)
            partial_clusters[i].append(e)
        return partial_clusters

    def missing_elements(self, partial_clusters):
        res = copy.copy(self.set2)
        for cluster in partial_clusters:
            for e in cluster:
                res.remove(e)
        return res



# rpc = RandomPairClusters(set1=list(range(20)), set2=list(range(21, 38)))
#
# rand_clusters1, rand_clusters2 = rpc.get(3, [list(range(10)), list(range(21, 31))])
#
# print(rand_clusters1)
# print(rand_clusters2)
