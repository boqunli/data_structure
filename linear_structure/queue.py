'''
the queue data structure

member functions
    enqueue
    dequeue
    front
'''

from linked_list import *

class queue(linked_list):
    def __init__(self, l: list=[]) -> None:
        linked_list.__init__(self, l)
    
    def enqueue(self, key):
        linked_list.insert_back(self, key)
    
    def dequeue(self):
        return linked_list.pop_front(self)
    
    def front(self):
        return self.first.key

if __name__ == '__main__':    
    q = queue([1, 2, 3])
    q.print_list()


