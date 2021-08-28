'''
Viết phương trình tính lãi suất tiết kiệm
Nhập vào T%/tháng
Nhập số vốn ban đầu n và số tháng gửi k. Tính số tiền m nhận được sau k tháng
m=n*(1+k*T)
'''
n=int(input('So tien ban dau: '))
k=int(input('So thang gui: '))
T=float(input('Lai suat/ thang: '))
print('Voi so tien ban dau ',n, ', sau ',k,' thang gui, lai suat ',T,'/ thang',sep='')
print('Thi so tien nhan duoc cuoi ky la:', float(n*(1+k*T)))
