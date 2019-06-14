# Balanced Binary Tree
# -------------------- #

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node
# never differ by more than 1.

# Definition for a binary tree node.

class BinaryTreeNode(object):
    def __init__(self, data = None, left = None, right = None):
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


def isBalanced_BF(root):
    
    if root is None:
        return True
    
    def getHeight(root):
        if root is None:
            return -1
        
        lh = getHeight(root.left)
        rh = getHeight(root.right)

        return 1 + max(lh, rh)

    
    height_diff = abs( getHeight(root.left) - getHeight(root.right)) 

    if height_diff < 1 and isBalanced_BF(root.left) and isBalanced_BF(root.right):
        return True
    
    return False


import unittest

class Test(unittest.TestCase):


    def test1(self):

        root = BinaryTreeNode(1)
        left = root.insert_left(2)
        right = root.insert_right(3)

        self.assertTrue(isBalanced_BF(root))

    def test_tree_with_one_root(self):
        root = BinaryTreeNode(1)
        self.assertTrue(isBalanced_BF(root))

    def test_null_tree(self):
        root = None
        self.assertTrue(isBalanced_BF(root))

    def test_unbalanced_tree(self):

        root = BinaryTreeNode(1)
        left = root.insert_left(2)
        right = root.insert_right(3)

        left_left = left.insert_left(5)
        left_left_left = left_left.insert_left(10)
        left_left_left.insert_left(20)


        self.assertEqual(isBalanced_BF(root), False)

    
unittest.main(verbosity=2)
    

    
