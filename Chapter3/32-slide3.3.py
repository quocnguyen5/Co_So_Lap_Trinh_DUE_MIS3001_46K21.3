'''
Câu3.3.Nhập vào số KW điện tiêu thụ của một hộ gia đình,
sau đó in lên màn hình số tiền mà hộgiađình đó phải trả biết rằng cách tính tiền điện như sau:
-Từ KW 1 đến KW thứ 100:giá 550đ/1KW
-Từ KW101 đến KW thứ 150:giá 750đ/1KW
-Từ KW151 đến KW thứ 200:giá 950đ/1KW
-Từ KW201 trở đi:giá 1350đ/1KW
-Thuế VAT là 10%.
Thànhtiền = SốKW tiêuthụ * Đơngiá +VAT
'''

a = int(input('Tieu thu='))

tien = 0
if a <= 100:
    tien = a * 550

elif 100 < a <= 150:
    tien = 100 * 550 + (a - 100) * 750

elif 150 < a <= 200:
    tien = 100 * 550 + 50 * 750 + (a - 150) * 950

elif 200 < a:
    tien = 100 * 550 + 50 * 750 + 50 * 950 + (a - 200) * 1350

print('Phai tra=', int(tien * 1.1), sep='')
