from data.cts_access import load_list_cts, dump_list_cts
from nested_symmetric_clustering.state_space import StateSpace

files_name = ['open_stack_logs_1', 'open_stack_logs_2']
state_space = StateSpace(realizing_spaces=load_list_cts(files_name=files_name))
dump_list_cts(list_cts=state_space.realizing_spaces, files_name=files_name)
