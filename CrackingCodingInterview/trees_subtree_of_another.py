# 4.8 [You have two very large binary trees: T1,
# with millions of nodes and T2, with hundres of nodes.
# Create an algorithm to decide if T2 is a subtree of T1]
# (https://leetcode.com/problems/subtree-of-another-tree/)

# - A tree T2 is a subtree of T1 if there exists a node n in T1
# such that the subtree of n is identical to T2. That is, if you
# cut off the tree at node n, the two trees would be identical.


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def identicalTree(s, t):

            if s is None and t is None:
                return True

            if s and t and s.val == t.val:
                return identicalTree(s.left, t.left) and identicalTree(s.right, t.right)

            return False

        if s is None:
            return False

        # Pre-order traversal
        if t is None or identicalTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


# Time Complexity: Worst Case O(m n)
# Space Complexity O(log(m) + log(n))
