import math
n = int(input())
x = float(input())
S = 0
for _ in range(1, n + 1):
    S = math.sqrt(x + S)
print(S + 1)