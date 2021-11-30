from matrix_manipulations import MatrixManipulation
from node_manipulations import NodeManipulation
from itertools import product

ROWS = 21
COLUMNS = 21

matrix = MatrixManipulation(ROWS, COLUMNS)
node = NodeManipulation()
shape = matrix.score_matrix.shape
initial_index = (0, 0)

for row, column in product(range(ROWS), range(COLUMNS)):
    # print(node.index)
    node.update_node_score(matrix.score_matrix)
    matrix.update_score_matrix(node.index, node.score)
    next_index = node.get_next_index(shape)

    node.index = next_index


paths = matrix.score_matrix.max()
# print("The score matrix is:")
int_array = matrix.score_matrix.astype(int)
# print(int_array)
# print("----------------------")
# print(matrix.score_matrix)
# print("----------------------")
print("There are", int(paths), "possible paths.")
# int_array_list = int_array.tolist()
# print(int_array_list)

# print(paths in matrix.score_matrix)









