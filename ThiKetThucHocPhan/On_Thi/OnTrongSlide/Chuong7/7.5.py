n = input().split()
X = input()

if X in n:
    for i in range(len(n)):
        if n[i] == X:
            print(i+1)
else:
    print(0)


nguyen