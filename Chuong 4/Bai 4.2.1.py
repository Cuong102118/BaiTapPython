def ChuanHoaChuoi(s):
    s = s.strip()
    s = s.lower()
    s = ' '.join(s.split())
    s = s.capitalize()
    return s
s = input()
kq = ChuanHoaChuoi(s)
print(kq)