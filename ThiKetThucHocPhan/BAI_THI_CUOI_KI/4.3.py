s = input()
L = []
kq = []
max = 1
KQ = 'x'

for i in s:
    L.append(i)

for i in L:
    if i not in kq:
        kq.append(i)
        x = L.count(i)
        if x > max:
            max = x
            KQ = i

if len(kq) == len(L):
    print('None')
else:
    print(KQ)
