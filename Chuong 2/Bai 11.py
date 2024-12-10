import math
def tinh_tong(n):
    S = 0
    for i in range(1, n + 1):
        S += math.factorial(i)
    return S

n = int(input())
if n > 0:
    kq = tinh_tong(n)
    print("{0}".format(kq))
else:
    print("n phải là số nguyên dương.")
