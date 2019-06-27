# 1.4. Write a method to replace all spaces in a string with
# '%20'. You may assume that the string has sufficient space
# at the end of the string to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: if implementing in java or python please use a charcter
# array so that you can perform this operation in place.)

import unittest


def urlify(str1, length):

    end = len(str1) - 1

    ptr = length - 1
    while end >= 0:

        if str1[ptr] != " ":
            str1[end] = str1[ptr]
            end -= 1
        #    ptr -= 1
        else:
            str1[end] = '0'
            str1[end-1] = '2'
            str1[end-2] = '%'
            end -= 3
        #    ptr -= 1

        ptr -= 1


# Test
# ***** #

class Test(unittest.TestCase):

    def test1(self):
        str1 = list('much ado about nothing      ')
        urlify(str1, 22)
        actual = "".join(str1)
        expected = 'much%20ado%20about%20nothing'
        self.assertTrue(actual, expected)

    def test2(self):
        str1 = list('Mr John Smith    ')
        urlify(str1, 13)
        actual = "".join(str1)
        expected = 'Mr%20John%20Smith'
        self.assertTrue(actual, expected)


unittest.main(verbosity=2)