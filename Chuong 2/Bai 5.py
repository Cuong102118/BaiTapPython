a1, b1, c1 = map(float,input().split())
a2, b2, c2 = map(float,input().split())

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if D == 0:
    if Dx == Dy == 0:
        print("VSN")
    else:
        print("VN")
else:
    x = Dx / D
    y = Dy / D
    print("He phuong trinh co nghiem: {0} {1}".format(x,y))