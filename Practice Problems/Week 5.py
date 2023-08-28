# Q1

user_input = input('Enter a string: ')
i = 0
output = ''

while i < len(user_input):
    if user_input[i].islower():
        output += user_input[i].upper()
    elif user_input[i].isupper():
        output += user_input[i].lower()
    i += 1

# print(output)

# Q1 Solution 2

Uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lowers = 'abcdefghijklmnopqrstuvwxyz'
second_input = input('Enter a string: ')
j = 0
output_str = ''
while j < len(second_input):
    if second_input[j] in Uppers:
        index = Uppers.find(second_input[j])
        output_str += Lowers[index]
    elif second_input[j] in Lowers:
        index = Lowers.find(second_input[j])
        output_str += Uppers[index]
    j += 1

# print(output_str)


# Q2

user_input = input('Enter a string: ')
to_remove = '!?'
k = 0
result_str = ''
while k < len(user_input):
    if user_input[k] in to_remove:
        result_str += ''
    else:
        result_str += user_input[k]
    k += 1

# print(result_str)

# Q3a

full_name = (input('Enter your full name: ')).upper()
first_name = 'Joe'.upper()
ind = full_name.find(first_name)
if ind == 0:
    print('How did you know my name?')
else:
    print('It\'s rude to not know my name')

# Q3b


def match_text(text_1, text_2):
    condition = False
    if text_1.upper() == text_2.upper():
        condition = True
    return condition


# print(match_text('Abc', 'AbC'))

# Q4

input_int = 20020
input_str = str(input_int)
rev_str = input_str[::-1]
print(rev_str)
p = 0
first_is_zero = False
while p < len(rev_str):
    if rev_str[0] == '0':
        rev_str.replace((rev_str[0]),'')
        p += 1
print(int(rev_str))










