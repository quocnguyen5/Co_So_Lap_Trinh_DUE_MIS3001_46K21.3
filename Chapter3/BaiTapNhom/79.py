import random
i = 0
max = 0
up = 0

while i <= 100:
    x = random.randrange(1, 101)
    # print(x)
    i += 1
    if x > max:
        max = x
        up += 1


print('The maximum value found was', max)
print('The maximun value was updated', up, 'times')
