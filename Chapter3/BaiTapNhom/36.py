a = input("Nhap chu cai ban muon: ")

if a in ('u', 'e', 'o', 'a', 'i'):
    print("Chu cai", a, "la nguyen am")
elif (a == "y"):
    print("Chu cai nay doi khi la nguyen am va doi khi la phu am")
else:
    print("Chu cai", a, "la phu am")
