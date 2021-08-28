n = int(input('n='))
i=1
count = 0
while i <= n:
    if count == 10:
        print()
        count = 0
    print(i,end=' ')
    i += 1
    count += 1
        
print('\n')
#CÁCH 2:
# i chưa hết cho 10 thì xuống dòng
#CÁCH FOR
# n = int(input('n='))
# for i in range(1, n+1):
#     print(i, end=' ')
#     if i % 10 == 0:
#         print('')


