while True:
    n = int(input('Nhập một số n có 2 chữ số: '))
    kq = None
    if n < 0 or n >= 100:
        print('n không hợp lệ')
    else:
        donvi = n % 10
        chuc = n // 10

        if chuc == 2:
            kq = ('Hai mươi ')
        elif chuc == 3:
            kq = 'Ba mươi '
        elif chuc == 4:
            kq = 'Bốn mươi '
        elif chuc == 5:
            kq = 'Năm mươi '
        elif chuc == 6:
            kq = 'Sáu mươi '
        elif chuc == 7:
            kq = 'Bảy mươi '
        elif chuc == 8:
            kq = 'Tám mươi '
        elif chuc == 9:
            kq = 'Chín mươi '

        if donvi == 1:
            kq = kq + 'một'
        elif donvi == 2:
            kq = kq + 'hai'
        elif donvi == 3:
            kq = kq + 'ba'
        elif donvi == 4:
            kq = kq + 'bốn'
        elif donvi == 5:
            kq = kq + 'năm'
        elif donvi == 6:
            kq = kq + 'sáu'
        elif donvi == 7:
            kq = kq + 'bảy'
        elif donvi == 8:
            kq = kq + 'tám'
        elif donvi == 9:
            kq = kq + 'chín'
    print(kq)

