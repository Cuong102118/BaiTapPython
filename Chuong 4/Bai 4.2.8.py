def ChuanHoa(s):
    s = s.strip()
    words = s.split(" ")
    kq = [word.capitalize() for word in words if word != ""]
    return " ".join(kq)
s = input()
print(ChuanHoa(s))