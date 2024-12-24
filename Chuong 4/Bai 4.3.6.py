n = int(input())
mt = []
for _ in range(n):
    row = list(map(int,input().split()))
    mt.append(row)
kt = 1
for i in range(n):
    for j in range(n):
        if mt[i][j] == mt[j][i]:
            kt = 1
        else:
            kt = 0
if kt == 1:
    print("YES")
else:
    print("NO")