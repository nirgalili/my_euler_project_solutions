class Node:
    def __init__(self, original_value, row, location_in_list):
        self.value = original_value
        self.row = row
        self.location_in_list = location_in_list
        self.parents_list = None
        self.score = None

    def get_node_score_parents(self, score_triangle_lists) -> list:
        if self.row == 0: # first row has no parents
            temp_parents_list = [0]
        elif self.row == 1: # second row has single parent
            temp_parents_list = score_triangle_lists[0]
        elif self.location_in_list == 0:
            temp_parents_list = [score_triangle_lists[self.row-1][0]]
        elif self.location_in_list == len(score_triangle_lists[self.row])-1:
            temp_parents_list = [score_triangle_lists[self.row-1][self.location_in_list-1]]
        else:
            mother = score_triangle_lists[self.row-1][self.location_in_list-1]
            father = score_triangle_lists[self.row-1][self.location_in_list]
            temp_parents_list = [mother, father]
        self.parents_list = temp_parents_list
        return temp_parents_list

    def calculate_new_score(self):
        bigger_parent = max(self.parents_list)
        temp_new_score = bigger_parent+self.value
        self.score = temp_new_score
        return temp_new_score


