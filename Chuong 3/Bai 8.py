def ThapPhanSangNhiPhan(n):
    if n == 0:
        return "0"
    NhiPhan = ""
    while n > 0:
        NhiPhan = str(n % 2) + NhiPhan
        n = n // 2
    return NhiPhan
n = int(input())
print(ThapPhanSangNhiPhan(n))