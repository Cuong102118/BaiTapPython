m, n = map(int,input().split())
mt = []
for _ in range(m):
    row = list(map(int,input().split()))
    mt.append(row)
S = 0
for i in range(m):
    S = sum(mt[i])
    if S % 7 == 0:
        print(i + 1)