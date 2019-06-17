# Reverse Words
# *************** #

# Write a function reverse_words() that takes a message as a list of characters 
# and reverses the order of the words in place. ↴

# Why a list of characters instead of a string?

# The goal of this question is to practice manipulating strings in place. 
# Since we're modifying the message, we need a mutable ↴ type like a list, 
# instead of Python 2.7's immutable strings.

# For example:

#   message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]

# reverse_words(message)

# # Prints: 'steal pound cake'
# print ''.join(message)

# When writing your function, assume the message contains only letters and spaces, 
# and all words are separated by one space.

import unittest


def reverse_words(message):

    # Decode the message by reversing the words
    
    start = 0
    end = 0
    length = len(message)
    lastIndex = length - 1
    
    reverseList(message, start, lastIndex)
    
    while end < length:
        
        # Find end pointer such that message[end] is not alphabet
        while end < length and message[end].isalpha():
            end += 1
        
        lastIndex = end - 1
        
        # Revere list from index start to lastIndex
        reverseList(message, start, lastIndex)
        
        # Now update start
        start = end 
        # Find new start suchs that message[end] is alphabet 
        while start < length and not message[start].isalpha():
            start += 1
        
        # reset end
        end = start


    return message
    

def reverseList( items, startIndex, lastIndex):
    while startIndex < lastIndex:
        items[startIndex], items[lastIndex] = items[lastIndex], items[startIndex]
        startIndex += 1
        lastIndex -= 1
    


# Time Complexity = O(n)
# Space complexity = O(1)


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)