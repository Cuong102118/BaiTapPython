import math
ep, x = map(float,input().split())

if 0 < ep < 1:
    S = 0
    n = 0
    while math.fabs(x**n / math.factorial(n)) >= ep:
        n = n + 1
        S = S + x**n / math.factorial(n) 
    print(S)
else:
    print("Sai dữ liệu.")
