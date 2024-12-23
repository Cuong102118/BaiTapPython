def DemKyTu(s):
    luuKyTu = {}
    for char in s:
        if char in luuKyTu:
            luuKyTu[char] += 1
        else:
            luuKyTu[char] = 1
    return luuKyTu
s = input()
kq = DemKyTu(s)
ds = []
for KyTu, SoLan in kq.items():
    ds.append("{0}: {1}".format(KyTu,SoLan))
print(", ".join(ds))