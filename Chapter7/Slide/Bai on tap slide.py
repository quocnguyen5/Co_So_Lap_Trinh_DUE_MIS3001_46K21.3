# s = 'Hello world!'
# print(s[1])
# print(s[0:5])
# print(s[:5])
# print(s[3:])


# print()
# # 7.3
# print('Hello'.upper())
# print('Hello'.upper().isupper())
# print('Hello'.upper().lower())

# print('Remember, remember, the fifth of November.'.split())
# print('-'.join('There can be only one.'.split()))


# print()
# # 7.4


# print()
# # 7.5
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
