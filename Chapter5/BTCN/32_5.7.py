L = []

n = int(input('n='))
for i in range(n):
    L.append(int(input()))

M = []
# Cach 1
for x in L:
    if x not in M:
        M.append(x)


[print(i, end=' ') for i in M]
