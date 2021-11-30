fibonacci_series = [1, 2]
i = 2
while True:
    fibonacci_series.append(fibonacci_series[i-1]+fibonacci_series[i-2])
    if fibonacci_series[i] > 4000000:
        break
    i += 1
# print(fibonacci_series[-1])
fibonacci_series = fibonacci_series[:-1]
# print(fibonacci_series[-1])

even_value_sum = 0
for i in fibonacci_series:
    if i % 2 == 0:
        even_value_sum += i
print(even_value_sum)

