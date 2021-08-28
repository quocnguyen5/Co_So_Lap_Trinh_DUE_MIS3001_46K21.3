def LaSoNguyenTo(x):
    if x < 2:
        return False
    if x in (2, 3, 5):
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    for i in range(5, int(x ** (1 / 2)), 2):
        if x % i == 0:
            return False
    return True


def SoHopLe(x):
    if x <= 1:
        return True
    return False


def NhapVaDem():
    dem = 0
    print('Nhap day so:')
    while True:
        x = int(input())
        if SoHopLe(x):
            break
        elif LaSoNguyenTo(x):
            dem += 1
    return dem


def inKQ(kq):
    print('Co', kq, 'so nguyen to')


kq = NhapVaDem()
inKQ(kq)
