# Add to set

L = [1,1,2,3,4,5]
s = set()
for i in L:
    s.add(i)

print(s)

# Look through tuple
t = (1,2,3,4,5)
for i in t:
    print(i)

# Swap with tuple
a = 3
b = 4
print(a,b)
(a, b) = (b, a)
print(a,b)

# Unpack
v = (1,2,3)
x,y,z = v
print(x, y, z)

# Index tuple
t2 = ([2,3,4],[5])
t2[0][1] = 99
print(t2)

# Set operations
s1 = {0,1,2,3}
s2 = {3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

# Dictionaries
wages = {'Bob': 44, 'Joe': 33, 'Joe_the_second': 34}


