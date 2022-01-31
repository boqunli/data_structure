'''
red black tree
color added to bst
'''

import binary_search_tree

class rb_node(binary_search_tree.node):

    BLACK = 'b'

    RED = 'r'

    def __init__(self, data=0, l=None, r=None, p=None, c=BLACK):
        super().__init__(data, l, r, p)
        self.color = c
    
    