
''' 
node of a binary tree
'''
import sys
sys.path.append('..')

from linear_structure.linked_list import linked_list

import networkx as nx
import matplotlib.pyplot as plt

class node:
    
    def __init__(self, data=0, l=None, r=None):
        self.data = data
        self.left = l
        self.right = r

    def __str__(self) -> str:
        return str(self.data)

'''
simple binary tree
'''
class binary_tree:
    
    def __init__(self, root: node=None):
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
        q = linked_list()
        if self.root == None:
            return
        q.insert_back(self.root)
        while not q.is_empty():
            top = q.pop_front()
            f(top)
            if top.left:
                q.insert_back(top.left)
            if top.right:
                q.insert_back(top.right)
        

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
    n1 = node(1)
    n2 = node(2)
    n3 = node(3, n1, n2)
    n4 = node(4)
    n5 = node(5)
    n6 = node(6, n4, n5)
    n7 = node(7, n3, n6)
    n8 = node(8)
    n9= node(9, n7, n8)
    t = binary_tree(n9) 
    t.preorder(lambda x: print(x, end=' '))
    print('\nheight = %d' % t.height())
    t.levelorder(lambda x: print(x, end=' '))
    print('\nvisualized in ./t.png')
    draw(n9)
