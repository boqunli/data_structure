import networkx as nx
import matplotlib.pyplot as plt
import random

class RBTreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size = None

class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

def LeftRotate(T: RBTree, x: RBTreeNode):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def RightRotate(T: RBTree, x: RBTreeNode):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

def RBInsert(T: RBTree, z: RBTreeNode):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == T.nil:
        T.root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'red'
    RBInsertFixup(T, z)
    return z.data, '颜色为', z.color

def RBInsertFixup(T: RBTree, z: RBTreeNode):
    while z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    LeftRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                RightRotate(T,z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    RightRotate(T, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                LeftRotate(T, z.parent.parent)
    T.root.color = 'black'

def RBTransplant(T: RBTree, u: RBTreeNode, v: RBTreeNode):
    if u.parent == T.nil:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent

def RBDelete(T: RBTree, z: RBTreeNode):
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        RBTransplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        RBTransplant(T, z, z.left)
    else:
        y = TreeMinimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            RBTransplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        RBTransplant(T, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color
    if y_original_color == 'black':
        RBDeleteFixup(T, x)
#红黑树的删除
def RBDeleteFixup(T: RBTree, x: RBTreeNode):
    while x != T.root and x.color == 'black':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                LeftRotate(T, x.parent)
                w = x.parent.right
            if w.left.color == 'black' and w.right.color == 'black':
                w.color = 'red'
                x = x.parent
            else:
                if w.right.color == 'black':
                    w.left.color = 'black'
                    w.color = 'red'
                    RightRotate(T, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 'black'
                w.right.color = 'black'
                LeftRotate(T, x.parent)
                x = T.root
        else:
            w = x.parent.left
            if w.color == 'red':
                w.color = 'black'
                x.parent.color = 'red'
                RightRotate(T, x.parent)
                w = x.parent.left
            if w.right.color == 'black' and w.left.color == 'black':
                w.color = 'red'
                x = x.parent
            else:
                if w.left.color == 'black':
                    w.right.color = 'black'
                    w.color = 'red'
                    LeftRotate(T, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 'black'
                w.left.color = 'black'
                RightRotate(T, x.parent)
                x = T.root
    x.color = 'black'

def TreeMinimum(T: RBTree, x: RBTreeNode):
    while x.left != T.nil:
        x = x.left
    return x
#中序遍历
def Midsort(x):
    if x!= None:
        Midsort(x.left)
        if x.data!=0:
            print('data:', x.data,'x.parent',x.parent.data)
        Midsort(x.right)

def create_graph(G: nx.DiGraph, node:RBTreeNode, pos={}, x=0, y=0, layer=1):
    pos[node.data] = (x, y)
    if node.left and node.left != T.nil:
        G.add_edge(node.data, node.left.data)
        G.nodes[node.data]['color'] = node.color
        G.nodes[node.left.data]['color'] = node.left.color
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right and node.right != T.nil:
        G.add_edge(node.data, node.right.data)
        G.nodes[node.data]['color'] = node.color
        G.nodes[node.right.data]['color'] = node.right.color
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node, path='./tree.png'):  
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(20, 7)) 
    colors=list(zip(*list(graph.nodes.data('color'))))[1]
    nx.draw_networkx(graph, pos, ax=ax, node_size=1000, node_color=colors, font_color='w')
    plt.savefig(path)

if __name__ == '__main__':
    nodes = list(range(1, 40))
    random.shuffle(nodes)
    T = RBTree()
    for node in nodes:
        RBInsert(T,RBTreeNode(node))
    draw(T.root)
    