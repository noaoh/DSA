# This algorithm takes O(N^2) worst case, because the array takes a maximum
# of N for loops to swap N completely out of order elements
# This algorithm takes O(N^2) average case, because most of the time the
# array's elements are completely out of order
# This algorithm takes O(N) best case, because it checks if all the values are
# in order using swapped, so if all the values are in order, swapped will be False,
# so sort will be True
def bubble_sort(array):
    length = len(array)
    sort = False
    while not sort:
        swapped = False
        for x in range(1,length):
            # if this pair is out of order
            if array[x-1] > array[x]:
                # swap them, and remember that they were swapped
                array[x-1], array[x] = array[x], array[x-1]
                swapped = True
        # if no pairs were swapped (False), the array was sorted (True)
        sort = not swapped
    return array
