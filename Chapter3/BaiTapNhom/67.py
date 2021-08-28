print('Nhap tuoi:')
age = []
a = 0
tuoi = input()
while tuoi != '':
    age.append(int(tuoi))
    tuoi = input()
for i in age:
    if i <= 2:
        a = a+0
    elif i >= 3 and i <= 12:
        a = a+14
    elif i >= 65:
        a = a+18
    else:
        a = a+23
print("The cost=${:.2f}".format(a))