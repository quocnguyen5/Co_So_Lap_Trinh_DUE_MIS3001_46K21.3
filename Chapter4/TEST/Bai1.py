def nhap():
    n = int(input('n='))
    return n


def LaSoDuong(x):
    if x >= 0 and x % 2 == 0: 
        return 1
    else:
        return 0


def Xuly(n):
    dem=0
    for i in range(1, n+1):
        x = int(input())
        if LaSoDuong(x)==1:
            dem+=1
    return dem


def InKQ(kq):
    print('ket qua la', kq)


n = nhap()
kq=Xuly(n)
InKQ(kq)

