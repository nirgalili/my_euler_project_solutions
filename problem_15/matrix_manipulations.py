import numpy as np


class MatrixManipulation:

    def __init__(self, rows: int, columns: int):
        self.max_node = (rows-1, columns-1)
        self.score_matrix = np.zeros((rows, columns))
        self.score_matrix[0, 0] = 1

    def update_score_matrix(self, index_to_update: tuple, new_score: int):
        self.score_matrix[index_to_update[0], index_to_update[1]] = new_score

