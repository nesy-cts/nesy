from pydtmc import HiddenMarkovModel
import pickle
from markov_chain.freq_cluster import get_freq_group
from realizing_space.cts import CTS

cts_location = "../dataset/cts_dataset/"
name = "HMM_scenario_2.pickle"

N = 500000  # length of markov chain
n = 200 # nb of categories

P = [[0.5, 0.3, 0.2], [0.1, 0.6, 0.3], [0.4, 0.1, 0.5]]
E = [get_freq_group(n, [3 ** i for i in range(4)]) for i in range(3)]

state_space = ['E' + str(i) for i in range(1, 201)]
hmm = HiddenMarkovModel(P, E)
_, cts = hmm.simulate(N, seed=400)

cts = CTS(series=cts)

with open(cts_location + name, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)
