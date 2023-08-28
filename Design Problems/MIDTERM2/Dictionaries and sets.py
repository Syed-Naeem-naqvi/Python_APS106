
# Append
Dic = {'Joe':5,'Bob':7}
Dic['Trent'] = 5
print(Dic)

# Access keys
for i in Dic.keys():
    print(i)

# Access Values
for j in Dic.values():
    print(j)

# Another way to create them
d = dict()
d['First'] = 1
d['Second'] = 2
d['Third'] = 3

# Check membership
print(d)
print('First' in d)

# Store 2 lists of keys and values
dkeys = []
dvalues = []
for i,j in d.items():
    dkeys.append(i)
    dvalues.append(j)

print(dkeys)
print(dvalues)


p = {'s1': 78, 's2': 85, 's3': 68}
grades = []
for i,j in p.items():
    grades.append(j)

max_g = max(grades)
print(grades, max_g)

for i, j in p.items():
    if j == max_g:
        print(i)

