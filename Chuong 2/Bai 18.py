import math
x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
x3, y3 = map(float,input().split())

d1 = math.sqrt((x1 - x2)**2 - (y1 - y2)**2)
d2 = math.sqrt((x1 - x3)**2 - (y1 - y3)**2)
d3 = math.sqrt((x2 - x3)**2 - (y2 - y3)**2)

S = 0
C = 0
if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
    C = d1 + d2 + d3
    p = C / 2
    S = math.sqrt(p*(p - d1) * (p - d2) * (p - d3))
    print(S)
else:
    print("Ba điểm không tạo thành tam giác.")