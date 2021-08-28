n = 15
j = 0
for i in range(n):
    j = j+(-1)**(i)/((2*i+2)*(2*i+3)*(2*i+4))
    pi = 3+4*j
    print(pi)
