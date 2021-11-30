
for a in range(1,1000):
    for b in range(a + 1, 1000):
        if a + b + (a*a + b*b)**0.5 - 1000 == 0:
            A = a
            B = b

print(A*B*(A*A+B*B)**0.5)