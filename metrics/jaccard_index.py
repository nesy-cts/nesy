

def jaccard_index(set1, set2):
    inter = [x for x in set1 if x in set2]
    union = list(set(set1 + set2))
    return len(inter)/len(union)
