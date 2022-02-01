import math 

class FibHeapNode:
    '''
    Node of FibHeap
             parent
               |
       left<- key ->right
               |
             child
    '''

    def __init__(self, key) -> None:
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.key = key        
        self.degree = 0
        self.marked = False
    
    def set_child(self, child):
        child.parent = self
        self.degree += 1
        if self.child == None:
            self.child = child
            child.left = child
            child.right = child
        else:
            c = self.child
            child.right = c
            child.left = c.left
            child.left.right = child    

    def __str__(self) -> str:
        res = "[root %d : " % self.key
        if self.child != None:
            child = self.child  
            left = child.left
            res += ("%d -> " % child.key)
            res += str(child)
            while left != child:
                child = child.right
                res += ("%d -> " % child.key)
                res += str(child)
        res += "] "
        return res
    
    def printNode(self):
        if self.child != None:
            c = self.child
            cl = c.left
            while True:
                print("%d has child: %d" % (self.key,c.key))
                c.printNode()
                if cl==c:
                    break
                c=c.right

    def search_child(self, key):
        iter = self
        while True:
            if iter.key == key:
                return iter
            if iter.child != None:
                res = iter.child.search_child(key)
            if res != None:
                return res
            iter = iter.right
            if iter == self:
                return None

class FibHeap:
    '''
    FibHeap:
    
        min_node <----------> node2 <----------> node3
           |                    |
    <-> child1 <-> child2     child3

    '''
    def __init__(self, num=0, min=None) -> None:
        self.num_nodes = num
        self.min_node = min
        # self.root_list = []
        # self.max_degree = 0

    def insert(self, new_key):
        node = FibHeapNode(new_key)
        if self.min_node == None:
            self.min_node = node    
            node.left = node
            node.right = node
        else:
            node.right = self.min_node
            node.left = self.min_node.left
            node.left.right = node
            self.min_node.left = node
            if node.key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1

    def minimum(self):
        if self.min_node == None:
            print('Heap empty!')
            return None
        return self.min_node.key

    def extract_min(self):
        iter = self.min_node
        if iter != None:
            if iter.child != None:
                iter_child = iter.child
                while iter_child.parent != None:
                    # add iter_child to root list
                    current = iter_child.left
                    iter_child.parent = None
                    iter_child.right = self.min_node
                    iter_child.left = self.min_node.left
                    iter_child.left.right = iter_child
                    self.min_node.left = iter_child
                    iter_child = current
            # remove iter from the root list
            iter.right.left = iter.left
            iter.left.right = iter.right
            iter.child = None
            if iter == iter.right:
                self.min_node = None
            else:
               self.min_node = iter.right
               self.consolidate()
            self.num_nodes -= 1
        return iter  

    def consolidate(self):
        # degrees[d] : node with degree d
        degrees = [None]*int(math.log(self.num_nodes, 2)+1)
        min = self.min_node
        if min == None:
            return
        left = min.left
        while True:
            iter = min
            d = iter.degree
            while degrees[d] != None:
                iter2 = degrees[d]
                if iter2.key < iter.key:
                    iter, iter2 = iter2, iter
                self.link(iter2, iter)
                degrees[d] = None
                d += 1
            degrees[d] = iter
            if min == left:
                break
            min = iter.right

        self.min_node = None
        for nd in degrees:
            if nd != None:
                if self.min_node == None:
                    self.min_node = nd
                    nd.left = nd
                    nd.right = nd
                else:
                    nd.right = self.min_node
                    nd.left = self.min_node.left
                    nd.left.right = nd
                    self.min_node.left = nd
                    if nd.key < self.min_node.key:
                        self.min_node = nd

    def link(self, c:FibHeapNode, p:FibHeapNode):
        # remove c from root list
        c.right.left = c.left
        c.left.right = c.right
        c.parent = p
        p.degree += 1
        c.marked = False
        # set child p.set_child(c)
        if p.child == None:
            p.child = c
            c.left = c
            c.right = c
        else:
            child = p.child
            c.right = child
            c.left = child.left
            c.left.right = c
            child.left = c

    def decrease_key(self, node_victim:FibHeapNode, new_key):
        if node_victim == None:
            print("No node is decreased")
            return 
        if new_key > node_victim.key:
            return
        node_victim.key = new_key
        p = node_victim.parent
        if p != None and node_victim.key < p.key:
            self.cut(node_victim, p)
            self.cascade_cut(p)
        if node_victim.key < self.min_node.key:
            self.min_node = node_victim

    def cut(self, child_node:FibHeapNode, parent_node:FibHeapNode):
        if parent_node.degree == 1:
            parent_node.child = None
            child_node.parent = None
        else:
            if child_node == parent_node.child:
                child_right = child_node.right
                child_right.left = child_node.left
                child_node.left.right = child_node.right
                parent_node.child = child_right
            else:
                child = parent_node.child
                child.left = child_node.left
                child_node.left.right = child_node.right
        parent_node.degree -= 1
        child_node.right = self.min_node
        child_node.left = self.min_node.left
        child_node.left.right = child_node
        self.min_node.left = child_node
        if child_node.key < self.min_node.key:
            self.min_node = child_node
        child_node.parent = None
        child_node.marked = False

    def cascade_cut(self, p:FibHeapNode):
        parent = p.parent
        if parent != None:
            if p.marked == False:
                p.marked = True
            else:
                self.cut(p, parent)
                self.cascade_cut(parent)

    def delete(self, node_victim):
        self.decrease_key(node_victim, self.min_node.key-1)
        res = self.extract_min()
        return res

    def print_heap(self):
        print('\n------------------------Heap-------------------------')
        print("heap size : %d" % self.num_nodes)
        iter : FibHeapNode = self.min_node
        if iter == None:
            return
        print("min_node : %d" % iter.key)
        print(iter)
        iter = iter.right
        while iter != self.min_node:
            print(iter)
            iter = iter.right
        print('-----------------------------------------------------\n')

    def search_node(self, key):
        if key < self.minimum():
            return None
        res = None
        iter = self.min_node
        while True:
            if iter.key == key:
                return iter
            else:
                if iter.child != None:
                    res = iter.child.search_child(key)
                if res != None:
                    return res
                iter = iter.right
                if iter == self.min_node:
                    return None

def MakeHeap()->FibHeap:
    return FibHeap()

def Union(self:FibHeap, that:FibHeap)->FibHeap:
    new_heap = MakeHeap()
    if self.min_node == None or self.min_node.key > that.min_node.key:
        new_heap.min_node = that.min_node
    else:
        new_heap.min_node = self.min_node
    new_heap.num_nodes = self.num_nodes + that.num_nodes
    if self.min_node != None and that.min_node != None:
        self.min_node.right = that.min_node
        that.min_node.left.right = self.min_node.right
        self.min_node.right.left = that.min_node.left
        that.min_node.left = self.min_node
    return new_heap

def main():
    heap:FibHeap = MakeHeap()
    for item in range(1, 11):
        heap.insert(item)
    heap.print_heap()
    node = heap.search_node(10)
    heap.extract_min()
    heap.decrease_key(node, 0)
    heap.print_heap()

if __name__ == '__main__':
    main()  