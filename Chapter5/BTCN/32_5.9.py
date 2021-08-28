def Input():
    n = int(input('n='))
    m = int(input('m='))

    return m, n


m, n = Input()

L1 = []
print('L1:')
for i in range(n):
    L1.append(int(input()))

L2 = []
print('L2:')
for i in range(m):
    L2.append(int(input()))

L3 = []
for i in L1:
    for j in L2:
        if i == j:
            L3 += [j]

print('L3:', end=' ')
[print(x, end=' ') for x in L3]
