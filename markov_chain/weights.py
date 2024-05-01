

def compute_weigths(W, R_possibilities, A_possibilities):
    n = sum(W)
    R = []
    A = []
    len_A_possibilities = len(A_possibilities)
    for r, w in zip(R_possibilities, W):
        R = R + [r] * w
        for a in A_possibilities:
            A = A + [a]*(w//len_A_possibilities)
    A = A + [A_possibilities[-1]] * (n - len(A))
    return R, A
