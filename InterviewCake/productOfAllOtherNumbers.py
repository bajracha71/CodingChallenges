# Product of All Other numbers:
#-----------------------------#

# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

# For example, given: [1, 7, 3, 4]  →  [84, 12, 28, 21]

# by calculating:

# [7 x 3 x 4, 1 x 3 x 4, 1 x 7 x 4, 1 x 7 x 3]

# Note: Do not use divison in your solution

# https://leetcode.com/problems/product-of-array-except-self/description/
# https://www.interviewcake.com/question/python3/product-of-other-numbers

import unittest


def prod_before(int_list):

    result = []
    prod = 1
    for x in int_list:
        result.append(prod)
        prod = prod * x 
    
    return result
    


def getProdutExceptSelf(int_list):
    
    array_size = len(int_list)
    
    if (array_size) <= 1:
        raise Exception("integer list must contain atleast 2 elements")
    
    # Make a list with the products
    
    prodBefore = prod_before(int_list)
    
    prod = 1
    
    end = array_size - 1

    while end >= 0:
        prodBefore[end] *=  prod
        prod  *= int_list[end]
        end -= 1
    
    return prodBefore


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = getProdutExceptSelf([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = getProdutExceptSelf([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = getProdutExceptSelf([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = getProdutExceptSelf([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = getProdutExceptSelf([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = getProdutExceptSelf([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            getProdutExceptSelf([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            getProdutExceptSelf([1])


unittest.main(verbosity=2)


# Complexity:
# Time: O(n) where n is the length of array
# Space: O(1), note: The output array does not count as extra space for the purpose of space complexity analysis.