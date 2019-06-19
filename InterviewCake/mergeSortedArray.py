# Merge Sorted List
# ***************** # 

# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

# For example:

# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print(mergeSortedList(my_list, alices_list))


def mergeSortedList( list1, list2 ):
    sortedList = []

    l1 = len(list1)
    l2 = len(list2)

    ptr1 = ptr2 = 0

    while ptr1 < l1 and ptr2 < l2:
        if list1[ptr1] <= list2[ptr2]:
            sortedList.append( list1[ptr1] )
            ptr1 += 1
        else:
            sortedList.append( list2[ptr2] )
            ptr2 += 1
    
    while ptr1 < l1:
        sortedList.append( list1[ptr1])
        ptr1 += 1
    
    while ptr2 < l2:
        sortedList.append( list2[ptr2] )
        ptr2 += 1
    
    return sortedList

# Test
# **** #

import unittest

class Test(unittest.TestCase):

    def test1(self):
        actual = mergeSortedList([2,3,4], [1,3, 4, 10, 20])
        expected = [1,2,3,3,4,4,10,20]
        self.assertTrue(actual, expected)
    def test_both_lists_are_empty(self):
        actual = mergeSortedList([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = mergeSortedList([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = mergeSortedList([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = mergeSortedList([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = mergeSortedList([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity = 2)