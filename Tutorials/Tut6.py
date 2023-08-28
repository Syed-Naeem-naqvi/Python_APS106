for i in range(5):
    print(i)
print('______')

for i in range(7,-2,-2):
    print(i)
print('______')

for i in range(10):
    if i is 3:
        continue
    print(i)
print('______')

for i in range(10):
    if i is 3:
        break
    print(i)
print('______')

for i in range(10, 13):
    for j in range(1, 5):
        print(i, j)

# Q1
# sum 1*1, 1*2, 3*1, 3*2 = 12
print('______')

total = 0
for x in range(1, 5, 2):
    for y in range(1, 3):
        total += x * y

print(total)

# Q2: wlk

# Q3


def alternate(l1, l2):
    s1 = ['a','b','c']
    s2 = [1,2,3]
    output = []
    for i in range(len(s1)):
        if i % 2 == 0:
            output.append(s1[i])
        elif i % 2 != 0:
            output.append(s2[i])

    return output


s1 = ['a','b','c']
s2 = [1,2,3]

print(alternate(s1,s2))