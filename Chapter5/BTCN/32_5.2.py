def Input():
    L = []
    n = int(input('n='))
    for i in range(n):
        L.append(int(input()))
    return L


def Search(L):
    min = max = L[0]

    for x in range(len(L)):
        if L[x] > max:
            max = L[x]
        if L[x] < min:
            min = L[x]
    return max, min


def Output(max, min):
    print(max, min)


max, min = Search(Input())
Output(max, min)
