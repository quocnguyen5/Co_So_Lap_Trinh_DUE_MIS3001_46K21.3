while True:
    x=int(input('Nhập một số: '))
    print(x,'là số chẳn' if x%2==0 else 'là số lẻ')
    hoi=input('Tiếp tục không? (c/k) ')
    if hoi=='k':
        break
print('Bye!thanks')