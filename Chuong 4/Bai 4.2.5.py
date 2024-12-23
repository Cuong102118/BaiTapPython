s = input()
words = list(s)
CH = 0
CT = 0
CS = 0
for i in words:
    if i.isupper():
        CH = CH + 1
    elif i.islower():
        CT = CT + 1
    elif i.isdigit():
        CS = CS + 1
print("Hoa: {0}, Thuong: {1}, So: {2}".format(CH,CT,CS))