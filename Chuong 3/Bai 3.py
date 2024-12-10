def SoHoanHao(n):
    S = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            S = S + i
    if S == n:
        return True
    else:
        return False
a, b = map(int,input().split())
for i in range(a, b + 1):
    if SoHoanHao(i) == True:
        print(i, end = " ")
