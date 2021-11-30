
def is_prime(n:int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_list = []
i = 2
while True:
    if is_prime(i):
        prime_list.append(i)
        # print(i)
    if len(prime_list) == 10001:
        break
    i += 1
print(prime_list[-1])



