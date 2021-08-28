a = float(input("Do dai canh thu nhat:"))
b = float(input("Do dai canh thu hai:"))
c = float(input("Do dai canh thu ba:"))
if a == b and b == c and a == c:
    print("Tam giac deu")
elif a == b or a == c or b == c:
    print("Tam giac can")
else:
    print("Tam giac vo huong")
