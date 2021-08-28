# try:
#     ten, mail = [x for x in input().split(', Email: ')]
#     print(mail)
# except:
#     print('')
#
#
#
#
#
# #cach 2
# # st = input().split(': ')
# # if len(st) == 3:
# #     print(st[2])


import re

st = input()
zst = r"(.+)(Email: )(.+)"
print(re.match(zst, st).group(3)
      if re.match(zst, st)
      else " ")
