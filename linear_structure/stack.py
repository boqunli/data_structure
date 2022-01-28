'''
stack data structure

member functions
    pop
    push
    top
'''

from linked_list import *

class stack(linked_list):
    def __init__(self, l: list=[]) -> None:
        linked_list.__init__(self, l)
    
    def push(self, key):
        linked_list.insert_back(self, key)
    
    def pop(self):
        return linked_list.pop_back(self)
    
    def top(self):
        return self.last.key

if __name__ == '__main__':    
    q = stack([1, 2, 3])
    q.print_list()
    print(q.top())
