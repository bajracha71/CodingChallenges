# 4.6 Write an algorithm to find the next node (i.e in-order successor)
# of a given node in a binary search tree. You may assume that each
# node has a link to its parents.
# -https://leetcode.com/problems/inorder-successor-in-bst-ii/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':

        def leftmostchild(node):
            curr = node
            while curr.left:
                curr = curr.left

            return curr

        def findSuccessorAncestor(node):
            par = node.parent
            curr = node

            while par and par.left != curr:
                curr = par
                par = par.parent

            return par

        if node is None:
            return node

        rightNode = node.right

        # When rightNode is not None then successor is in leftsubtree
        if rightNode:
            return leftmostchild(rightNode)
        else:
            # When rightNode is None then walk up through the node and find
            # ancestor who is the successor
            return findSuccessorAncestor(node)
