

class Realizing_Space(object):
    def __init__(self):
        self.n_categories = None
        self.state_space = None
        self.compute_state_space()

    def compute_state_space(self):
        pass

    def update_state_space(self, state_space):
        self.state_space = state_space
        self.n_categories = len(state_space)

    def get_new_state_space_by_default(self):
        return ['new_' + c for c in self.state_space]

    def convert_to(self, new_state_space):
        pass

    def convert_by_default(self):
        new_state_space = self.get_new_state_space_by_default()
        self.convert_to(new_state_space)

    def restrict_to(self, sub_state_space):  # sub_state_space is a subset of self.state_space
        pass

    def get_function_computing(self, feature_name):
        return getattr(self, 'get_' + feature_name)

    def get_for_all_state_space(self, feature_name):
        features = []
        func = self.get_function_computing(feature_name)
        for category in self.state_space:
            features.append(func(category))
        return features
