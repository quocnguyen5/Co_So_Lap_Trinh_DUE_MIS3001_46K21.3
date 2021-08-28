# Đếm 1 số có bao nhiêu chữ số
a=int(input('n='))
n = a
s = 1 #so chu so 
while n > 10:
    if n // 10 > 0: #chia so cho 10, neu phan nguyen > 0 (kh phai so thuc) thi chia tiep, so chu so cong them 1
        s = s+1
        n = n // 10

print(a,'co',s,'chu so')