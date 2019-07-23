# 4.5 Implement a function to check if a binary tree is a binary search tree

# For each node in binary tree, all the nodes in its left subtree is less
# than current node and all the nodes in its right subtree is more than
# current node

# Use recursion and pre-order traversal techniques (DLR)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def isValidBST(root):
    def helper(node, lower, upper):
        if node is None:
            return True

        val = node.data
        if val <= lower or val >= upper:
            return False

        checkleft = helper(node.left, lower, val)
        checkright = helper(node.right, val, upper)

        if checkleft and checkright:
            return True

        return False

    result = helper(root, float("-inf"), float("inf"))
    return result
