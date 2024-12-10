def UCLN(a,b):
    while b != 0:
        d = a % b
        a = b
        b = d
    return a
def BCNN(a,b):
    return (a * b) // UCLN(a,b)
a, b = map(int,input().split())
print(BCNN(a,b))