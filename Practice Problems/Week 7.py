import random


# Q1
def generate_n_sorted_random_numbers(n):
    """ (n) -> List
    Given a number n, generate a list of n random numbers
    which are ordered. Numbers are between 0 and 999
    """
    output = []
    while n > 0:
        output.append(random.randint(0, 999))
        n -= 1

    return sorted(output)


print(generate_n_sorted_random_numbers(5))

# Q2


def find_median(L):
    """ (List) -> List
    Given a sorted list, return the median
    >>> find_median([1,2,3])
    2
    >>> find_median([1,2,3,4])
    2.5
    """
    median = 0
    length = len(L)
    if length % 2 != 0:
        median = L[length//2]
    elif length % 2 == 0:
        first = L[length//2]
        second = L[length//2 - 1]
        median = (first + second)/2
    return median


print(find_median([1, 2, 3]))
print(find_median([1, 2, 3, 4]))


# Q3


def extract_list_properties(L):
    """ (List) -> List
        Given a sorted list L, extract:
        1) Minimum
        2) Maximum
        3) Median
        4) Arithmetic mean
        5) Geometric mean
    """
    list_properties = []
    minimum = L[0]
    maximum = L[len(L) - 1]
    median = find_median(L)
    arith_mean = sum(L)/len(L)
    term_product = 1
    for i in L:
        term_product *= i
    geo_mean = round(term_product ** (1/len(L)), 5)
    list_properties.extend([minimum, maximum, median, arith_mean, geo_mean])

    return list_properties


print(extract_list_properties([1,2,3]))

# Q4

s = 'University'
n = len(s)
k = 5
size = n/k

list_rep = []
helper_s = ''
for i in range(len(s)):
    helper_s += s[i]
    if len(helper_s) == size:
        list_rep.extend([helper_s])
        helper_s = ''
rev = []
for i in range(k):
    rev.append(list_rep[i][::-1])
rev.reverse()

# Q5

Database1 = [['Mohamed', 'A, A+, C, FZ, B-'],
            ['Cindy', 'B, B, C, A, B'],
            ['Mustafa', 'A, A+, A+, C, C'],
            ['Stefan', 'FZ, B, B, C, C']]


def print_database(database):
    for i in range(len(database)):
        for j in range(len(database[0])):
            print(database[i][j])


def return_students_with_grade(Database, grade):
    students = []
    print_database(Database)
    for i in range(len(Database)):
        if grade in Database[i][1]:
            students.append(Database[i][0])
    return students


print(return_students_with_grade(Database1,'A'))
print(return_students_with_grade(Database1,'C'))

# Q6














