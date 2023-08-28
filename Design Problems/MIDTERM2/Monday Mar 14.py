def sparse_add(d1, d2):
    """ (Dict, Dict) -> List
    Adds two sparse vectors
    """
    # Find the biggest key
    keys = []
    for key in d1:
        keys.append(key)
    for key in d2:
        keys.append(key)
    biggest_key = max(keys)

    # Now, generate 2 right-sized empty vectors
    v1 = [0]*(biggest_key+1)
    v2 = [0]*(biggest_key+1)

    # Fill up the vectors with the dict info
    for key, value in d1.items():
        v1[key] = value

    for key, value in d2.items():
        v2[key] = value

    # Add v1 and v2
    res = [0]*(biggest_key+1)
    for i in range(len(v1)):
        res[i] = v1[i] + v2[i]
    out = {}
    for i in range(len(res)):
        if res[i] != 0:
            out[i] = res[i]
    return out


# print(sparse_add({0:1,6:3},{0:2,1:1,6:3}))


def sparse_dot(d1, d2):
    """ (Dict, Dict) -> number
    Given two sparse vectors  calculate their dot
    product
    """
    # Find the biggest key
    keys = []
    for key in d1:
        keys.append(key)
    for key in d2:
        keys.append(key)
    biggest_key = max(keys)

    # Now, generate 2 right-sized empty vectors
    v1 = [0] * (biggest_key + 1)
    v2 = [0] * (biggest_key + 1)

    # Fill up the vectors with the dict info
    for key, value in d1.items():
        v1[key] = value

    for key, value in d2.items():
        v2[key] = value

    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]

    return dot


# print(sparse_dot({0:1,6:3},{0:2,1:1,6:3}))


def sparsify(v):
    """ (List) -> Dict
    Given a vector v, returns it's sparse version
    """
    dict_out = {}
    for i in range(len(v)):
        if v[i] != 0:
            dict_out[i] = v[i]

    return dict_out


# print(sparsify([0, 0, 0, 4, 0, 0, 5]))
# print(sparse_add(sparsify([0,0,1,-2,0,0]), sparsify([0,1,0,2,0,0])))

# Q8

word = 'philadelphia'
letter_dic = {}
for i in word:
    letter_dic[i] = word.count(i)
out = ''
for let, count in letter_dic.items():
    if count == max(letter_dic.values()):
        out += let + ' appears ' + str(count) + ' times. '

# print(out)


#
# def reversed_dictionary(d):
#     """ (Dict) -> Dict
#     Given a dictionary of the form: {emp: {software}}
#     Returns: {software: {emp}}
#     """
#     # generate a set of all software
#     all_software = set()
#     for set_ in d.values():
#         for item in set:
#             all_software.add(item)
#
#     # Generate a list of all employees
#     emps = []
#     for emp in d.keys():
#         emps.append(emp)
#
#     # Generate the reverse
#     rev = {}
#     for emp, s_set in d.items():
#         for soft in s_set:

# Online Questions
# Q1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)

# Q2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
# print(dict1)

# Q3

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

# Q4

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d = {}
for name in employees:
    d[name] = defaults
print(d)

# Q5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d = {}
for item in keys:
    d[item] = sample_dict[item]

print(d)

# Q6

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
new = {}
keys = ["name", "salary"]
for key, value in sample_dict.items():
    if key not in keys:
        new[key] = value

print(new)

# Q7

sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(type(sample_dict.keys()), type(sample_dict.values()))
if 200 in sample_dict.values():
    print('Yes, ', 200, ' is in the dict')

# Q8

sample_dict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

city_value = sample_dict['city']
sample_dict['location'] = city_value
sample_dict.pop('city')
print(sample_dict)

# Q9

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

for sub, grade in sample_dict.items():
    if grade == min(sample_dict.values()):
        print('The lowest grade is in: ', sub, ', and it is: ', grade)


# Q10

sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)

# 10 list problems
# Q1

list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

# Q2

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res = []
for i in range(len(list1)):
    res.append(list1[i]+list2[i])

print(res)

# Q3

numbers = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print(numbers)

# Q4

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = []

for i in list1:
    for j in list2:
        res.append(i+j)
print(res)

# Q5

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(list1[i], list2[::-1][i])


# Q6

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i == '':
        list1.remove(i)

print(list1)

# Q7

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Q8

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2] += sub_list
print(list1)

# Q9

list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

# Q10

list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        list1.remove(i)

print(list1)

# PyNative 10 Set Questions
# Q1

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

for item in sample_list:
    sample_set.add(item)
print(sample_set)

# Q2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s = set()
s = set1.intersection(set2)
print(s)

# Q3

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
new_s = set1.union(set2)
print(new_s)

# Q4

set1 = {10, 20, 30}
set2 = {20, 40, 50}
dif_set = set1.difference(set2)
print(dif_set)

# Q5

set1 = {10, 20, 30, 40, 50}
to_remove = {10, 20, 30}
set1 = set1.difference(to_remove)
print(set1)

# Q6

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
union_s = set1.union(set2)
inter_s = set1.intersection(set2)
u_minus_int = union_s.difference(inter_s)
print(u_minus_int)

# Q7
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
commons = set()
for item in set1:
    if item in set2:
        commons.add(item)

print(commons)

# Q8

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
intersect = set1.intersection(set2)
set1 = set1.difference(set2)
print(set1)
for item in set2:
    if item not in intersect:
        set1.add(item)

print(set1)

# Q9

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1 = set1.intersection(set2)
print(set1)








