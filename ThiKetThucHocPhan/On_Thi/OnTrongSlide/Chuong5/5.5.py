L = []
tong = 0
n = int(input('n='))
for i in range(n):
    L.append(int(input()))
for i in range(1,n ,2):
    tong += L[i]

print('Tong=',tong,sep='')
