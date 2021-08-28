import math


def nhap():
    # global a, b, c
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c


def giaipt(a, b, c):
    #Xet tat ca truong hop
    # if a == 0:
    #     # bx+c=0
    #     if b == 0:
    #         if c == 0:
    #             print('INF')
    #         else:
    #             print('NO')
    #     else:
    #         if c == 0:
    #             print(0)

    #         else:
    #             x = -c/b
    #             print(round(x, 2))2

    # else:
    global x1, x2
    global delta
    delta = b**2-4*a*c
    if delta == 0:
        x1 = x2 = -b/(2*a)
    elif delta > 0:
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        x1 = float((-b + math.sqrt(delta)) / (2 * a))


def inkq():
    if delta > 0:
        print('Phuong trinh co hai nghiem')
        print('x1=', x1,sep='')
        print('x2=', x2,sep='')
    elif delta == 0:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=', x1, sep='')
    else:
        print('Phuong trinh vo nghiem')


a, b, c = nhap()
giaipt(a, b, c)
inkq()
