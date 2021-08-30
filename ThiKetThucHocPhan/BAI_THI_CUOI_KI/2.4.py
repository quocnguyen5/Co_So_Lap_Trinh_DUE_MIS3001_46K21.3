def check(i, L2):
    if i not in L2:
        return True


def kq():
    for i in L1:
        if check(i, L2):
            return False
    return True


L1 = input().split()
L2 = input().split()
print(kq())

'''
20 40
10 20 30 40 50 60
20 80
10 20 30 40 50 60
'''
