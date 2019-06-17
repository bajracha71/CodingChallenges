# Which number appears twice:
# **************************** #

# I have a list of n + 1 numbers. Every number in the range 1..n
#  appears once except for one number that appears twice.

# Write a function for finding the number that appears twice.

import unittest


def find_repeat(nums):

    # Find the number that appears twice

    # Solution 1
    #-----------
    # n = max(nums)
    # s = sum(nums)
        
        
    # return s - n * (n + 1)//2
    
    # Solution 2
    #------------
    seen = set()
    
    for x in nums:
        if x in seen:
            return x
        else:
            seen.add(x)
    
    raise Exception("No duplicates")


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_no_duplicates(self):
        with self.assertRaises(Exception):
            find_repeat([1,2,3])


unittest.main(verbosity=2)