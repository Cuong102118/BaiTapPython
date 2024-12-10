def BTPBacNhat(a, b):
    if a == 0:
        if b > 0:
            return "VSN"
        else:
            return "VN"
    else:
        nghiem = -b / a
        if a > 0:
            return "x > {0:.2f}".format(nghiem)
        else:
            return "x < {0:.2f}".format(nghiem)

a, b = map(float,input().split())
kq = BTPBacNhat(a, b)
print(kq)