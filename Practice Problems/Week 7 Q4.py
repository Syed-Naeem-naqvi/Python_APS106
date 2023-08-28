s = "University"
k = 2
n = int(len(s))

white_space = ''
for i in range(len(s)):
    white_space += s[i]
    if (i+1)%2 == 0:
        white_space += ' '

print(white_space)

l = white_space.split(" ")
rev = []
for i in l:
    rev.append(i[::-1])

print(rev)
output = rev[::-1]
print(output)
if '' in output:
    output.remove('')
print(output)
for i in output:
    print(i)
    