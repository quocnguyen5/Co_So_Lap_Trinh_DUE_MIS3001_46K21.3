# Tính giai thừa
#3.7a
# while True:
#     n= int(input('n='))
#     result = 1
#     i = 1
#     if n > 0:
#         while i <= n:
#             result = result * i
#             i = i + 1
#     elif n==0:
#         result = 1
#     else: break
#     print('n!=', result, sep='')


#3.7b
n = int(input('n='))
while n >= 0:
    result = 1
    for i in range(1, n+1):
        result = result * i
    print('n!=', result, sep='')
    n = int(input('n='))
