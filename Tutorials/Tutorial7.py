l = [10, 30, 50, 70, 100]
length = len(l)
min = min(l)
max = max(l)
sum = sum(l)

print(length, min, max, sum)

l2 = ['apple', 'banana','blueberry']
l2.append('pear')

# Extend method needs a list
l2.extend(['pear'])
l2.extend([3])
print(l2)

l2.insert(2, 'peach')
print(l2)

l2.remove('apple')
print(l2)

removed = l2.pop(0)

print(l2, removed)

# count and index

l1 = [2,3]
l2 = l1
l2.append(3)
print(l1)

# Make copies of objects to avoid aliasing

lis = ['a','b','c']
for item in lis:
    print(item)

for ind in range(len(lis)):
    print(lis[ind])


# Q1
# B, C, E don't create the same output

# Q2
# C




