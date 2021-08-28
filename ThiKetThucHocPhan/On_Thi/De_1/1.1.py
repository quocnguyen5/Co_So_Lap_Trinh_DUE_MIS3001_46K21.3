L = []
T = []

while True:
    x = int(input())
    if x == 0:
        break
    else:
        L.append(x)

for i in L:
    if i > 0 and i % 2 == 0:
        T.append(i)

if len(L) == 0:
    print('Khong hop le')
elif len(T) == 0:
    print(0)
else:
    print(sum(T) / len(T))
