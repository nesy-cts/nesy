from nested_symmetric_clustering.state_space import StateSpace
from data.cts_access import load_list_cts
from nested_symmetric_clustering.nested_symmetric_clustering import NestedSymmetricClustering
from nested_symmetric_clustering.random_pair_clusters import RandomPairClusters

files_name1 = ['HMM_scenario_2_1', 'HMM_scenario_2_2']
files_name2 = ['new_HMM_scenario_2_3', 'new_HMM_scenario_2_4']

state_space1 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name1))
state_space2 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name2))
n = 200

set1 = ['e' + str(i) for i in range(n)]
set2 = ['new_' + 'e' + str(i) for i in range(n)]

give_random = 90

rpc = RandomPairClusters(set1=set1, set2=set2)
pair_clusters = rpc.get(k = 90, known_pairs=[set1[:int(give_random/100 * n):], set2[:int(give_random/100 * n):]])
state_space1.elements = set1
state_space2.elements = set2
nesy = NestedSymmetricClustering(state_space1=state_space1,
                                  state_space2=state_space2,
                                  mapping_by_default=True)
nesy.pair_clusters = pair_clusters

nesy.compute_prm()
nesy.compute_tailored_AMI()

nesy.display()