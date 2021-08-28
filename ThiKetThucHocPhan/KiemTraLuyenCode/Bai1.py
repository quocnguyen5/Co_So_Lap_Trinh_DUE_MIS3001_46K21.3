N, L = [int(x) for x in input().split()]
List = []

for i in range(N):
    x = input()
    if len(x) == L:
        List.append(x)

List.sort()
print(''.join(List))