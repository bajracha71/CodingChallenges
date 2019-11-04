# Hightest Product of 3
#************************#

# Given a list of integers, find the highest product you can get from three of the integers.

# The input list_of_ints will always have at least three integers.

import unittest

def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    n = len(list_of_ints)
    if n < 3:
        raise Exception("error")

    h1, h2, h3 = get_highest_3(list_of_ints)
    l1, l2 = get_lowest_2(list_of_ints)

    return max(h1 * h2 * h3, h1 * l1 * l2)



def get_highest_3(nums):
    h1, h2, h3 = float("-inf"), float("-inf"), float("-inf")
    for x in nums:
        if x >= h1:
            h1, h2, h3 = x, h1, h2
        elif x >= h2:
            h2, h3 = x, h2
        elif x > h3:
            h3 = x

    return h1, h2, h3



def get_lowest_2(nums):
    l1, l2 = float("inf"), float("inf")
    for x in nums:
        if x <= l1:
            l1, l2 = x, l1
        elif x < l2:
            l2 = x

    return l1, l2


# Complexity
# Time = O(n log n )
# Space = O(n)

# This could be done in linear time and constant space (TODO)

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        acutal = highestProductOfThree([1,2,3,4])
        expected = 24
        self.assertEqual(acutal, expected)

    def test_longer_list(self):
        actual = highestProductOfThree([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highestProductOfThree([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highestProductOfThree([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highestProductOfThree([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highestProductOfThree([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highestProductOfThree([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highestProductOfThree([1, 1])


unittest.main(verbosity=2)