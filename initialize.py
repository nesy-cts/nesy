from nested_symmetric_clustering.state_space import StateSpace
from data.nsc_access import dump_list_nsc
from data.cts_access import load_list_cts
from nested_symmetric_clustering.nested_symmetric_clustering import NestedSymmetricClustering

files_name1 = ['open_stack_logs_1', 'open_stack_logs_2']
files_name2 = ['spark_logs_1', 'spark_logs_2']

state_space1 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name1))
state_space2 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name2))

nesy1 = NestedSymmetricClustering(state_space1=state_space1,
                                  state_space2=state_space2,
                                  mapping_by_default=True)

files_name1 = ['open_stack_logs_2', 'open_stack_logs_1']
files_name2 = ['spark_logs_2', 'spark_logs_1']

state_space1 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name1))
state_space2 = StateSpace(realizing_spaces=load_list_cts(files_name=files_name2))

nesy2 = NestedSymmetricClustering(state_space1=state_space1,
                                  state_space2=state_space2,
                                  mapping_by_default=True)

dump_list_nsc([nesy1, nesy2], ['current_symmetric_clustering_state1',
                                               'current_symmetric_clustering_state2'])
