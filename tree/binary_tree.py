
''' 
node of a binary tree
'''
class node:
    
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

class binary_tree:
    
    def __init__(self, root: node=None):
        self.root = root
    
    def height(self) -> int:
        def helper(root: node):
            if not root:
                return 0
            return 1 + max(self.height(root.left), self.height(root.right))
        return helper(self.root)

    def is_empty(self):
        return False if self.root else True

