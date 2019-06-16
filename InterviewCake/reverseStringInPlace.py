# Reverse String In Place 
# *********************** # 
# Write a function that takes a list of characters and reverses the letters in place. 

# Time Complexity = O(n/2)
# Space = O(1)

import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    
    start = 0
    end = len(list_of_chars) - 1
    
    while start < end:
        list_of_chars[start], list_of_chars[end] =  list_of_chars[end],  list_of_chars[start]
        start += 1
        end -= 1
        

    return list_of_chars




# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)