def ThapPhanSangThapLucPhan(n):
    if n == 0:
        return "0"
    ThapLucPhan = ""
    KyTuThapLucPhan = "0123456789ABCDEF"
    while n > 0:
        ThapLucPhan = KyTuThapLucPhan[n % 16] + ThapLucPhan
        n = n // 16
    return ThapLucPhan
n = int(input())
print(ThapPhanSangThapLucPhan(n))