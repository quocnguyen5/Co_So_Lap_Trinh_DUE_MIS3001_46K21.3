
x = float(input('x='))
y = float(input('y='))
ch = str(input)

if ch == '/':
    print(x,'/',y,'=',x/y,sep='')
elif ch == '+':
    print(x,'+',y,'=',x+y,sep='')
elif ch == '-':
    print(x,'-',y,'=',x-y,sep='')
elif ch == '*':
    print(x,'*',y,'=',x*y,sep='')
else:
    print('Khong hop le')

