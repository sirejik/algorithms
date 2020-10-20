"""
Description: The sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if
they are in the wrong order.

Average complexity: O(n^2).
"""
import random


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


random_values = [random.randint(0, 1000) for x in range(0, 10000)]
bubble_sort(random_values)
