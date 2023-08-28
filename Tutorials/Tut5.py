# Tut 5

# 1) from start to end-1
# 2) when slicing with negatives, it's from leftmost element to rightmost-1
# 3) Bigger negative index first
s = 'HELLO'
slice = s[-3:-1]
print(slice)


name = 'joe'
print(name.upper().replace('j','B'))
print(name.replace('j','B').upper())

# Practice questions


def string_sum(s):
    """ (str) -> int
    Returns the sum of all digits found within the string
    """
    i = 0
    sum_digits = 0
    while i < len(s):
        if s[i].isdigit():
            sum_digits += int(s[i])
        i += 1
    return sum_digits


x = 'I see 5 people over there, and 2 of them are sitting down. call 911'
print(string_sum(x))


# Practice question 2

def string_avg(s):
    """ (str) -> float
    Returns the average of all the digits that appear in
    the string, rounded to 2 decimal places
    """
    i = 0
    sum_digits = 0
    count_digits = 0
    while i < len(s):
        if s[i].isdigit():
            sum_digits += int(s[i])
            count_digits += 1
        i += 1
    avg = sum_digits / count_digits
    avg = round(avg, 2)
    return avg


print(string_avg('abcde12f3'))

