''' 
node of a binary tree
'''
import sys
sys.path.append('..')

import networkx as nx
import matplotlib.pyplot as plt

class node:
    
    def __init__(self, data=0, l=None, r=None, p=None):
        self.data = data
        self.left = l
        self.right = r
        self.parent = p

    def __str__(self) -> str:
        return str(self.data)

'''
bst:
right > root > left
'''

class binary_search_tree:

    def __init__(self, root=None) -> None:
        self.root = root

    def height(self) -> int:
        def helper(root: node):
            if not root:
                return 0
            return 1 + max(helper(root.left), helper(root.right))
        return helper(self.root)

    def is_empty(self):
        return False if self.root else True

    def preorder(self, f):
        def helper(root: node, f):
            if root:
                f(root)
                helper(root.left, f)
                helper(root.right, f)
        helper(self.root, f)    

    def inorder(self, f):
        def helper(root: node, f):
            if root:
                helper(root.left, f)
                f(root)
                helper(root.right, f)
        helper(self.root, f)

    def postorder(self, f):
        def helper(root: node, f):
            if root:
                helper(root.left, f)
                helper(root.right, f)
                f(root)
        helper(self.root, f)
      
    def levelorder(self, f):
        q = []
        if self.root == None:
            return
        q.append(self.root)
        while q:
            top = q.pop(0)
            f(top)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)

    def tree_search(self, k):
        def helper(node: node, k):
            if not node:
                return node
            if node.data == k:
                return node
            if node.data > k:
                return helper(node.left, k)
            else:
                return helper(node.right, k)
        return helper(self.root, k)

    def iterative_tree_search(self, k):
        if not self.root:
            return None
        x = self.root
        while x.data != k:
            if k < x.data:
                x = x.left
            else:
                x = x.right
            if not x:
                return x
        return x

    def tree_minimum(self, xx:node):
        x = xx
        while x.left:
            x = x.left
        return x

    def tree_maximum(self, xx:node):
        x = xx
        while x.right:
            x = x.right
        return x
    
    def tree_successor(self, xx:node):
        x = xx
        if x.right:
            return self.tree_minimum(x.right)
        y = x.parent
        while y:
            if x != y.right:
                break
            x = y
            y = y.parent
        return y
    
    def tree_predecessor(self, xx:node):
        x = xx
        if x.left:
            return self.tree_maximum(x.left)
        y = x.parent
        while y:
            if x != y.left:
                break
            x = y
            y = y.parent 
        return
    
    def tree_insert(self, data):
        z = node(data)
        y = None
        x = self.root
        while x:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right 
        z.parent = y
        if not y:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        
    def transplant(self, u:node, v:node):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent
    
    def tree_delete(self, z:node):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


def create_graph(G, node:node, pos={}, x=0, y=0, layer=1):
    pos[node.data] = (x, y)
    if node.left:
        G.add_edge(node.data, node.left.data)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.data, node.right.data)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(10, 6))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=1000)
    plt.savefig('./t.png')


if __name__ == '__main__':
    t = binary_search_tree()
    t.tree_insert(4)
    t.tree_insert(2)
    t.tree_insert(1)
    t.tree_insert(3)
    t.tree_insert(6)
    t.tree_insert(5)
    t.tree_insert(7)
    n = t.tree_search(4)
    draw(n)
    t.tree_delete(n)
    draw(t.root)    
    
    
