# Find in Ordered set 
# ------------------- # 

# Suppose we had a list ↴ of nn integers sorted in ascending order. 
# How quickly could we check if a given integer is in the list?

import unittest


def contains(ordered_list, number):

    # Check if an integer is present in the list
    def bsearch(start, end):
        mid = start + (end - start) // 2

        if end < start or mid < start or mid > end:
            return False

        potential_value = ordered_list[mid]

        if potential_value == number:
            return True
            
        elif potential_value < number :
            # check right half
            return bsearch(mid+1 , end )
            
        else:
            # check left half
            return bsearch(start, mid-1)
            
    n = len(ordered_list)
    first_idx = 0
    last_idx = n - 1
    return bsearch(first_idx, last_idx)

# Complexity
# Time: O(nlogn)
# Space : O(1)


# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)