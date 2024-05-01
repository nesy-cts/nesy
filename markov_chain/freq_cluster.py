

def get_freq_group(n_tot, weights):
    n_group = len(weights)
    size = n_tot // (n_group - 1)
    res = []
    sum_weights = sum(weights)
    for i in range(n_group - 1):
        res = res + [weights[i]/(size*sum_weights)] * size

    last_size = n_tot - (n_group - 1) * size
    res = res + [weights[-1]/(last_size*sum_weights)] * last_size
    return res

