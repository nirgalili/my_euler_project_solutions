
def flip_string(numbers_string: str) -> str:
    return numbers_string[::-1]


def is_palindrome(number: int) -> bool:
    number_str = str(number)
    if len(number_str) % 2 == 0:
        half_string_length = int(len(number_str)/2)
        # print(half_string_length)
        # print(type(half_string_length))
        second_half_string = number_str[half_string_length:]
        flipped_half_string = flip_string(number_str[:half_string_length])
        if second_half_string == flipped_half_string:
            return True
    else:
        half_string_length = int(len(number_str[:-1])/2)
        second_half_string = number_str[half_string_length+1:]
        flipped_half_string = flip_string(number_str[:half_string_length])
        if second_half_string == flipped_half_string:
            return True
    return False


top = 999
palindrome_max = 0
for i in range(top, 1, -1):
    for j in range(i, 1, -1):
        multiply = i*j
        if is_palindrome(multiply):
            if multiply > palindrome_max:
                palindrome_max = multiply


print(palindrome_max)


