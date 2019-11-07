# Parenthesis Matching
# ******************* # 


# I like parentheticals (a lot).

# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above,
# along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 
# 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    bracket_table = create_bracket_table(sentence)
    return bracket_table[opening_paren_index]


def create_bracket_table(sentence):
    s = list() # stack
    bracket_table = dict()  # key => open paren index, value => close paren index
    for i, x in enumerate(sentence):
        if x == "(":
            s.append(i)
        if x == ")":
            if s:
                open_paren_index = s.pop()
                bracket_table[open_paren_index] = i
            else:
                raise Exception("invalid brackets")

    return bracket_table
# Time and space Complexity : O(n)


# Tests
class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)