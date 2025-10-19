

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

comper = 0
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if low > high:
        return -1


    midpoint = (low + high) // 2

    comper += 1

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

print(binary_search([1,2, 3, 3, 4, 4, 4, 5, 6, 9, 9, 9, 10], 10))
print(comper)