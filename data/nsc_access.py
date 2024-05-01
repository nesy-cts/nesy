import pickle
import json

folder = "symmetric_clustering_state/"

def load_nsc(file_name):
    with open(folder + file_name + ".pickle", "rb") as read_file:
        nesy = pickle.load(read_file)
    return nesy

def dump_nsc(nesy, file_name):
    clustering_state = []
    for pair_cluster in nesy.pair_clusters:
        pair = {'elements_1': list(pair_cluster.cluster1.elements),
                'elements_2': list(pair_cluster.cluster2.elements)}
        clustering_state.append(pair)
    with open(folder + file_name + ".json", "w") as write_file:
        json.dump(clustering_state, write_file)
    with open(folder + file_name + ".pickle", "wb") as write_file:
        pickle.dump(obj=nesy, file=write_file)

def dump_list_nsc(nesys, file_names):
    for nesy, file_name in zip(nesys, file_names):
        dump_nsc(nesy, file_name)

def load_list_nsc(file_names):
    return [load_nsc(file_name) for file_name in file_names]
