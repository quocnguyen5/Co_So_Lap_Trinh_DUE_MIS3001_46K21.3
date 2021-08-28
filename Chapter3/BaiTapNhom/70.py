s = str(input("Nhap tin nhan can ma hoa:"))
for i in s:
    if i == "x":
        print("a", end="")
    elif i == "X":
        print("A", end="")
    elif i == "y":
        print("b", end="")
    elif i == "Y":
        print("B", end="")
    elif i == "z":
        print("c", end="")
    elif i == "Z":
        print("C", end="")
    elif (i >= "a" and i <= "w") or (i >= "A" and i <= "W"):
        print("%c" % (ord(i)+3), end="")
# https://likegeeks.com/python-caesar-cipher/
