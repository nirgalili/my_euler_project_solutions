def next_number_for_even(number: int) -> int:
    return number/2


def next_number_for_odd(number: int) -> int:
    return number*3+1


def next_number(number_not_know_even_or_odd: int) -> int:
    if number_not_know_even_or_odd % 2 == 0:
        return next_number_for_even(number_not_know_even_or_odd)
    else:
        return next_number_for_odd(number_not_know_even_or_odd)


def produce_collatz_sequence(starting_number: int) -> list:
    current_number_in_list = starting_number
    new_collatz_sequence = [starting_number]
    while current_number_in_list != 1:
        current_number_in_list = next_number(current_number_in_list)
        new_collatz_sequence.append(int(current_number_in_list))
    return new_collatz_sequence

# collatz_sequence = produce_collatz_sequence(13)
# print(collatz_sequence)

top = 1000000
# chain = []
max_chain_length = 0
for i in range(top-1, 2, -1):
    chain = produce_collatz_sequence(i)
    chain_length = len(chain)
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        starting_number = i
print(max_chain_length, starting_number)

