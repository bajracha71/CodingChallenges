# Design an algorithm and write code to find the first common ancestor of two
# nodes in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree
# Also parent link is not available.

class BinaryTreeNode:
    def __init__(self, data=data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

def lowest_common_ancestors(root, p, q):

    def lca_helper(root):

        # Base case
        if root is None or root == p or root == q:
            return root

        # Post-order traversal
        left = lca_helper(root.left)
        right = lca_helper(root.right)

        # when left and righ is not None

        if left and right:
            return True
        if left:
            return left
        else:
            return right

    return lca_helper(root)
