import math

def triangle_number_create(number: int, previous_triangle_number: int) -> int:
    # triangle = 0
    # for i in range(1, number+1):
    #     triangle += i
    # return triangle
    new_triangle_number = number + previous_triangle_number
    # print(new_triangle_number)
    return new_triangle_number






def countDivisors(n):
    cnt = 0
    for i in range(1, (int(n**0.5) + 1)):
        if (n % i == 0):

            # If divisors are equal,
            # count only one if i is the square root of n
            if (n / i == i):
                cnt = cnt + 1
            else:  # Otherwise count both because the number have a number to multiple that is larger than the square root
                cnt = cnt + 2

    return cnt

# def factors_count(number: int,) -> int:
#     count_factors = 0
#     for i in range(1, number+1):
#         if number % i == 0:
#             count_factors += 1
#     return count_factors

less_then_500_divisors = True
n = 1
triangle_number = 0

while less_then_500_divisors:
    # print(n)
    triangle_number = triangle_number_create(n, triangle_number)
    count = countDivisors(triangle_number)
    if count > 500:
        print(triangle_number)
        less_then_500_divisors = False
    n = n+1

# divisor_count = 0
#
# n = 1
# while divisor_count < 500:
#     divisor_count = factors_count(n)
#     print(divisor_count)
#     n += 1



# print(factors_count(100000000))

# print(triangle_number_create(6))