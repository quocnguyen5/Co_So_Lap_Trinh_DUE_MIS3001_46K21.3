# Tính giai thừa
# Bài 1.Viết chương trình nhập từ bàn phím một số nguyên n (0<=n<=100).In lên màn hình n!
n = int(input('n='))
result = 1
i = 1
while n >= i:
    result = result * i
    i = i + 1
print(n,'!=',result,sep='')


