'''
Bubble Sort
O(n^2)

do
  swapped = false
  for i = 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap(leftElement, rightElement)
      swapped = true; ++swapCounter
while swapped
'''

from json.tool import main
import random


def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    # return array


def bubble_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    bubble_sort(array)
    print(array)

if __name__ == '__main__':
    bubble_sort_test()

