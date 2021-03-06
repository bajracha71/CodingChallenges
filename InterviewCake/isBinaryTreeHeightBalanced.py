# Balanced Binary Tree
# -------------------- #

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node
# never differ by more than 1.

# Definition for a binary tree node.

import unittest


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, val):
        left_subTree = BinaryTreeNode(data = val)
        self.left = left_subTree
        return left_subTree

    def insert_right(self, val):
        right_subTree = BinaryTreeNode(data = val)
        self.right = right_subTree
        return right_subTree


def isBalanced( root):

    def isBalancedHelper(root):
        if root is None:
            return -1

        left_height = isBalancedHelper(root.left)

         # if the left subtree is not balanced, then left_height > 1
        # then this tree is not balanced


        right_height = isBalancedHelper(root.right)


        # if the difference in height is greater than 1, then
        # the tree is not balanced

        h_diff = abs(left_height - right_height)
        if h_diff > 1:
            raise Exception("unbalanced tree")

        # otherwise tree is balanced. So when tree is balanced return its height

        return 1 + max(left_height, right_height)

    try:
        return isBalancedHelper(root) >= -1

    except Exception:
        return False


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
# Space: O(h)



