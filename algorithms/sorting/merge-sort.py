def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))

    while len(left) != 0:
        result.append(left.pop(0))

    while len(right) != 0:
        result.append(right.pop(0))

    return result

def merge_sort(array):
    if len(array) <= 1:
        return array

    left = []
    right []
    middle = len(array)/2
    for x in range(0,len(array)):
        if x < middle:
            left.append(array[x])

        else:
            right.append(array[x])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)
