from pydtmc import MarkovChain
import pickle
from markov_chain.generate_transition_matrix import trans_markov
from markov_chain.weights import compute_weigths
from realizing_space.cts import CTS
import matplotlib.pyplot as plt
import copy
import numpy as np

N = 500000  # length of markov chain
n = 200 # nb of categories

# scenario 1
# W = [n-(n//4)-(n//5)-(n//7)-(n//10), n//4, n//5, n//7, n//10]
# R_possibilities = [0.3, 0.6, 0.7, 0.8, 0.9]
# A_possibilities = [1, 2, 3, 4, 5]

# scenario 2

# W = [3]*65 + [5]
# R_possibilities = [0.01 * i for i in range(10, 76)]
# A_possibilities = [1] * 66

# scenario 3

W = [200]
R_possibilities = [0.5]
A_possibilities = [1.1 ** i for i in range(10, 76)]




R, A = compute_weigths(W, R_possibilities, A_possibilities)
P = trans_markov(R, A)


P1 = copy.copy(P)
P2 = copy.copy(P)
for i in range(n):
    P2[i, i] = 0

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(P2, interpolation='nearest')
fig.colorbar(cax)
plt.show()

state_space = ['a' + chr(i) for i in range(40, 40 + n)]
mc = MarkovChain(P, state_space)

cts = mc.simulate(N, seed=400)

freq = [cts.count(e)/len(cts) for e in state_space]

cts_location = "../dataset/cts_dataset/MC_scenario_3_4.pickle"

cts = CTS(series=cts)

with open(cts_location, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)

