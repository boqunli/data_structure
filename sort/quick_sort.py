'''
Quick Sort
O(n log n)

for each (unsorted) partition
set first element as pivot
  storeIndex = pivotIndex+1
  for i = pivotIndex+1 to rightmostIndex
    if (a[i] < a[pivot]) or (equal but 50% lucky))
      swap(i, storeIndex); ++storeIndex
  swap(pivot, storeIndex-1)

'''

from json.tool import main
import random

def partition(array: list, left: int, right: int):
    pass

def quick_sort(array: list, left: int, right: int):
    pass

def quick_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    quick_sort(array, 0, 9)
    print(array)

if __name__ == '__main__':
    quick_sort_test()

