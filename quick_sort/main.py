"""
Description: Efficient sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the
other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays
are then sorted recursively.

Average complexity: O(n * log(n)).
"""
import random


def quick_sort(array, begin, end):
    if begin < end:
        p = partition(array, begin, end)
        quick_sort(array, begin, p - 1)
        quick_sort(array, p, end)


def partition(array, begin, end):
    pivot = array[end]
    i = begin
    for j in range(begin, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i


random_values = [random.randint(0, 1000) for x in range(0, 10000)]
quick_sort(random_values, 0, len(random_values) - 1)
