def nhap():
    s = input()
    return s

def dem(s):
    global hoa, thuong, so, khac
    hoa = 0
    thuong = 0
    so = 0
    khac = 0
    for char in s:
        if char.isupper():
            hoa += 1
        elif char.islower():
            thuong += 1
        elif char.isnumeric():
            so += 1
        else:
            khac += 1


def inkq():
    print('In hoa:', hoa,'\nIn thuong:',thuong,'\nChu so:', so,'\nKhac',khac)

s = nhap()
dem(s)
inkq()
