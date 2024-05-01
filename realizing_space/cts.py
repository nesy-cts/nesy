from realizing_space.realizing_space import Realizing_Space

class CTS(Realizing_Space):
    def __init__(self, series):
        self.series = series
        self.length = len(series)
        self.initial_state_space = None
        super().__init__()

    def compute_state_space(self):
        self.update_state_space(state_space=list(set(self.series)))

    def convert_to(self, new_state_space):
        self.series = self.get_new_series_with(new_state_space)
        self.initial_state_space = self.state_space
        self.update_state_space(state_space=new_state_space)

    def restrict_to(self, sub_state_space): # sub_state_space is a subset of self.state_space
        self.series = [c for c in self.series if c in sub_state_space]
        self.update_state_space(state_space=sub_state_space)

    def get_new_series_with(self, new_state_space):
        return [new_state_space[self.state_space.index(c)] for c in self.series]

    def get_frequency(self, category):
        return self.series.count(category) / self.length
