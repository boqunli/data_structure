'''
Insertion Sort
O(n^2)

mark first element as sorted
for each unsorted element X
  extract the element X
  for j = lastSortedIndex down to 0
    if current element j > X
      move sorted element to the right by 1
    break loop and insert X here
'''

from json.tool import main
import random


def insertion_sort(array: list) -> list:
    n = len(array)
    for i in range(1, n):
        tmp = array[i]
        j = i - 1
        while j >= 0 and array[j] > tmp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
    # return array


def insertion_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    insertion_sort(array)
    print(array)

if __name__ == '__main__':
    insertion_sort_test()

