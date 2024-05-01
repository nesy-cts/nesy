from nested_symmetric_clustering.finite_set.clusters import Cluster

class CommonSetOfCategories(Cluster):
    def __init__(self, sets_of_categories):
        self.sets_of_categories = sets_of_categories
        super().__init__(elements=self.get_intersection())

    def get_intersection(self):
        intersection = self.sets_of_categories[0]
        for set_of_categories in self.sets_of_categories[1::]:
            intersection = [element for element in set_of_categories if element in intersection]
        return intersection

    def is_same_sets(self):
        return all([set(self.elements) == set(set_of_categories) for set_of_categories in self.sets_of_categories])
