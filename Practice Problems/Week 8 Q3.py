L = list(range(1001))
print(L)
target = 3


def binary_search(L, target):
    start = 0
    end = len(L) - 1
    while end >= start:
        mid = (start + end)//2
        if target == L[mid]:
            return mid
        elif target > L[mid]:
            start = mid - 1
        elif target < L[mid]:
            end = mid + 1
    return -1


print(binary_search(L, target))
