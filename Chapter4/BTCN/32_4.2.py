def nhap():
    n = int(input('n='))
    return n


def inkq(n):
    for i in range(2, n+1, 2):
        print(i, end=' ', sep='')

    print()


def tieptuc():
    hoi = str(input('Tiep tuc khong?'))
    if hoi != 'k' and hoi != 'K':
        n = nhap()
        inkq(n)
        tieptuc()


n = nhap()
inkq(n)
tieptuc()
