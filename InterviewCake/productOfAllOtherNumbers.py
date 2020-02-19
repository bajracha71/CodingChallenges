# Product of All Other numbers:
# -----------------------------#

# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# For example, given: [1, 7, 3, 4]  →  [84, 12, 28, 21]

# by calculating:

# [7 x 3 x 4, 1 x 3 x 4, 1 x 7 x 4, 1 x 7 x 3]

# Note: Do not use divison in your solution

# https://leetcode.com/problems/product-of-array-except-self/description/
# https://www.interviewcake.com/question/python3/product-of-other-numbers

"""
Idea:
====

nums:  [1, 7, 3, 4]
Index:  [0, 1, 2, 3]
output: [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3] = [84, 12, 28, 21]

LeftP:  [1, 1, 7,  21]
rightP: [84, 12, 4, 1]
output: [1 * 84, 1 * 12, 7 * 4, 21 * 1 ] = [84, 12, 28, 21]

LeftP(0) = 1
LeftP(1) = LeftP(0) * nums(0) = 1 * 1 = 1
LeftP(2) = LeftP(1) * nums(1) = 1 * 7 = 7
LeftP(t) = LeftP(t-1) * nums[t-1]

n = len(num)
last = n - 1 = 3

rightP(3) = 1
rightP(2) = rightP(3) * nums(3) = 1 * 4 = 4
rightP(t) = rightP(t + 1) * nums(t + 1)

"""
import unittest

def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise Exception("invalid list")


    # Make a list with the products
    leftP = left_prod(int_list)
    rightP = right_prod(int_list)

    return [ l * r for l,r in zip(leftP, rightP) ]

def left_prod(nums):
    n = len(nums)
    leftP = [1] * n
    for i in range(1, n):
        leftP[i] = leftP[i-1] * nums[i - 1]

    return leftP

def right_prod(nums):
    n = len(nums)
    last = n - 1
    rightP = [1] * n
    for i in range(last-1, -1, -1):
        rightP[i]  = rightP[i+1] * nums[i + 1]

    return rightP


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
# Complexity:
# Time: O(n) where n is the length of array
# Space: O(1), note: The output array does not count as extra space for the purpose of space complexity analysis.
