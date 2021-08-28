def Nhap():
    print('Nhap mot so nguyen:')
    n = int(input('n='))
    return n


def Tinh(n):
    S = 0
    for x in range(1, n+1):
        S = S+x
    return S


def InKQ(n):
    
    print('Tong cua ', n, ' so nguyen duong dau tien=', kq, sep='')


n = Nhap()
kq = Tinh(n)
InKQ(kq)
