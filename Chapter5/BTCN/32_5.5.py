A = []
Tong = 0
n = int(input('n='))
for i in range(n):
    A.append(int(input()))
for x in range(1, n, 2):
    Tong += A[x]
print('Tong=', Tong, sep='')
