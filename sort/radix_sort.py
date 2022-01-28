'''
Radix Sort
O(n + k)

create 10 buckets (queues) for each digit (0 to 9)
    for each digit placing
        for each element in list
            move element into respective bucket
        for each bucket, starting from smallest digit
            while bucket is non-empty
                restore element to list
'''

from json.tool import main
import random


def radix_sort(array: list):
    pass

def radix_sort_test():
    low, high = 0, 100
    array = [random.randint(low, high) for _ in range(0, 10)]
    print(array)
    array = radix_sort(array)
    print(array)

if __name__ == '__main__':
    radix_sort_test()

