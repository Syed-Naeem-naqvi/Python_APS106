# Q 1, 2, and 5 on home computer

# Q3

input_s = 'Hello'
k = 3
n = len(input_s)
parts = int(n/k)

new = ''
for i in range(len(input_s)):
    new += input_s[i]
    if (i+1) % k == 0:
        new += ' '

splitted = new.split(' ',parts)
print(splitted)
lis = []
for i in splitted:
    lis.append(i[::-1])

for i in lis:
    print(i)

# Q4


def count_vowels(n):
    """ (str) -> str
    Returns the number of each vowel in
    the string n
    """
    n = n.lower()
    vowels = 'aeiou'
    count_a, count_e, count_i, count_o, count_u = 0,0,0,0,0
    for i in n:
        if i == vowels[0]:
            count_a += 1
        elif i == vowels[1]:
            count_e += 1
        elif i == vowels[2]:
            count_i += 1
        elif i == vowels[3]:
            count_o += 1
        elif i == vowels[4]:
            count_u += 1
    print('Number of A\'s = ', count_a , '\n'
          'Number of E\'s = ', count_e , '\n'
          'Number of I\'s = ', count_i , '\n'
          'Number of O\'s = ', count_o , '\n'
          'Number of U\'s = ', count_u , '\n')


count_vowels('AEIou')


