'''
Selection Sort
O(n^2)

repeat (numOfElements - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
'''

from json.tool import main
import random


def selection_sort(array: list):
    n = len(array)
    for i in range(0, n):
        tmp = i
        for j in range(i, n): 
            if array[j] < array[tmp]:
                tmp = j
        array[i], array[tmp] = array[tmp], array[i]
    # return array


def selection_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    selection_sort(array)
    print(array)

if __name__ == '__main__':
    selection_sort_test()

