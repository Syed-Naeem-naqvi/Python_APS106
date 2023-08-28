L = [1,2,3,4,4,5,5,6,7,8,9,9]
new = []
dupes = set()
for i in L:
    if i not in new:
        new.append(i)
    elif i in new:
        dupes.add(i)

# print(dupes)




