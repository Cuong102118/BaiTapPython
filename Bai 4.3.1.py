m, n, k = map(int,input().split())
mt = []
for i in range(m):
    row = list(map(int, input().split()))
    mt.append(row)
C = 0
for i in range(m):
    for j in range(n):
        if mt[i][j] == k:
            C = C + 1
print(C)