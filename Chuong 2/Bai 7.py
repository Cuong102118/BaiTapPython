def TinhTong(n):
    S = 0
    for i in range(1, n + 1):
        S = S + (i * (i + 1))**(-1)
    return S

n = int(input())
if n > 0:
    kq = TinhTong(n)
    print("{0:.6f}".format(kq))
else:
    print("n phải là số nguyên dương.")
