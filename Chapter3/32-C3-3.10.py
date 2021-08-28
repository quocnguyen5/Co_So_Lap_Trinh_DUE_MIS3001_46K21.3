# Bai 3.10a
# n = int(input('n='))
# i = 1
# j = 1
# while i <= n:
#     print (i,)
#     i = i + 1

# Bai 3/10b
# cach 1
# n = int(input('n='))
# i = 1
# x = 0

# while i <= n:
#     if x == 5:
#         print()
#         x = 0

#     print (i,end=' ')
#     i = i + 1
#     x = x + 1


# cach 2
n = int(input('n='))
x = 0

for i in range(1,n+1):
    if x == 5:
        print()
        x = 0
    x = x + 1
    print(i,end=' ')
print('\n')
# cach 3
n = int(input('n='))

for i in range(1,n+1):
    print(i, end=' ')
    if i % 5 == 0:
        print()

    


# Bai 3/10c
# n = int(input('n='))
# i = 1
# j = 1

# while i <= n:
#     for j in range(1, n+1):
#         print(j, end=' ')
#     i = i + 1
#     print()
