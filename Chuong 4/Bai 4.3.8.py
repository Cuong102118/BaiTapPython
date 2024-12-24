n = int(input())
mt = []
for _ in range(n):
    row = list(map(int,input().split()))
    mt.append(row)
ktTamGiacTren = True
ktTamGiacDuoi = True
for i in range(n):
    for j in range(i):
        if mt[i][j] != 0:
            ktTamGiacTren = False
            break
    if not ktTamGiacTren:
        break
for i in range(n):
    for j in range(i + 1, n):
        if mt[i][j] != 0:
            ktTamGiacDuoi = False
            break
    if not ktTamGiacDuoi:
        break
if ktTamGiacTren:
    print("UPPER TRIANGLE")
elif ktTamGiacDuoi:
    print("LOWER TRIANGLE")
else:
    print("NONE")