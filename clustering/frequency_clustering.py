import warnings
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.cluster import adjusted_mutual_info_score
from itertools import product
import copy


def gini(x):
    x = np.array(x, dtype=np.float32)
    n = len(x)
    diffs = sum(abs(i - j) for i, j in product(x, repeat=2))
    return diffs / (2 * n ** 2 * x.mean())


def max_gini(n_clusters, nb_elements):
    L = [0] * n_clusters
    L[0] = nb_elements
    return gini(L)


def transformed_gini(nb_element_per_cluster):
    g = gini(nb_element_per_cluster)
    max_g = max_gini(n_clusters=len(nb_element_per_cluster), nb_elements=sum(nb_element_per_cluster))
    return 1 - g/max_g


def transformation(f, lbd):
    return (1 - np.exp(-lbd * f)) / (1 - np.exp(-lbd))


class FrequencyClustering:
    def __init__(self, model, adjustment_frequencies):
        self.n_clusters_ = None
        self.score = None
        self.scores = None
        self.cluster_centers_ = None
        self.clusters = None
        self.labels_ = None
        self.model = model
        self.model_adjustment = copy.deepcopy(model)
        self.model.cluster_centers_ = None
        self.lbd = 1
        self.adjustment_frequencies = adjustment_frequencies

    def classify(self, frequencies, verbose=False):
        X = np.array([transformation(f, lbd=self.lbd) for f in frequencies])
        X = X.reshape(-1, 1)
        self.model.fit(X)
        self.compute_score(verbose)
        self.labels_ = self.model.labels_

    def compute_score(self, verbose=False):
        n_clusters = np.max(self.model.labels_) + 1
        nb_element_per_cluster = [np.sum(self.model.labels_ == i)
                                  for i in range(n_clusters)]
        X = np.array([transformation(f, lbd=self.lbd) for f in self.adjustment_frequencies])
        X = X.reshape(-1, 1)
        self.model_adjustment.fit(X)
        self.score = ((transformed_gini(nb_element_per_cluster)) *
                      adjusted_mutual_info_score(labels_true=self.model_adjustment.labels_,
                                                 labels_pred=self.model.labels_)**3)
        if verbose:
            print('transformed_gini = ', transformed_gini(nb_element_per_cluster))
            print('nb_element_per_cluster = ', nb_element_per_cluster)
            print('intra ami score = ', adjusted_mutual_info_score(labels_true=self.model_adjustment.labels_,
                                                             labels_pred=self.model.labels_))
            print('score = ', self.score)

    def optimize_transformation(self, frequencies):
        self.scores = []
        for lbd in range(1, 1500):
            warnings.filterwarnings('ignore')
            self.lbd = lbd
            self.classify(frequencies)
            self.scores.append(self.score)
            if lbd % 500 == 0:
                print(lbd)
                print(self.score)
                print(" ")
        plt.plot(self.scores)
        plt.show()

        scores = np.array(self.scores)
        self.lbd = np.where(scores == np.max(scores))[0][0] + 1
        print("lambda max : ", self.lbd)
        print("objective max : ", self.scores[int(self.lbd) - 1])

    def fit(self, frequencies):
        frequencies.reshape(-1)
        self.optimize_transformation(frequencies)
        self.classify(frequencies, verbose=True)
        if self.model.cluster_centers_ is not None:
            self.cluster_centers_ = self.model.cluster_centers_
        self.n_clusters_ = np.max(self.model.labels_) + 1
