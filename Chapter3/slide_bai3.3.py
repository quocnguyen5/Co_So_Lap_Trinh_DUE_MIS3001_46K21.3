
#Bang cửu chương 9x9

'''
i = 1
x = 0
count = 0
boiso = 1
while i <= 81 and x <= 8:
    print(i, end=' ')
    i = i + boiso
    count = count + 1
    if count == 9:
        print('\n')
        x = x + 1
        i = x + 1
        boiso = boiso + 1
        count = 0
'''
#Cách 2

print(('\n'))
i= 1 #dong
while i<= 9:
    j = 1 #cot
    while j <= 9:
        print(i*j,end=' ')
        j= j + 1

    print()
    i = i + 1
print('\n')
#Cách 2-Dùng for
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end=' ')
    print()









        











