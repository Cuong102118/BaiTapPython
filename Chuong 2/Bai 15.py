import math
a = float(input())
if 0 < a < 0.01:
    S = 0
    n = 0
    while (2 * n + 1)**(-1) > a:
        n = n + 1
        S = S + (math.factorial(2 * n + 1))**(-1)
    print(S)
else:
    print("Sai dữ liệu.")
