def TinhTong(x, n):
    S = 0
    for i in range(1, n + 1):
        S += x**i
    return S

x = float(input())
n = int(input())
if n > 0:
    kq = TinhTong(x, n)
    print("{0}".format(kq))
else:
    print("n phải là số nguyên dương.")
