def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    if array[high] < array[i + 1]:
        array[high], array[i + 1] = array[i + 1], array[high]

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)
