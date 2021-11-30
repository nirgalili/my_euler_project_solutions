NUMBER = 600851475143
#
#
# def is_prime_factor(number:int):
#
#     number_to_divide_by = number - 1
#     while number_to_divide_by > 1:
#         if number % number_to_divide_by == 0:
#             return False
#         number_to_divide_by -= 1
#     return True

def is_prime(n:int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


for i in range(2, NUMBER + 1):
    if is_prime(i) and NUMBER % i == 0:
        print(i)

