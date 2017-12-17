# takes O(N) because it has to check N values in the array
# before finding the proper position
def insert_helper(array,pos):
    value = array[pos]
    del array[pos]
    while value < array[pos-1] and pos != 0:
        pos -= 1

    array.insert(pos,value)

# Takes O(N) best case, because insert_helper checks before
# sorting input, so if each item is in the right position,
# insert_helper takes O(1), and insert_helper is called N
# Takes O(N^2) worst case and average case, because if all/most
# values are out of order, insert_helper takes O(N), and is called
# N times, which is costly
def insertion_sort(array):
    for x in range(1,len(array)):
        insert_helper(array,x)

    return array

f = [10,8,6,4,2,9,7,5,3,1]
insertion_sort(f)

g = [312,3,212,1,2,4,43,213,13]
insertion_sort(g)

h = [1,3,2,5,4,7,6,9,8,10]
insertion_sort(h)
