# Find the height of Binary Tree
# The height of a node is the number of edges from the node to the deepest leaf
# The height of a tree is the number of edges from the root to the deepest leaf

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, val);
        left_tree = self.BinaryTreeNode(data = val)
        self.left = left_tree
        return left_tree

    def insert_right(self, val):
        right_tree = self.BinaryTreeNode(data = val)
        self.right = right_tree
        return right_tree


def height(root):
    if root is None:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)




