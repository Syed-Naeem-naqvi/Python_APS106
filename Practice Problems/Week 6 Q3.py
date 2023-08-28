text = 'University'
k = 2
n = len(text)

sp = ''
for i in range(len(text)):
    sp += text[i]
    if (i+1) % 2 == 0:
        sp += ' '

splitted = sp.split(' ')
lis = []
for i in splitted:
    lis.append(i[::-1])

print(lis)

