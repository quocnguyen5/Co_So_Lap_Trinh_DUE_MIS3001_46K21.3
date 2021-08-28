s = input()
hoa = 0
thuong = 0
so = 0
khac = 0

for letter in s:
    if letter.isupper():
        hoa += 1
    elif letter.islower():
        thuong += 1
    elif letter.isnumeric():
        so += 1
    else:
        khac += 1

print('In hoa: %d' % (hoa))
print('In thuong: %d' % (thuong))
print('Chu so: %d' % (so))
print('Khac: %d' % (khac))
