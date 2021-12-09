from triangle import Triangle
from nodes import Node


def test_triangle():
    list_length = 3
    triangle = Triangle(list_length)
    new_list = triangle.create_list_of_zeroes(list_length)
    print(new_list)
    assert len(new_list) == list_length


def test_node_get_parents_4th_row_2_parents():
    triangle_lists = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    score_triangle_lists_for_4th_row = [
        [1],
        [3, 4],
        [7, 9, 10],
        [0, 0, 0, 0]
    ]
    row = 3  # 1st row is 0
    location_in_list = 2  # 3rd place in the row
    original_value = triangle_lists[row][location_in_list]  # should be 9
    node = Node(original_value=original_value, row=row, location_in_list=location_in_list)
    parents_score = node.get_node_score_parents(score_triangle_lists_for_4th_row)
    print(parents_score)
    assert parents_score == [9, 10]

def test_node_get_parents_4th_row_1_parent_first():
    triangle_lists = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    score_triangle_lists_for_4th_row = [
        [1],
        [3, 4],
        [7, 9, 10],
        [0, 0, 0, 0]
    ]
    row = 3  # 1st row is 0
    location_in_list = 0  # 1st place in the row
    original_value = triangle_lists[row][location_in_list]  # should be 7
    node = Node(original_value=original_value, row=row, location_in_list=location_in_list)
    parents_score = node.get_node_score_parents(score_triangle_lists_for_4th_row)
    print(parents_score)
    assert parents_score == [7]

def test_node_get_parents_4th_row_1_parent_last():
    triangle_lists = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    score_triangle_lists_for_4th_row = [
        [1],
        [3, 4],
        [7, 9, 10],
        [0, 0, 0, 0]
    ]
    row = 3  # 1st row is 0
    location_in_list = 3  # last place in the row
    original_value = triangle_lists[row][location_in_list]  # should be 10
    node = Node(original_value=original_value, row=row, location_in_list=location_in_list)
    parents_score = node.get_node_score_parents(score_triangle_lists_for_4th_row)
    print(parents_score)
    assert parents_score == [10]

def test_node_new_scoe():
    triangle_lists = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    score_triangle_lists_for_4th_row = [
        [1],
        [3, 4],
        [7, 9, 10],
        [0, 0, 0, 0]
    ]
    row = 3  # 1st row is 0
    location_in_list = 2  # 2nd place in the row
    original_value = triangle_lists[row][location_in_list]  # should be 9
    node = Node(original_value=original_value, row=row, location_in_list=location_in_list)
    parents_score = node.get_node_score_parents(score_triangle_lists_for_4th_row)
    print(parents_score)
    new_score = node.calculate_new_score()
    print(new_score)

