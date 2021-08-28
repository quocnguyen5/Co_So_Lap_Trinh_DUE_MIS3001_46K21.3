m = int(input('m='))
n = int(input('n='))
print('A:')
for i in range(m):
    A = []
    for j in range(n):
        A.append(input())
print('B:')
for i in range(m):
    B = []
    for j in range(n):
        B.append(input())

# FIXME:

C = [A]+[B] 
print( C)
for row in C:
    for item in row:
        print(item,end=' ')