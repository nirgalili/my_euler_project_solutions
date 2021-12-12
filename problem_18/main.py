from triangle import Triangle
from nodes import Node
from problem_18_suplementary import new_list_of_lists

# if __name == "__main__"

# print(new_list_of_lists)
ORIGINAL_TRIANGLE = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]

original_triangle_rows = len(new_list_of_lists)
# print(original_triangle_rows)

# print("--------------------")

triangle = Triangle(original_triangle_rows)

for row in range(triangle.number_of_rows):
    # print("========")
    row_length = len(triangle.triangle_of_scores[row])
    # print(row_length)
    # print("=-=-=-=")
    original_row = new_list_of_lists[row]
    for location in range(row_length):
        # print("-+-+-+-+-+-+-+-+-")
        # print(location)
        # print(original_row)
        # print(original_row[location])

        node = Node(original_value=original_row[location], row=row, location_in_list=location)
        # print(node.location_in_list)
        # print(triangle.triangle_of_scores)
        parents_list = node.get_node_score_parents(triangle.triangle_of_scores)
        # print(parents_list)
        new_score = node.calculate_new_score()
        # print(new_score)
        new_triangle_of_scores =  triangle.update_triangle_score(new_score=new_score, row=row, location_in_list=location)
        # print(new_triangle_of_scores)

    max_score = max(new_triangle_of_scores[-1])
    # print(max_score)

print("The Maximum path sum is:", max_score)
