# 4.1 Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined
# to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.


import unittest


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, val):
        left_subTree = BinaryTreeNode(data=val)
        self.left = left_subTree
        return left_subTree

    def insert_right(self, val):
        right_subTree = BinaryTreeNode(data=val)
        self.right = right_subTree
        return right_subTree


def isBalanced(root):

    def helper(node):
        if node is None:
            return {"balancedQ": True, "height": -1}

        leftcheck = helper(node.left)
        if not leftcheck["balancedQ"]:
            return {"balancedQ": False, "height": -2}

        rightcheck = helper(node.right)
        if not rightcheck["balancedQ"]:
            return {"balancedQ": False, "height": -2}

        lh = leftcheck["height"]
        rh = rightcheck["height"]
        balancedcheck = abs(lh - rh) <= 1
        node_height = 1 + max(lh, rh)

        return {"balancedQ": balancedcheck, "height": node_height}

    result = helper(root)
    return result["balancedQ"]


class Test(unittest.TestCase):

    def test1(self):

        root = BinaryTreeNode(1)
        left = root.insert_left(2)
        right = root.insert_right(3)

        self.assertTrue(isBalanced(root))

    def test_tree_with_one_root(self):
        root = BinaryTreeNode(1)
        self.assertTrue(isBalanced(root))

    def test_null_tree(self):
        root = None
        self.assertTrue(isBalanced(root))

    def test_unbalanced_tree(self):

        root = BinaryTreeNode(1)
        left = root.insert_left(2)
        right = root.insert_right(3)

        left_left = left.insert_left(5)
        left_left_left = left_left.insert_left(10)
        left_left_left.insert_left(20)

        self.assertEqual(isBalanced(root), False)


unittest.main(verbosity=2)

# Complexity:
# Time: O(n) where n is the number of nodes
# Space: O(h) where h is the height of Binary Tree
