A = []
M = []
N = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        A.append(n)

for i in A:
    if i % 2 == 0:
        N.append(i)
    else:
        M.append(i)

N.sort()
M.sort()

for i in N:
    print(i,end=' ')
print()
for i in M:
    print(i, end=' ')
