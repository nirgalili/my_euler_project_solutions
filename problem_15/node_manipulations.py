class NodeManipulation:

    def __init__(self):
        self.index = (0, 0)
        self.score = 1

    def does_have_single_donor(self) -> bool:
        if self.index[0] == 0 or self.index[1] == 0:
            return True
        else:
            return False

    def update_node_score(self, score_matrix):
        if not self.does_have_single_donor():
            left_score = score_matrix[(self.index[0], self.index[1]-1)]
            upper_score = score_matrix[(self.index[0]-1, self.index[1])]
            self.score = left_score+upper_score
        else:
            self.score = 1

    def get_next_index(self, matrix_shape) -> tuple:
        num_rows, num_cols = matrix_shape
        if self.index[1] == num_cols-1:
            new_index = (self.index[0]+1, 0)
        else:
            new_index = (self.index[0], self.index[1]+1)
        return new_index


