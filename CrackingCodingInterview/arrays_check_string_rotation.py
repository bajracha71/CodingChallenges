# 1.8 Assume you have a method `isSubstring` which checks
# if one word is a substring of another. Given two strings,
# `s1` and `s2`, write code to check if `s2` is a roation
# of `s1` using only one call to `isSubstring`
# (eg. `waterbottle` is a rotation of `erbottlewat`)


import unittest


def check_string_rotation(string1, string2):

    def isSubstring(string1, string2):
        return string1 in string2

    if len(string1) != len(string2):
        return False

    superString = string1 + string1
    return isSubstring(string2, superString)


# Test
# ***** #

class Test(unittest.TestCase):

    def test1(self):
        string1 = "waterbottle"
        string2 = "erbottlewat"
        self.assertTrue(check_string_rotation(string1, string2))

    def test2(self):
        string1 = "waterbottle"
        string2 = "erbottlewat"
        self.assertTrue(check_string_rotation(string2, string1))

    def test3(self):
        string1 = "waterbottle_"
        string2 = "erbottlewat"
        self.assertFalse(check_string_rotation(string2, string1))


if __name__ == "__main__":
    unittest.main(verbosity=2)