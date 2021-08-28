def Input():
    L = []
    n = int(input('n='))
    for i in range(n):
        L.append(int(input()))
    x = int(input('x='))
    return L, x


def FirstAndLast(L):
    L = [L[1], L[-1]]
    print(L)


def Search(L, x):
    if x in L:
        return True
    else:
        return False


L, x = Input()
FirstAndLast(L)
print(Search(L, x))
