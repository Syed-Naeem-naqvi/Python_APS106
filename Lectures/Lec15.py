# Lec 15
# Strings continued

# Pass: Doesn't do shit

s = 'string'
k = s[1:]
print(k)
length = len(s)
print(length)

# indexing: go from start to end-1

x = '1234'
print(int(x))

y = 1234
print(str(y))

# Strings are immutable
# strings aren't change-able
# Can emulate changes by making new objects
# Using aliasing

# loop over a string


string1 = 'abcde'
position = 0
s_new = ''
while position < len(string1): # Has to be less otherwise it will overindex
    s_new += string1[position] + ' '
    position += 1
print(s_new)


Vowels = 'AEIOUY'
s2 = 'A House'
i = 0
vowels = 0
while i < len(s2):
    if (s2[i]).upper() in Vowels:
        vowels += 1
    i += 1

print(vowels)





