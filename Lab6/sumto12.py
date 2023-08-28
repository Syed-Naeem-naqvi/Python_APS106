from itertools import combinations

numbers = [9, 2, 3, 3, 4]
target = 15

result = []
for i in range(2, len(numbers)+1):
    combos = list(combinations(numbers, i))
    for combo in combos:
        if sum(combo) == 15:
            result.append(combo)

print(result)

points = len(result)*2
