from pydtmc import MarkovChain
import pickle
from markov_chain.generate_transition_matrix import trans_markov
from markov_chain.weights import compute_weigths
from realizing_space.cts import CTS

cts_location = "../dataset/cts_dataset/"
name = "MC_scenario_3.pickle"

N = 500000  # length of markov chain
n = 200 # nb of categories

W = [200]
R_possibilities = [0.5]
A_possibilities = [1.1 ** i for i in range(10, 76)]

R, A = compute_weigths(W, R_possibilities, A_possibilities)
P = trans_markov(R, A)

state_space = ['a' + chr(i) for i in range(40, 40 + n)]
mc = MarkovChain(P, state_space)
cts = mc.simulate(N, seed=400)

cts = CTS(series=cts)

with open(cts_location + name, "wb") as cts_file:
    pickle.dump(obj=cts, file=cts_file)
