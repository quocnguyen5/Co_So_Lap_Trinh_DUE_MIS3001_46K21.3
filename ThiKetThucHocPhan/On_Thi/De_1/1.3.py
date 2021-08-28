A = []
N = []
M = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        A.append(x)

for i in A:
    if i % 2 == 0:
        N.append(i)
    if i % 2 == 1:
        M .append(i)

N.sort()
M.sort()

for i in N: 
    print(i,end=' ')
print()
for i in M:
    print(i,end=' ')

