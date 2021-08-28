n = [str(x) for x in input().split(',')]
L = []
for x in n:
    if int(x, 2) % 3 == 0:
        L.append(x)
print(','.join(L))
