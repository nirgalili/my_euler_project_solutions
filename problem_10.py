def is_prime(n:int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
sum_of_primes = 0
top = 2000000
for i in range(2, top):
    if is_prime(i):
        sum_of_primes += i
print(sum_of_primes)