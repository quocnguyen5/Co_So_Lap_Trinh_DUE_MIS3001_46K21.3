from typing import Sequence


def Input():
    L = []
    n = int(input('n='))
    for i in range(n):
        L.append(int(input()))
    x = int(input('x='))
    return L, x


def FirstAndLast(L):
    L = [L.pop(0)] + [L.pop()]
    # Hoặc hàm: del L[1:(len(L)-1)]
    print(L)


def Search(L, x):
    if x in L:
        print('True')
    else:
        print('False')


L, x = Input()
FirstAndLast(L)
Search(L, x)
