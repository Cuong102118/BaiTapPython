m, n = map(int,input().split())
mt = []
for _ in range(m):
    row = list(map(int,input().split()))
    mt.append(row)
S = 0
for i in range(m):
    for j in range(n):
        S = S + mt[i][j]
tb = S / (m * n)
print("{0:.2}".format(tb))
for i in range(m):
    for j in range(n):
        if mt[i][j] > tb:
            print("{0} {1} {2}".format(mt[i][j],i + 1,j + 1))