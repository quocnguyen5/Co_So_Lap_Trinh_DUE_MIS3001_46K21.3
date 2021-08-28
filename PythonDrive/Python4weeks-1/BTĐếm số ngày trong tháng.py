print('Chương trình đếm số ngày trong tháng')
m=int(input('Nhập vào 1 tháng: '))
if m in (1,3,5,7,8,10,12):
    print('Tháng ',m,' có 21 ngày.',sep='')
elif m in (4,6,9,11):
    print('Tháng ', m,' có 30 ngày.',sep='')
elif m ==2:
    y=int(input('Mời bạn nhập vào năm '))
    if (y % 4 ==0 and y % 100 !=0) or (y % 400 ==0):
        print('Tháng ', m,' có 29 ngày.',sep='')
    else:
        print('Tháng ',m,' có 28 ngày.',sep='')
else:
    print('Tháng ',m,' không hợp lệ.',sep='')
print('Cảm ơn đã tham gia chương trình.')

