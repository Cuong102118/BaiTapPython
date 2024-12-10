import math

def PTBacHai(a, b, c):
    if a == 0:
        return "Hệ số a phải khác 0."
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return "Phương trình có hai nghiệm phân biệt: x1 = {0}, x2 = {1}".format(x1,x2)
    elif delta == 0:
        x = -b / (2 * a)
        return "Phương trình có nghiệm kép: x = {0}".format(x)
    else:
        return "Phương trình vô nghiệm."

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
kq = PTBacHai(a, b, c)
print(kq)
