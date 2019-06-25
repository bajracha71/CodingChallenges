# 1.2. Implement a function void reverse(char* str) in C or C++
# which reverses a null-terminated string.

import unittest


def string_reverse(char_array):

    start = 0
    end = len(char_array) - 1

    while start < end:
        char_array[start], char_array[end] = char_array[end], char_array[start]
        start += 1
        end -= 1


# Tests
# ***** #

class Test(unittest.TestCase):

    def test1(self):
        string1 = list("hello")
        string_reverse(string1)
        actual = "".join(string1)
        expected = "olleh"
        self.assertTrue(actual, expected)


unittest.main(verbosity=2)
