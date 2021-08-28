s = input()
kq = []
s = s.split(',')
for i in s:
    if int(i,2) % 3 == 0:
        kq.append(i)
print(','.join(kq))
