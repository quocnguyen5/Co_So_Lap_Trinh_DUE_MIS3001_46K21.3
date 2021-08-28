while True:
    a = float(input('a='))
    b = float(input('b='))
    ch = str(input('Toan tu:'))
    
    if ch == '/':
        print(a, '/', b, '=', a/b, sep='')
    elif ch == '+':
        print(a, '+', b, '=', a+b, sep='')
    elif ch == '-':
        print(a, '-', b, '=', a-b, sep='')
    elif ch == '*':
        print(a, '*', b, '=', a*b, sep='')
    tieptuc = str(input('Tiep tuc:'))
    if tieptuc == 't' or tieptuc == 'T':
        break





