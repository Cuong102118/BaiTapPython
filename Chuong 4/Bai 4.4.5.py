class NhanVien:
    def __init__(self, ma = 0, ten = "", hsl = 0.0, phucap = 0):
        self.ma = ma
        self.ten =ten
        self.hsll = hsl
        self.phucap = phucap
        self.luong = 0.0
    def nhap(self):
        chuoi = input()
        s = chuoi.split()
        self.ten = s[0]
        self.ma = int(s[1])
        self.hsl = float(s[2])
        self.phucap = int(s[3])
        self.luong = (self.hsl * 2000000) + self.phucap
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma,self.ten,self.hsl,self.phucap,self.luong))
n = int(input())
NhanViens = []
for i in range(n):
    NV = NhanVien()
    NV.nhap()
    NhanViens.append(NV)
NhanViens.sort(reverse=True,key=lambda x:x.luong)
print("Danh sach nhan vien da sap xep: {0}".format(n))
for i in NhanViens:
    i.xuat()