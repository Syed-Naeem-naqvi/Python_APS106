# Keys need to be hashable, or immutable
# keys are also unique

d = {'a': '1','b': '2'}
dinv = {}
for key, value in d.items():
    old_key = key
    old_val = value
    dinv[old_val] = old_key

print(dinv)

t = [(1,2), (2,3)]
length = len(t)

x_mean, y_mean = 0,0

for i in range(len(t[0])):
    x_mean += t[i][0]
    y_mean += t[i][1]

x_mean = x_mean/length
y_mean = y_mean/length

print(x_mean, y_mean)
