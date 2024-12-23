def TimKiem(s, n, x):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if x == s[m]: return "YES"
        else:
            if x > s[m]: l = m + 1
            else : r = m - 1
    return "NO"
n, k = map(int,input().split())
s = list(map(int, input().split()))
s1 = list(map(int,input().split()))
for i in range(k):
    print(TimKiem(s,n,s1[i]))