# # slide 6
# print('"Đen Vâu" is a rap singer\nHe\'s 32 years old\nI want to become a rapper')

# print(r'"Đen Vâu" is a rap singer\nHe\'s 32 years old\nI want to become a rapper')
# st = '''
# abc
# casc
# cascsacsa
# '''
# print(st)

# str = "Python Programming"
# print(str[:6])
# print(str[7:])
# print(str2[0:3])
# print(str1[-4:])
# print(str[:2] + str[-4:])

# str1 = str[:6]
# str2 = str[7:]
# print(str1 in str)
# print(str2 not in str)
# str3 = "PYTHON"
# print(str3 not in str)
# print(" " in str)

# slide 17
# str = "Python Programming"
# print("\n")
# print('How are you?')

# feeling = input()

# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')


# Slide 19
# str = 'Learn PYTHON Programming'
# ch = 'n'
# dem = 0
# for i in str:

#     if i.lower() == ch.lower():
#         dem += 1
# print('Number of chracter n is:', dem)


# slide 28
# def startswith(st1,st2,st3):
#     if st1.startswith(st2) and st1.endswith(st3):
#         return True
#     else:
#         return False

# slide 35
# print('sandwiches'.ljust(20, '.'), '4'.rjust(5, ' '))
# print('apples'.ljust(20, '.'), '12'.rjust(5, ' '))
# print('cups'.ljust(20, '.'), '4'.rjust(5, ' '))
# print('cookies'.ljust(20, '.'), '8000'.rjust(5, ' '))

# slide 38
# st = 'AbbaTheAbbaSongsAbab'
# print(st.rstrip('ab'))
# print(st.lstrip('ab'))
# print(st.strip('Aab'))

data = 'Email cua toi la: tn20502@gmail.com Sat Jan'
pos1 = data.find('@')
print(pos1)
pos2 = data.find(' ', pos1)
print(pos2)
host = data[(pos1+1):pos2]
print(host)
