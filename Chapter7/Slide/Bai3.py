s = input()
SCC = 0
SCS = 0

for letter in s:
    if letter.isnumeric():
        SCS += 1
    elif letter.isalpha():
        SCC += 1

print('Chu cai: %d' % (SCC))
print('Chu so: %d' % (SCS))