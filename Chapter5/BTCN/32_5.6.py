A = []
# B = []
for i in range(10):
    A.append(int(input()))

B = A.copy()
for i in range(0, 10, 2):
    B[i] = A[i + 1]
    B[i + 1] = A[i]

for j in range(10):
    print(B[j], end=' ')
