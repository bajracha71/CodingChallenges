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

