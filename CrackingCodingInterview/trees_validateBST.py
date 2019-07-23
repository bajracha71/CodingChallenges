# 4.5 Implement a function to check if a binary tree is a binary search tree

# For each node in binary tree, all the nodes in its left subtree is less
# than current node and all the nodes in its right subtree is more than
# current node

# Use recursion and pre-order traversal techniques (DLR)
# Min/Max trick


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def isValidBST(root):
    def isBST(node, lower, upper):
        if node is None:
            return True

        # Get node value
        val = node.data

        # Check condition to be binary search tree
        if val <= lower or val >= upper:
            return False

        # Check left and right subtree
        checkleft = isBST(node.left, lower, val)
        checkright = isBST(node.right, val, upper)

        return (checkleft and checkright)

    lower = float("-inf")
    upper = float("inf")
    return isBST(root, lower, upper)
