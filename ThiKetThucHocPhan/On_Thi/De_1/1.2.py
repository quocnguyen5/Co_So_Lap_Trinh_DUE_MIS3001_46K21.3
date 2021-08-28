def inp():
    n = int(input())
    return n 

def FeeShip(n):
    if n == 0:
        cost =  0
    else:
        cost = 5.95 + (n-1)*3.75
    return cost
 
def ShowFee(cost):
    print(cost)

n = inp()
cost = FeeShip(n)
ShowFee(cost)
