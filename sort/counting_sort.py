'''
Counting Sort
O(n + k)

create key (counting) array
for each element in list
  increase the respective counter by 1
for each counter, starting from smallest key
  while counter is non-zero
    restore element to list
    decrease counter by 1
'''

from json.tool import main
import random


def counting_sort(array: list, k: int):
    n = len(array)
    b = [0 for _ in range(0, n)]
    c = [0 for _ in range(0, k + 1)]
    for i in range(0, n):
        c[array[i]] += 1
    for i in range(1, k + 1):
        c[i] = c[i] + c[i-1]
    for j in range(n-1, -1, -1):
        b[c[array[j]]-1] = array[j]
        c[array[j]] -= 1
    return b

def counting_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    array = counting_sort(array, 100)
    print(array)

if __name__ == '__main__':
    counting_sort_test()

