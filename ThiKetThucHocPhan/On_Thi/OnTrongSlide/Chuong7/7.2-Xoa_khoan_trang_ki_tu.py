s = input()

puncs = [',', ':', ';', '.']
for punc in puncs:
    while s.find(' ' + punc) != -1:
        a = s.replace(' ' + punc, punc)
s = " ".join(s.split())
s = s.capitalize()

print(s)

