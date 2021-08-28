L =[]
SNC = []
SND = 0
n = int (input('n='))
for i in range(n):
    L.append(int(input()))
for i in L:
    if i > 0 :
        SND += 1
    if i % 2 == 0:
        SNC.append(i)
print('SND=',SND,sep='')
if len(SNC) == 0:
    print('TBC=0')
else:
    print('TBC=',sum(SNC)/len(SNC),sep='')