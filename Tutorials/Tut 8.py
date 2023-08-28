from itertools import combinations

# Tut 8 (Week 9)

L = [1,1,2,3,3]
to_find = [1,2,3]

count = 0
for a in L:
    for b in L:
        for c in L:
            comp = [a, b, c]
            if comp == to_find:
                count += 1
# print(count)  # gives 4 as expected

# Thus, run points is run length times count

L2 = [1,1,2,3]
count2 = 0
for v1 in L2:
    for v2 in L2:
        for v3 in L2:
            if [v1, v2, v3] == to_find:
                count2 += 1
# print(count2)  # gives 2 as expected

L3 = [1, 2, 2, 3, 3, 3]  # Should give 6
count3 = 0
for c1 in L3:
    for c2 in L3:
        for c3 in L3:
            if [c1, c2, c3] == to_find:
                count3 += 1

# print(count3)  # gives 6 as expected

# Tutorial questions


# def combine(data):
#     res = {}
#     for subdict in data:
#         for key, value in subdict.items():
#             if key == 'item':
#                 if subdict[key] not in res:
#                     key_to_add = res['item']
#                     val_to_add = res['amount']
#                     res[key_to_add] = val_to_add
#                 elif subdict[key] in res:
#                     val_to_add = res['amount']
#                     res[key] = val_to_add
#     return res


# data1 = [{'item': 'i1', 'amount': 400}, {'item': 'i2', 'amount': 300}, {'item': 'i1', 'amount': 750}]
# print(combine(data1))
