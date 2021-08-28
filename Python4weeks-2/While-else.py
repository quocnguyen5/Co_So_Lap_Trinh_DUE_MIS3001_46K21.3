count=sum=0
print("Nhap 5 so >= de tinh trung binh")
while count < 5:
    val=int(input('Moi nhap so '))
    if val < 0:
        print('So bị lỗi')
        break
    sum = val + sum
    count = count + 1
else:
    print('Trung binh cong',sum/countw