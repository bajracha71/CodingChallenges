# Trees and Graphs

## Binary Tress

### Binary Tree Node

```python

class BinaryTreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
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
