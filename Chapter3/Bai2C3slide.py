# Tìm số Nguyên Tố
n = int(input('n='))
dem = 0
x = 1
while x <= n:
    if n % x == 0:
        dem = dem + 1
    x = x + 1
if dem == 2:
    print(n,'la SNT')
else:
    print(n, 'khong la SNT')
  
    
