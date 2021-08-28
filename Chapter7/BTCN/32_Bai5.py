n = [str(x) for x in input().split(' ')]
X = int(input())
L = []

for x in range(len(n)):
    if int(n[x]) == X:
        L.append(x+1)

if L == []:
    print (0)
else:
    for i in L:
        print(int(i))