# Iterable to __iter()__
# some iterators are immutable (ranges)
# Lists are mutable
# infinite for loops exist

iterator1 = iter('abcd')

for i in iterator1:
    print(i)

# iterator gets used up

iterator2 = iter('abcd')

for i in iterator2:
    print(i)
    print('next:', iterator2.__next__())

# runs twice for 4 characters


# Range()

s = 'Hello'
vowels = 0
vowel_list = 'aeiou'
for vowel in range(len(s)):
    if s[vowel].lower() in vowel_list:
        vowels += 1
print(vowels)


s2 = 'Abcef'

vowels_to_return = ''
for i in range(len(s2)):
    if s2[i].lower() in vowel_list:
        vowels_to_return += s2[i]

print(vowels_to_return)


s = 'ab'
iterations = 0
for i in s:
    s = s + 'c'
    print(i, iterations)
    print('s is: ', s)
    iterations += 1

    if iterations > 10:
        break

# not true for mutable stuff

l = [1, 2]
for i in l:
    l.append(i+1)
    print(i)

    if i > 100:
        break