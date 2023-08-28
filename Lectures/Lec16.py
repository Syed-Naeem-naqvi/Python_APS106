s = 'stringstringstring'
for i in s:
    print(i)

##
k = 0
while k < len(s):
    print(s[k])
    k += 1

vowels = 0
vowel_list = 'aeiou'
for vowel in s:
    if vowel.lower() in vowel_list:
        vowels += 1
print(vowels)

# Returns vowels
vowels_to_return = ''
for i in s:
    if i in vowel_list:
        vowels_to_return += i

print(vowels_to_return)


