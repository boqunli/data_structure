'''
Merge Sort
O(n^2)

split each element into partitions of size 1
recursively merge adjacent partitions
  for i = leftPartIdx to rightPartIdx
    if leftPartHeadValue <= rightPartHeadValue
      copy leftPartHeadValue
    else: copy rightPartHeadValue; Increase InvIdx
copy elements back to original array
'''

from json.tool import main
from operator import le
import random

def merge(array: list, left: int, mid: int, right: int):
    m = mid - left + 1
    n = right - mid
    l, r = [], []
    for i in range(0, m):
        l.append(array[left + i])
    for j in range(0, n):
        r.append(array[mid + j + 1])
    l.append(float('inf'))
    r.append(float('inf'))
    i = j = 0
    for k in range(left, right + 1):
        if l[i] <= r[j]:
            array[k] = l[i]
            i += 1
        else:
            array[k] = r[j]
            j += 1

def merge_sort(array: list, left: int, right: int) -> list:
    if (left < right):
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def merge_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    merge_sort(array, 0, 9)
    print(array)

if __name__ == '__main__':
    merge_sort_test()

