'''

print('Nhập 1 số  [1..10]')
x=-1
while x<1 or x<10:
    x=int(input('Nhập [1..10]'))
    print(pow(x,2))
'''
#s=1+2+3+4...n
print('Nhập n:')
n=int(input())
s=0
i=0
while i<=n:
    s=s+i
    i=i+1
print(s)