def UCLN(a,b):
    while b != 0:
        d = a % b
        a = b
        b = d
    return a
a, b = map(int,input().split())
print(UCLN(a,b))