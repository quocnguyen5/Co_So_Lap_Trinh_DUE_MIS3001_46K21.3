from string import maketrans   # bat buoc de goi ham maketrans.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "vi du Python ve chuoi....ok!!!"
print (str.translate(trantab))
