# Trees and Graphs

## Binary Tree

### Binary Tree Node

```python

class BinaryTreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insertLeftSubTree(self, data):
        leftsubtree = BinaryTreeNode(data=data)
        self.left = leftsubtree
        return leftsubtree

    def insertRightSubTree(self,data):
        rightSubTree = BinaryTreeNode(data=data)
        self.right = rightSubTree
        return rightSubTree
```

### Height of Binary Tree

- Height of Binary Tree is the number of edges from root to the deepest leaf.
- If root is None, height = -1
- If root does not have any children, height = 1
- Computing height using recursive methods, heigt(root) = 1 + max(height(root.left), height(root.right))

```python
def treeHeight(root):
    if root is None:
        return -1

    leftSubTreeHeight = treeHeight(root.left)
    rightSubTreeHeight = treeHeight(root.right)
    return 1 + max(leftSubTreeHeight, rightSubTreeHeight)
```

### Check if a given Binary Tree is height balanced

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(root):
            if not root:
                return {"BalancedQ": True, "Height": -1}

            checkleft = helper(root.left)

            if not checkleft["BalancedQ"]:
                return {"BalancedQ": False, "Height": -2}

            checkright = helper(root.right)

            if not checkright["BalancedQ"]:
                return {"BalancedQ": False, "Height": -2}

            lh = checkleft["Height"]
            rh = checkright["Height"]

            check = abs(lh - rh) <= 1

            return {"BalancedQ": check, "Height": 1 + max(lh,rh)}

        return helper(root)["BalancedQ"]
```
