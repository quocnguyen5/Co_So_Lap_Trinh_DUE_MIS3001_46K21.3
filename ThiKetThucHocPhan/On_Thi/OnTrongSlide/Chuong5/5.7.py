L = []
n = int(input('n='))
for i in range(n):
    L.append(int(input()))

L = list(set(L))
for i in L:
    print(i,end=' ')
