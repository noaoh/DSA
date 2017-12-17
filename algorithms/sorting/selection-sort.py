# takes O(N), where N = (array.length() - 1) - n
# because it has to iterate through each value in the array
def smallest_idx(array,n):
    return array.index(min(array[n:]))

# takes O(N^2) in all cases, because it has to apply the
# smallest_idx function N times, so N * N = N^2
# Only does N swaps, so useful if memory is limited so using
# multiple temp variables is unfeasible

def selection_sort(array):
    for x in range(0,len(array)):
        smallest_index = smallest_idx(array,x)
        array[x], array[smallest_index] = array[smallest_index], array[x]

    return array
