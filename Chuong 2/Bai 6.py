def TinhTong(n):
    S = 0
    for i in range(1, n + 1):
        S = S + i
    return S * 3

n = int(input("Nhập n: "))
if n > 0:
    kq = TinhTong(n)
    print("Tổng S = {0}".format(kq))
else:
    print("n phải là số nguyên dương.")
