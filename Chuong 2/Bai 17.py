import math
a, b, c = map(float,input().split())
S = 0
C = 0
if a + b > c and a + c > b and b + c > a:
    C = a + b + c
    p = C / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("{0} {1}".format(C,S))
else:
    print("Không tạo thành tam giác")