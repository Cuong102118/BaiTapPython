def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    f1 = 1
    f2 = 1
    for i in range(3, n + 1):
        tg = f2
        f2 = f1 + f2
        f1 = tg
    return f2
def InDayVaTinhTong(n):
    luu = []
    for i in range(1, n + 1):
        luu.append(fibonacci(i))
        S = sum(luu)
    print("Dãy fibonacci: {0}".format(' '.join(map(str,luu))))
    print("Tổng dãy là: {0}".format(S))
n = int(input())
InDayVaTinhTong(n)