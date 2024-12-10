import math

def TinhTong(n):
    S = 0
    for i in range(n + 1):
        SoLe = 2 * i + 1
        S += (math.factorial(SoLe))**(-1)
    return S

n = int(input())
if n >= 0:
    kq = TinhTong(n)
    print("{0}".format(kq))
else:
    print("n phải là số nguyên không âm.")
