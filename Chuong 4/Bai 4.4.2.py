class Sach:
    def __init__(self, ten = "", sotrang = 0, giatien = 0):
        self.ten = ten
        self.sotrang = sotrang
        self.giatien = giatien
        self.tb = 0
    def nhap(self):
        chuoi = input()
        s = chuoi.split()
        self.ten = s[0]
        self.sotrang = int(s[1])
        self.giatien = int(s[2])
        self.tb = round(self.giatien / self.sotrang, 2)
    def xuat(self):
        print(self.ten, self.sotrang, self.giatien, self.tb)
n = int(input())
books = []
for i in range(n):
    book = Sach()
    book.nhap()
    books.append(book)
books.sort(key = lambda x:x.tb)
with open('ketqua.txt', 'w', encoding='utf-8') as file:
    for b in books:
        file.write(f"{b.ten} {b.sotrang} {b.giatien} {b.tb}\n")