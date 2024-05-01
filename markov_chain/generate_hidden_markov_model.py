from pydtmc import HiddenMarkovModel
import pickle
from markov_chain.freq_cluster import get_freq_group
from realizing_space.cts import CTS
import matplotlib.pyplot as plt
import copy

N = 500000  # length of markov chain
n = 200 # nb of categories

# scenario 1
P = [[0.5, 0.3, 0.2], [0.1, 0.6, 0.3], [0.4, 0.1, 0.5]]
E1 = [get_freq_group(n, [1.3 ** i for i in range(20)]) for i in range(3)]

# scenario 2
P2 = [[0.5, 0.3, 0.2], [0.1, 0.6, 0.3], [0.4, 0.1, 0.5]]
E2 = [get_freq_group(n, [3 ** i for i in range(4)]) for i in range(3)]


# E1p = [e[:-2:] for e in E1]
# E2p = [e[:-2:] for e in E2]
# fig, axs = plt.subplots(2)
# cax1 = axs[0].matshow(E1p, interpolation='nearest')
# fig.colorbar(cax1, orientation="horizontal", ax=axs[0])
# cax2 = axs[1].matshow(E2p, interpolation='nearest')
# fig.colorbar(cax2, orientation="horizontal", ax=axs[1])
# plt.show()

E1p = [e[:-2:] for e in E2]
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(E1p, interpolation='nearest')
fig.colorbar(cax, orientation="horizontal")
plt.show()



state_space = ['E' + str(i) for i in range(1, 201)]
hmm = HiddenMarkovModel(P, E1)

_, cts = hmm.simulate(N, seed=400)

freq = [cts.count(e)/len(cts) for e in state_space]

cts_location = "../dataset/cts_dataset/HMM_scenario_2_4.pickle"

cts = CTS(series=cts)

with open(cts_location, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)

