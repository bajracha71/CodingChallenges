# Find in Ordered set 
# ------------------- # 

# Suppose we had a list ↴ of nn integers sorted in ascending order. 
# How quickly could we check if a given integer is in the list?

import unittest


def contains(ordered_list, number):

    # Check if an integer is present in the list
    
    def helper(start, end):
        mid = start + (end - start) // 2
        
        potential_value = ordered_list[mid]
        
        if end < start or mid < 0 or mid > len(ordered_list):
            return False
    
            
        if potential_value == number:
            return True
            
        elif potential_value < number :
            # check right half
            return helper(mid+1 , end )
            
        else:
            # check left half
            return helper(start, mid-1)
            
    length = len(ordered_list)
    
    if length == 0:
        return False
        
    return helper(0, length - 1)

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