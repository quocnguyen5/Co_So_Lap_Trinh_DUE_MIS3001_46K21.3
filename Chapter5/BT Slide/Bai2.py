L = [1, 2, 3, 4, 5]


def search(L, x):
    for i in range(len(L)):
        if x == L[i]:
            return i
    return None


x = 5
print(search(L, x))
