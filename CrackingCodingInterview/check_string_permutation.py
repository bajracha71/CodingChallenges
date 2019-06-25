# 1.3. Given two strings, write a method to decide if one is a
# permutation of the other


import unittest


def check_string_permutation(string1, string2):

    if len(string1) != len(string2):
        return False

    char_table = dict()

    for x in string1:
        if x in char_table:
            char_table[x] += 1
        else:
            char_table[x] = 1

    for y in string2:
        if y in char_table:
            char_table[y] -= 1
        else:
            return False

    for c in char_table:
        if char_table[c] != 0:
            return False

    return True


class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(check_string_permutation("hello", "olleh"))

    def test2(self):
        self.assertFalse(check_string_permutation("hello", "ollh"))

    def test3(self):
        self.assertFalse(check_string_permutation("hello", "plleh"))





unittest.main(verbosity=2)

