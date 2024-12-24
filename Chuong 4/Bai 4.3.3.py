m, n = map(int, input().split())  # Kích thước ma trận mt1 (m x n)
k, p = map(int, input().split())  # Kích thước ma trận mt2 (k x p)

# Đọc ma trận mt1 (m x n)
mt1 = []
for _ in range(m):
    row1 = list(map(int, input().split()))
    mt1.append(row1)

# Đọc ma trận mt2 (k x p)
mt2 = []
for _ in range(k):
    row2 = list(map(int, input().split()))
    mt2.append(row2)

# Kiểm tra điều kiện nhân ma trận
if n != k:
    print("Khong the nhan ma tran")
else:
    # Khởi tạo ma trận kết quả mt3 (m x p)
    mt3 = [[0] * p for _ in range(m)]
    
    # Nhân ma trận
    for i in range(m):
        for j in range(p):
            for l in range(n):
                mt3[i][j] += mt1[i][l] * mt2[l][j]
    
    # In kết quả
    for row in mt3:
        print(' '.join(map(str, row)))
