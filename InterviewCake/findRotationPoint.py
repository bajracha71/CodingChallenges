# Find Rotation Point
# ---------------------- #

# I want to learn some big words so people think I'm smart.
# I opened up a dictionary to a page in the middle and started flipping through, 
# looking for words I didn't know. I put each word I didn't know at increasing 
# indices in a huge list I created in memory. When I reached the end of the dictionary, 
# I started from the beginning and did the same thing until I reached the page I started at.
# Now I have a list of words that are mostly alphabetical, except they start somewhere in 
# the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. 
# In other words, this is an alphabetically ordered list that has been "rotated."
#  For example:

#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

# Write a function for finding the index of the "rotation point," 
# which is where I started working from the beginning of the dictionary. 
# This list is huge (there are lots of words I don't know) so we want to be efficient here.

import unittest

def find_rotation_point(words):

    # Find the rotation point in the list
    
    def helper( start, end ):
        
        if start < end:
            mid = start + ( end - start) // 2
        
            potential_RWord = words[mid]
        
            left_word = words[mid - 1]
            right_word = words[mid + 1]
    
            if potential_RWord < right_word and potential_RWord < left_word:
            # we found rotation point
                return mid
        
        # if potential_RWord is in left side i.e 
        # side from where we started 
        
            if words[0] <=  potential_RWord :
                return helper(mid + 1, end )
        
            if potential_RWord <= words[-1]:
                return helper(start, mid - 1)
                
        if start == end and end == len(words) - 1:
            return end
    
    start = 0
    end = len(words) - 1 
    
    
    if end == start: # list has only one element
        return 0
    
    if end == 1 and words[end] < words[start]: # list has two element
        return 1       
    
    return helper(0, len(words)  - 1)

# Complexity:
# Time :O(nlogn)

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)