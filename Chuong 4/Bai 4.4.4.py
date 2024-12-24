class Nhanvien:
    def __init__(self, ma = 0, ten = "", hsl = 0, phucap = 0):
        self.ma = ma
        self.ten = ten
        self.hsl = hsl
        self.phucap =phucap
        self.luong = 0
    def nhap(self):
        chuoi = input()
        s = chuoi.split(' ')
        self.ma = int(s[0])
        self.ten = s[1]
        self.hsl = float(s[2])
        self.phucap = int(s[3])
        self.luong = (self.hsl * 2000000) + self.phucap
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma,self.ten,self.hsl,self.phucap,self.luong))
n = int(input())
Nhanviens = []
for i in range(n):
    NV = Nhanvien()
    NV.nhap()
    Nhanviens.append(NV)
Nhanviens.sort(key = lambda x:x.luong)
print("Nhan vien co luong thap nhat")
Nhanviens[0].xuat()