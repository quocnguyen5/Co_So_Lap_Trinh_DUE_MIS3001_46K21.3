

def nhap():
    global n
    n = int(input('n='))
    return n


def LaNST(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        return True
    return False


def InKQ(x):
    if x is True:
        print(n, 'la SNT')
    else:
        print(n, 'khong la SNT')


nhap()
kq = LaNST(n)
InKQ(kq)
