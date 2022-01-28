'''
linked_list data structure

member functions
    insert_back
    insert_front
    pop_back
    pop_front
    erase_at
    insert_at
    erase_key
    insert_after
    print_list
'''

class node:
    '''
    node of the linked list
    '''
    def __init__(self, key=0):
        self.key = key
        self.prev = None
        self.next = None   
    
    def __str__(self) -> str:
        if self.next:
            return str(self.key) + " -> "
        else:
            return str(self.key)

class linked_list:
    '''
    doubly linked list data structure
    '''
    def __init__(self, l: list = []) -> None:
        self.first = None
        self.last = None
        if len(l) > 0:
            for i in l:
                self.insert_back(i)
    
    def is_empty(self):
        if self.first == None and self.last == None:
            return True
        return False

    def insert_back(self, key):
        new_node = node(key)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        
    def insert_front(self, key):
        new_node = node(key)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.first.prev = new_node
            new_node.next = self.first
            self.first = new_node

    def pop_back(self):
        victim = self.last
        if self.is_empty():
            print('Cannot pop from empty list!')
            return None
        if not victim.prev:
            self.first = None
            self.last = None
        else:
            self.last = victim.prev
            self.last.next = None
        return victim.key
    
    def pop_front(self):
        victim = self.first
        if self.is_empty():
            print('Cannot pop from empty list!')
            return None
        if not victim.next:
            self.first = None
            self.last = None
        else:
            self.first = victim.next
            self.first.prev = None
        return victim.key

    def traverse(self, f):
        it = self.first
        while it:
            f(it)
            it = it.next
    
    def __str__(self) -> str:
        it = self.first
        res = '[ '
        while it:
            if it.next:
                res += str(it.key) + ' -> '
            else:
                res += str(it.key)
            it = it.next
        return res + ' ]'
    
    def __sizeof__(self) -> int:
        it = self.first
        count = 0
        while it:
            count += 1
            it = it.next
        return count

    def __eq__(self, __o) -> bool:
        i, j = self.first, __o.first
        if len(self) != len(__o):
            return False
        while i and j:
            if i.key != j.key:
                return False
            i, j = i.next, j.next
        return True
        
    def print_list(self):
        print('[ ', end='')
        self.traverse(lambda x : print(x, end=''))
        print(' ]')

    def to_array(self):
        it = self.first
        res = []
        while it:
            res.append(it.key)
            it = it.next
        return res
    
    def clear(self):
        self.first = None
        self.last = None        
    
    def search(self, value):
        it = self.first
        while it:
            if it.key == value:
                return it
            it = it.next
        return None


    def reverse(self):
        pass

    def sort(self):
        pass

    def insert_at(self, postion=0):
        pass

    def insert_after(self, key):
        pass

    def erase_key(self, key):
        pass

    def erase_at(self, postition=0):
        pass

def linked_list_test():
    l1 = linked_list()
    l1.insert_back(1)
    l1.insert_front(0)
    l1.insert_front(-1)
    print(l1)
    l2 = linked_list([1, 2, 3, 4, 5])
    l2.pop_back()
    l2.pop_front()
    print(l2)
    l2.print_list()
    print(l2.to_array())
    l3 = linked_list([1, 2, 3])
    

if __name__ == '__main__':
    linked_list_test()


    
