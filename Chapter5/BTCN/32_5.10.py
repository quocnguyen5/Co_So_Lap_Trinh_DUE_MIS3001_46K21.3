L = []
n = int(input('n='))

for i in range(n):
    print('Hoc sinh ', i+1, ':', sep='')
    DiemHocSinh = []
    for j in range(2):
        if j == 0:
            DiemHocSinh.append(float(input('Toan=')))
        if j == 1:
            DiemHocSinh.append(float(input('Ly=')))
    L.append(DiemHocSinh)


for i in range(n):
    for j in range(2):
        TBC = (L[i][0] + L[i][1])/2
    L[i].append(TBC)

TBCmax = L[i][2]
for i in range(n):
    if TBCmax < L[i][2]:
        TBCmax = L[i][2]
print("DTB cao nhat:", TBCmax)
