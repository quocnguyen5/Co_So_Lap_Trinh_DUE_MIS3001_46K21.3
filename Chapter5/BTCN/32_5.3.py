L = []
SND = 0
TONG = 0
SNC = 0

n = int(input('n='))
for i in range(n):
    L.append(int(input()))
    if L[i] > 0:
        SND += 1
    if L[i] % 2 == 0:
        SNC += 1
        TONG += L[i]

if SNC == 0:
    TBC = 0
else:
    TBC = TONG/SNC


print('SND=', SND, sep='')
print('TBC=', TBC, sep='')
