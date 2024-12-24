n = int(input())
mt = []
for _ in range(n):
    row = list(map(int,input().split()))
    mt.append(row)
S1 = 0
S2 = 0
for i in range(n):
    S1 = S1 + mt[i][i]
    S2 = S2 + mt[i][n - i - 1]
print(S1, S2)