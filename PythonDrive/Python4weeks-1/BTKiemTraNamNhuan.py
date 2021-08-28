print("Chương trình kiểm tra năm nhuần")
y=int(input('Nhập vào 1 năm: '))
if (y % 4 ==0 and y % 100 !=0) or y % 400 ==0:
    print('Năm ', y, ' là năm nhuần.',sep='')
else:
    print('Năm ',y, ' không nhuần.',sep='')