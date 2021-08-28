A = []
B = []
n = int(input('n='))
for i in range(n):
    A.append(int(input()))

for i in range(n-1, -1, -1):
    B = B + [A[i]]

print(B)

# print('[', end='')
# for i in range(0, n-1, 1):
#     print(B[i], end=' ')
# print(B[n-1],end='')
# print(']')


# C = sorted(A)
# print(C)

for i in range(len(B)):
    for j in range(i):
        if B[i] < B[j]:
            tmp = B[i]
            B[i] = B[j]
            B[j] = tmp
print(B)

# print('[', end='')
# for i in range(0, n-1, 1):
#     print(B[i], end=' ')
# print(B[n-1], end='')
# print(']')
