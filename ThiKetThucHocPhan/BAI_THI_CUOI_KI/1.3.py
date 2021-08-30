n = [int(x) for x in (input().split())]
kq = []
for i in n:
    if i not in kq:
        kq.append(i)
print(kq)

# 10 20 30 20 10 50 60 40 80 50 40
