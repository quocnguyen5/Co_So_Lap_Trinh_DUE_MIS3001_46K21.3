am = 0
duong = 0
while True:
    a = int(input())
    if a > 0:
        duong = duong + 1 
    elif a < 0: 
        am = am + 1
    else: 
        break

print(duong, ' so duong\n', am, " so am", sep='')
