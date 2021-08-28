t=int(input('Nhập vào Số T: '))
h=(t//3600)%24
#chia cho 24 vì để xem có ra thành 1 ngày k, vì chia lấy dư nếu chưa đủ 1 ngày thì k tính
m=(t%3600)//60
s=(t%3600)%60
print(h,':',m,':',s,sep='')