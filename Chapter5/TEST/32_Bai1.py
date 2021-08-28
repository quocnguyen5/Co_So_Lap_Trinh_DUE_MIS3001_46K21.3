SoNguyen = []


while True:
    print('Nhap day so:')
    so = int(input())
    SoNguyen = SoNguyen + [so]
    if so == 0:
        break


n = int(input('n='))
if n in SoNguyen:
    print(n, 'co ton tai')
else:

    print(n, 'khong ton tai')
