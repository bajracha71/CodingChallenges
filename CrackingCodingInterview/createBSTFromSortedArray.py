# 4.3 Given a sorted (increasing array) with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def createBST(nums):
    start = 0
    end = len(nums) - 1

    def createBST_helper(start, end):
        if start > end:
            return None

        mid = start + (end - start)//2
        mid_value = nums[mid]
        node = BinaryTreeNode(data=mid_value)
        node.left = createBST_helper(start, mid-1)
        node.right = createBST_helper(mid+1, end)
        return node

    root = createBST_helper(start, end)
    return root

# Time: O(n) , Space = O(h)
# Tested this solution in leetcode:
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
