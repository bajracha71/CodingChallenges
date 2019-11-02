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
    n = len(words)
    return bsearch(words, 0, n - 1)


def bsearch(words, first_ptr, last_ptr):
    mid = first_ptr + (last_ptr - first_ptr) // 2
    if words[mid] >= words[0]: # words[mid] in first interval
        return bsearch(words, mid + 1, last_ptr)
    if words[mid] <= words[-1]: # words[mid] is in the second interval where solution exits
        if mid == len(words) - 1:
            return mid
        elif words[mid] < words[mid + 1] and words[mid] < words[mid - 1]:
            return mid
        else:
            return bsearch(words, first_ptr, mid - 1)



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
