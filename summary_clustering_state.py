from data.nsc_access import load_nsc

file_name = 'current_symmetric_clustering_state1'

nesy1 = load_nsc(file_name=file_name)

nesy1.display()
