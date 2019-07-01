# Hightest Product of 3
#************************#

# Given a list of integers, find the highest product you can get from three of the integers.

# The input list_of_ints will always have at least three integers.

import unittest

def highestProductOfThree(intList):

    sortedList = sorted(intList)
    h1, h2, h3 = sortedList[-3:]
    l1, l2 = sortedList[:2]

    highest_prod = max( h1 * h2 * h3, h3 * l1 * l2)

    return highest_prod

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