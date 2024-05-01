import pickle

def get_path(file_name):
    return 'dataset/cts_dataset/' + file_name + ".pickle"

def load_cts(file_name):
    path_file = get_path(file_name)
    with open(path_file, 'rb') as cts_file:
        cts = pickle.load(cts_file)
    return cts

def load_list_cts(files_name):
    return [load_cts(file_name) for file_name in files_name]

def dump_cts(cts, file_name):
    path_file = get_path(file_name)
    with open(path_file, "wb") as cts_file:
        pickle.dump(obj=cts, file=cts_file)
    return cts

def dump_list_cts(list_cts, files_name):
    return [dump_cts(cts, file_name) for cts, file_name in zip(list_cts, files_name)]

