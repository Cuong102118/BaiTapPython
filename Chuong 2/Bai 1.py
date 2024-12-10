def PTBacNhat(a, b):
    if a == 0:
        if b == 0:
            return "VSN."
        else:
            return "VN."
    else:
        x = -b / a
        return "{0}".format(x)

a, b = map(float,input().split())
kq = PTBacNhat(a, b)
print(kq)
