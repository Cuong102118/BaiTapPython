class SinhVien:
    def __init__(self, ten = "", ma = 0, d1 = 0.0, d2 = 0.0, d3 = 0.0):
        self.ten = ten
        self.ma = ma
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tb = 0.0
    def nhap(self):
        chuoi = input()
        s = chuoi.split(' ')
        self.ten = s[0]
        self.ma = int(s[1])
        self.d1 = float(s[2])
        self.d2 = float(s[3])
        self.d3 = float(s[4])
        self.tb = (self.d1 + self.d2 + self.d3) / 3
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.ma,self.ten,self.d1,self.d1,self.d3,self.tb))
n = int(input())
SinhViens = []
for i in range(n):
    SV = SinhVien()
    SV.nhap()
    if (SV.d1 < 4 and SV.d2 < 4) or (SV.d1 < 4 and SV.d3 < 4) or (SV.d2 < 4 and SV.d3 < 4):
        SinhViens.append(SV)
print("Danh sach sinh vien hoc lai")
for i in SinhViens:
    i.xuat()
print("Danh sach nay co {0} sinh vien phai hoc lai".format(len(SinhViens)))