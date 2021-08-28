def nhap():
    n = int(input('n='))
    return n


def giaithua(n):
    global result 
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
    
def inkq(n,X):
    print(n,'!=', X, sep='')

n= nhap()
giaithua(n)
inkq(n,result)


