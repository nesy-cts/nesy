import numpy as np
import copy

# groups : two criteria per elements r = P(x|x) and a = P(x)
# n elements
# arguments : n int > 1, R list of length n, A list of length n

def trans_markov(R, A):
    # compute F
    n = len(R)
    F = np.zeros((n, n))
    for i in range(n):
        L = copy.copy(A)
        L.pop(i)
        tot = sum(L)
        for j in range(n):
            if j != i:
                F[i, j] = A[j]/tot

    # compute transition matrix
    P = np.diag(R)
    for i in range(n):
        for j in range(n):
            if i != j:
                P[i, j] = (1-R[i]) * F[i, j]
    return P
