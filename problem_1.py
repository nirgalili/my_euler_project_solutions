x = 1000
# multiples = []
multiples_sum = 0
for i in range (3, x):
    if i % 3 == 0 or i % 5 == 0:
        # multiples.append(i)
        multiples_sum += i

# print(multiples)
print(multiples_sum)