

# def nhap():
#     global M1, M2, S
#     M1 = int(input('M1='))
#     M2 = int(input('M2='))
#     S = int(input('S='))
#     # return M1, M2, S
#     print()


# def tiendien(M1,M2,S):
#     if S <= 100:
#         TienDien = S*M1
#     else:
#         TienDien = 100*M1 + (S-100)*M2
#     PhaiTra = TienDien + TienDien*0.1
#     print('So dien nang tieu thu la', S, 'chu')
#     print('So tien phai tra:', PhaiTra)
#     print()


# while True:
#     print('CONG VIEC')
#     print('-'*25)
#     print('So 1: Nhap M1, M2 va S')
#     print('So 2: Tinh so tien phai tra')
#     print('So 0: Thoat')
#     print('-'*25)
#     n = input('Moi ban chon cong viec ')
#     print()
#     if n == '1':
#         nhap()
#     elif n == '2':
#         tiendien(M1,M2,S)
#     elif n == '0':
#         break


# def LaSoNguyenTo(x):
#     SNT = 0
#     for i in range(1, x+1):
#         if x % i == 0:
#             SNT = SNT + 1
#     if SNT != 2:
#         return False
#     return True

def LaSoNguyenTo(x):
    for i in range(2, x):
        # if x == 2:
        #     return True
        if x % i == 0:
            return False
       
    return True

def SoHopLe(x):
    if x <= 1:
        return True
    return False


def nhapvadem():
    global kq
    global x
    kq = 0
    print('Nhap day so:')
    while True:
        x = int(input())
        if SoHopLe(x):
            break
        elif LaSoNguyenTo(x):
            kq = kq + 1


def InKQ(kq):
    print('Co', kq, 'so nguyen to')


nhapvadem()
InKQ(kq)
