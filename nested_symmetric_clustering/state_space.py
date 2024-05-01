from nested_symmetric_clustering.finite_set.common_set_of_categories import CommonSetOfCategories


class StateSpace(CommonSetOfCategories):
    def __init__(self, realizing_spaces):
        self.realizing_spaces = realizing_spaces
        super().__init__(sets_of_categories=self.get_state_spaces())
        if not super().is_same_sets():
            self.intersect_realizing_spaces()

    def get_state_spaces(self):
        return [realizing_space.state_space for realizing_space in self.realizing_spaces]

    def intersect_realizing_spaces(self):
        for realizing_space in self.realizing_spaces:
            realizing_space.restrict_to(sub_state_space=self.elements)

    def get_features_from(self, features, elements):
        return [features[self.elements.index(e)] for e in elements]
