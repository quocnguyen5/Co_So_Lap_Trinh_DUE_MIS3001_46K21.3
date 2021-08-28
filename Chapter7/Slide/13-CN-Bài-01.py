import re
n = (input())
L = list(n)
hoa = 0
thuong = 0
so = 0
khac = 0
for i in L:
    if re.search("[A-Z]", i):
        hoa = hoa + 1
    elif re.search("[a-z]", i):
        thuong = thuong + 1
    elif re.search("[0-9]", i):
        so = so + 1
    else:
        khac = khac + 1
print('In hoa:', hoa)
print('In thuong:', thuong)
print('Chu so:', so)
print('Khac:', khac)
