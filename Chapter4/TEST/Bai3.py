

def nhap():
    global n
    n = int(input('n='))
    return n


def LaNST(n):
    global i
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def InSoNguyenTo(n):
    for i in range(2, n+1):
        if LaNST(i):
            print(i, end=' ')


nhap()
InSoNguyenTo(n)
