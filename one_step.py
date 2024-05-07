from data.nsc_access import load_list_nsc, dump_list_nsc
from sklearn.cluster import AgglomerativeClustering

file_names = ['current_symmetric_clustering_state1', 'current_symmetric_clustering_state2']
feature_name='frequency'
algorithms_schema = [[AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)],
                     [AgglomerativeClustering(n_clusters=2), AgglomerativeClustering(n_clusters=2)]
                     ]
list_is_concerned = [False, False, False, False, False, False, False, False, False, False, False, False, False,
                     False, False, False]

nesy1, nesy2 = load_list_nsc(file_names=file_names)
nesy1.proceed(algorithms_schema=algorithms_schema,
              feature_name=feature_name,
              list_is_concerned=list_is_concerned)

nesy2.proceed(algorithms_schema=algorithms_schema,
              feature_name=feature_name,
              list_is_concerned=list_is_concerned)

nesy1.compute_crossed_jaccard(nesy2)
nesy1.compute_prm()
# nesy1.compute_tailored_AMI()

dump_list_nsc([nesy1, nesy2], file_names=file_names)
