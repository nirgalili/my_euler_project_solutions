top_range = 20


def is_divide_by_all(n):
    for i in range(top_range, 0, -1):
        if n % i != 0:
            return False
    return True

# print(is_divide_by_all(2520))

i = 2520
while True:
    # print(i)
    if is_divide_by_all(i):
        break
    i += 2520
print(i)