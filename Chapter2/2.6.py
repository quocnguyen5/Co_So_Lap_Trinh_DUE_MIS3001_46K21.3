"""
-Nhập vào: Họ tên, Đơn giá ngày công, Số ngày công, Hệ số phụ cấp, Tiền tạm ứng.
-In lên màn hình: Họ tên, Lương, Tạm Ứng và thực lĩnh
-Lương=(Đơn giá ngày công) * (Số ngày công) * (Hệ số phụ cấp)
-Thực lính=Lương-Tạm ứng
"""
a=str(input('Ho ten: '))
b=int(input('So ngay cong: '))
c=int(input('Don gia ngay cong: '))
d=float(input('He so phu cap: '))
e=int(input('Tam ung: '))
x=float(c*b*d)
y=float(x-e)
print('Nhan vien ',a,', Co tien Luong=',x,', Tam ung=',e,' va Thuc linh=',y,sep='')

