# Print elements of binary tree using level order traversal
# or BFS using queue

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


def printLevelOrder(root):
    if not root:
        return

    q = queue.Queue()
    q.put(root)

    while q.qsize() > 0:
        currnode = q.get()
        print(currnode.data)

        left = currnode.left
        if left:
            q.put(left)

        right = currnode.right
        if right:
            q.put(right)


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

if __name__ == "__main__":
    root = createTree()
    printLevelOrder(root)
