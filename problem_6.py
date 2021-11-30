top_range = 100
squares_sum = 0
naturals_sum = 0
for i in range(1,top_range + 1):
    squares_sum += i*i
    naturals_sum += i
difference = naturals_sum * naturals_sum - squares_sum
print(difference)

