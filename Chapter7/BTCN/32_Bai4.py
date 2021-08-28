n = [str(x) for x in input().split(',')]
L = []
for x in n:
    if x not in L:
        L.append(x)
L.sort()
print(','.join(L))