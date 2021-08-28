

def add(L, x, k):
    if k > len(L):
        L = L + [x]
    else:
        L = L[:k-1] + [x] + L[k-1:]
    return L


def search(L, x):
    global dem
    dem = -1

    for i in L:
        dem += 1
        if x == i:
            print(dem)
            break

        else:
            return False


def delete(L, x):
    L2 = []

    for i in L:
        if i!=x:
            L2 += [i]
    
    return L2


L = [1, 2, 3, 4, 5, 2]
x = 2
L2 = delete(L, x)
print(L2)


def count(L):
    dem = 0
    for i in L:
        if i != []:
            dem += 1
    print(dem)


def update(L, x, y):
    if x in L:
        L[L.index(x)] = y
