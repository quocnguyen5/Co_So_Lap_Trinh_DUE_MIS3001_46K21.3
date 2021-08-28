n = input()

n = " ".join(n.split())
n = n.capitalize()
n = n.replace(' ,', ',')
n = n.replace(' ;', ';')
n = n.replace(' .', '.')
n = n.replace(' :', ':')

print(n)

# /n = input()
# n = n.strip()
# n = n.capitalize()
# puncs = [',', ';', ':', '.']
# for punc in puncs:
#     while n.find(' ' + punc) != -1:
#         n = n.replace(' ' + punc, punc)

# print(n)
a = input()
cacdau = [',', ':', ';', '.']
for dau in cacdau:
    while a.find(' ' + dau) != -1:
        a = a.replace(' ' + dau, dau)
a = " ".join(a.split())
a = a.capitalize()

print(a)

# Cach3
st = input()
st = st.strip()
st = ' '.join(st.split())
st = st[0].upper() + st[1:].lower()
M = [',', ';', ':', '.']
i = 0
while i < len(st):
    if st[i] in M:
        if st[i - 1].isspace():
            st = st[:i - 1] + st[i:]
    i += 1
print(st)
