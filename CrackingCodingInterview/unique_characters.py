# 1.1. Implement an algorithm to determine if a string has
# all unique characters. What if you cannot use additional data structure?

import unittest


# Using extra memory
def unique_charq(input_string):

    char_table = set()
    for x in input_string:
        if x in char_table:
            return False
        else:
            char_table.add(x)

    return True

# O(n) time and space


class Test(unittest.TestCase):

    def test1(self):
        self.assertTrue(unique_charq("abc"))

    def test2(self):
        self.assertFalse(unique_charq("aab"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

