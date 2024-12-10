import math

def PTBacHai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "VSN."
            else:
                return "VN."
        else:
            x = -c / b
            return "{0}".format(x)
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return "{0} {1}".format(x1,x2)
        elif delta == 0:
            x = -b / (2 * a)
            return "{0}".format(x)
        else:
            return "VN"
        
a, b, c = map(float,input().split())
kq = PTBacHai(a, b, c)
print(kq)
