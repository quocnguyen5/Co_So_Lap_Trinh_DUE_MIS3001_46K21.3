s = str(input())
result = ''
for letter in s:
    if letter is '0': 
        result='A'
    if letter is '1': 
        result='B'
    if letter is '2':
        result='C'
    if letter is '3':
        result='D'
    if letter is '4':
        result='E'
    if letter is '5':
        result='F'
    if letter is '6':
        result='G'
    if letter is '7':
        result='H'
    if letter is '8':
        result='K'
    if letter is '9':
        result='L'
    print(result,end='')
