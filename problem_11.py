import numpy as np

numbers = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# print(numbers)

numbers = numbers.split('\n')
# print(numbers)

def list_items_str_to_int(list_of_strings:list)->list:
    new_list_of_int = []
    for string in list_of_strings:
        # print(string)
        new_list_of_int.append(int(string))
        # print(new_list_of_int)
    return new_list_of_int


def create_list(string_with_spaces:str) ->list:
    new_list_of_str = string_with_spaces.split(" ")
    # print(new_list_of_str)
    new_list = list_items_str_to_int(new_list_of_str)
    return new_list

new_list_of_lists = []
for row_of_numbers in numbers:
    new_row_of_numbers = create_list(row_of_numbers)
    new_list_of_lists.append(new_row_of_numbers)
# print(new_list_of_lists)

A = np.array(new_list_of_lists)
# print(A)

def multiplyList(myList:list)->int:
    result = 1
    for x in myList:
        print(x)
        print(type(x))
        if type(x) != int:
            x = int(x)
        result = result * x
    return result

tuple_list = []
for i in range(20):
    temp_row_list = []
    for j in range(20):
        new_tuple = (i, j)
        temp_row_list.append(new_tuple)
    tuple_list.append(temp_row_list)
# print(tuple_list)
B = np.array(tuple_list, dtype="i,i")
# print(B)

print("-------------------------------------------------------")

row_numbers = new_list_of_lists[0]
row_tuples = tuple_list[0]


def create_list_of_numbers_tuples_and_multiply(row_numbers:list, row_tuples:list)->list:

    if len(row_numbers) - 4 >= 0:
        list_of_numbers_tuples_and_multiply = []
        for i in range(len(row_numbers) - 4 + 1):
            temp_list_numbers = []
            temp_list_tuples = []
            # list_of_numbers_tuples_and_multiply = []
            result = 1
            for j in range(i, i + 4):
                temp_list_numbers.append(row_numbers[j])
                temp_list_tuples.append(row_tuples[j])
                result = result * row_numbers[j]

            temp_multiply = result
            temp_list_of_numbers_tuples_and_multiply_row = [temp_list_tuples, temp_list_numbers, temp_multiply]
            list_of_numbers_tuples_and_multiply.append(temp_list_of_numbers_tuples_and_multiply_row)
        # print(list_of_numbers_tuples_and_multiply)
        return list_of_numbers_tuples_and_multiply
    else:
        return [0, 0, 0]


# new_list = create_list_of_numbers_tuples_and_multiply(row_numbers, row_tuples)
# print(new_list)

print("--------------------------horizontal-----------------------------")

# horizontal
horizontal_list = []
for i in range(20):
    numbers_list = A[i, :]
    tuples_list = B[i, :]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    horizontal_list = horizontal_list + new_list
print(horizontal_list)

print("---------------------------vertical----------------------------")

# vertical
vertical_list = []
for i in range(20):

    numbers_list = A[:, i]
    tuples_list = B[:, i]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    vertical_list = vertical_list + new_list
print(vertical_list)

print("---------------------------diagonal regular----------------------------")

# diagonal regular
numbers = []
tuples = []
for i in range(4-1, 20):
    # row = i
    temp_numbers = []
    temp_tuples = []
    new_row = i
    for j in range(i+1):

        new_column = i - new_row
        temp_numbers.append(A[new_row, new_column])
        temp_tuples.append(B[new_row, new_column])
        new_row -= 1
    # print(numbers_list)
    numbers.append(temp_numbers)
    tuples.append(temp_tuples)
# print(numbers)
# print(tuples)

diagonal_list = []
for i in range(len(numbers)):

    numbers_list = numbers[i]
    tuples_list = tuples[i]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    diagonal_list = diagonal_list + new_list
print(diagonal_list)
diagonal_regular = diagonal_list

print("---------------------------diagonal flipped----------------------------")

A_flipped = np.flip(A, axis=1)
B_flipped = np.flip(B, axis=1)

# A_flip_and_transpose = A_flipped.transpose()
# B_flip_and_transpose = B_flipped.transpose()

# diagonal flipped
numbers = []
tuples = []
for i in range(4-1, 20):
    # row = i
    temp_numbers = []
    temp_tuples = []
    new_row = i
    for j in range(i+1):

        new_column = i - new_row
        temp_numbers.append(A_flipped[new_row, new_column])
        temp_tuples.append(B_flipped[new_row, new_column])
        new_row -= 1
    # print(numbers_list)
    numbers.append(temp_numbers)
    tuples.append(temp_tuples)
# print(numbers)
# print(tuples)

diagonal_list = []
for i in range(len(numbers)):

    numbers_list = numbers[i]
    tuples_list = tuples[i]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    diagonal_list = diagonal_list + new_list
print(diagonal_list)
diagonal_flipped = diagonal_list



print("---------------------------diagonal regular upside down----------------------------")

A_upside_down = np.flip(A, axis=0)
B_upside_down = np.flip(B, axis=0)

# diagonal regular upside down
numbers = []
tuples = []
for i in range(4-1, 20):
    # row = i
    temp_numbers = []
    temp_tuples = []
    new_row = i
    for j in range(i+1):

        new_column = i - new_row
        temp_numbers.append(A_upside_down[new_row, new_column])
        temp_tuples.append(B_upside_down[new_row, new_column])
        new_row -= 1
    # print(numbers_list)
    numbers.append(temp_numbers)
    tuples.append(temp_tuples)
# print(numbers)
# print(tuples)

diagonal_list = []
for i in range(len(numbers)):

    numbers_list = numbers[i]
    tuples_list = tuples[i]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    diagonal_list = diagonal_list + new_list
print(diagonal_list)
diagonal_regular_upside_down = diagonal_list

# print(A_flipped)

# diagonal left to right till middle

print("---------------------------diagonal flipped upside down----------------------------")

A_flipped = np.flip(A, axis=1)
B_flipped = np.flip(B, axis=1)

A_flipped_upside_down = np.flip(A_flipped, axis=0)
B_flipped_upside_down = np.flip(B_flipped, axis=0)

# diagonal flipped upside down
numbers = []
tuples = []
for i in range(4-1, 20):
    # row = i
    temp_numbers = []
    temp_tuples = []
    new_row = i
    for j in range(i+1):

        new_column = i - new_row
        temp_numbers.append(A_flipped_upside_down[new_row, new_column])
        temp_tuples.append(B_flipped_upside_down[new_row, new_column])
        new_row -= 1
    # print(numbers_list)
    numbers.append(temp_numbers)
    tuples.append(temp_tuples)
# print(numbers)
# print(tuples)

diagonal_list = []
for i in range(len(numbers)):

    numbers_list = numbers[i]
    tuples_list = tuples[i]
    new_list = create_list_of_numbers_tuples_and_multiply(numbers_list, tuples_list)
    diagonal_list = diagonal_list + new_list
print(diagonal_list)
diagonal_flipped_upside_down = diagonal_list

#max_in_horizontal
multiply_list = []
for i in horizontal_list:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

#max_in_vertical
multiply_list = []
for i in vertical_list:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

#max_in_diagonal_regular
multiply_list = []
for i in diagonal_regular:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

#max_in_diagonal_flipped
multiply_list = []
for i in diagonal_flipped:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

#max_in_diagonal_regular_upside_down
multiply_list = []
for i in diagonal_regular_upside_down:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

#max_in_diagonal_flipped_upside_down
multiply_list = []
for i in diagonal_flipped_upside_down:
    multiply_list.append(i[2])
    max_multiply = max(multiply_list)
print(max_multiply)

# the max is in diagonal flipped ant it is 70600674

