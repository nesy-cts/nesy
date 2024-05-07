from pydtmc import MarkovChain
import pickle
from markov_chain.generate_transition_matrix import trans_markov
from markov_chain.weights import compute_weigths
from realizing_space.cts import CTS

cts_location = "../dataset/cts_dataset/"
name = "MC_scenario_1.pickle"

N = 500000  # length of markov chain
n = 200 # nb of categories

W = [n-(n//4)-(n//5)-(n//7)-(n//10), n//4, n//5, n//7, n//10]
R_possibilities = [0.3, 0.6, 0.7, 0.8, 0.9]
A_possibilities = [1, 2, 3, 4, 5]

R, A = compute_weigths(W, R_possibilities, A_possibilities)
P = trans_markov(R, A)

state_space = ['a' + chr(i) for i in range(40, 40 + n)]
mc = MarkovChain(P, state_space)
cts = mc.simulate(N, seed=400)

cts = CTS(series=cts)

with open(cts_location + name, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)
