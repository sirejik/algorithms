import random


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


random_values = [random.randint(0, 1000) for x in range(0, 10000)]
bubble_sort(random_values)
