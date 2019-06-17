# Recursive String Permutation 
# **************************** #

# Write a recursive function for generating all permutations of an input string. Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops—it just needs to also be recursive.


import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    result = set()
    
    l = len(string)
    mystring = list(string)
    
    startIndex = 0
    endIndex = l - 1
    def permute(items, startIndex, endIndex):
        if startIndex > endIndex:
            result.add("".join(items))
        
        j = startIndex
        while j <= endIndex:
            items[j], items[startIndex] = items[startIndex], items[j]
            permute(items, startIndex + 1, endIndex)
            items[j], items[startIndex] = items[startIndex], items[j]
            j += 1
    
    permute(mystring, startIndex, endIndex)
    
    return result
            


# Time Complexity ; O(n * n!)


# Tests
class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)