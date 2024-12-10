def TongCacChuSo(n):
    S = 0
    while n != 0:
        d = n % 10
        S = S + d
        n = n // 10
    return S
n = int(input())
print(TongCacChuSo(n))