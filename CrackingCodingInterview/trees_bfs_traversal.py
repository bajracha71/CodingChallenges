# Given a binary tree, design an algorithm which creates
# a linked list of all nodes at each depth
# ( eg. if you have a tree of depth D, you will have D linked list )

# Note: For this problem instead of creating a linked list I will
# create a list of array

# We will use queue for this solution

import queue


class BinaryTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

    def insertLeft(self, val):
        leftTree = BinaryTreeNode(val)
        self.left = leftTree
        return leftTree

    def insertRight(self, val):
        rightTree = BinaryTreeNode(val)
        self.right = rightTree
        return rightTree


def createTree():
    root = BinaryTreeNode(3)
    left = BinaryTreeNode(9)
    right = BinaryTreeNode(20)
    root.left = left
    root.right = right

    rightleft = BinaryTreeNode(15)
    rightright = BinaryTreeNode(7)

    root.right.left = rightleft
    root.right.right = rightright

    return root


def bfs_levelOrderTraversal(root):

    result = []

    if not root: # root is None
        return result

    q = queue.Queue()
    q.put(root)

    while q.qsize() > 0:

        size = q.qsize()
        # process every current number of nodes in the queue
        currlevel = []
        for i in range(size):
            currnode = q.get()
            currlevel.append(currnode.data)

            leftnode = currnode.left
            rightnode = currnode.right

            if leftnode: # leftnode is not None
                q.put(leftnode)

            if rightnode:
                q.put(rightnode)

        result.append(currlevel)

    return result

if __name__ == "__main__":
    root = createTree()
    res = bfs_levelOrderTraversal(root)
    print(res)
