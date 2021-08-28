m1 = int(input('M1='))
m2 = int(input('M2='))
m3 = int(input('M3='))
s = int(input('S='))
tien = 0
if s <= 100:
    tien = s * m1

elif 100 < s <= 150:
    tien = 100 * m1 + (s - 100) * m2

elif 150 < s:
    tien = 100 * m1 + 50 * m2 + (s - 150) * m3

print('Phai tra=', tien, sep='')
