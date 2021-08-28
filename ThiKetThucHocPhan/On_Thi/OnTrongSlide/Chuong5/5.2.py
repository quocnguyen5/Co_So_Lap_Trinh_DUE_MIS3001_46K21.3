def Input():
    L = []
    n = int(input('n='))
    for i in range(n):
        L.append(int(input()))
    return L


def Search(L):
    Min = (min(L))
    Max = (max(L))
    return Max, Min


def Output(Max, Min):
    print(Max, Min)

L = Input()
Max, Min = Search(L)
Output(Max, Min)

