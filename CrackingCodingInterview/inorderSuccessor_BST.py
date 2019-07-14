# 4.6 (b) Write an algorithm to find the next node (i.e in-order successor)
# of a given node in a binary search tree without pareent link.


# Without parelent link

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p is None:
            return None

        def leftmostchild(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def find_ancestor(root, node):
            curr_root = root
            nodeval = node.val
            succ = None

            while curr_root and curr_root.val != nodeval:

                if nodeval < curr_root.val:
                    # ancestor is in leftsubtree of root
                    succ = curr_root
                    curr_root = curr_root.left

                if nodeval > curr_root.val:
                    curr_root = curr_root.right

            return succ

        rightsubtree = p.right

        if rightsubtree:
            return leftmostchild(rightsubtree)
        else:
            return find_ancestor(root, p)


