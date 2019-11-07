# Bracket Validator 
# ***************** #

# You're working with an intern that keeps coming to you with JavaScript code 
# that won't run because the braces, brackets, and parentheses are off. 
# To save you both some time, you decide to write a braces/brackets/parentheses validator.

# Let's say:

# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."

# Write an efficient function that tells us whether or not an input string's 
# openers and closers are properly nested.

# Examples:

# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False


import unittest


def is_valid(code):

    # Determine if the input code is valid
    open_brackets = [ "[", "{", "(" ]
    close_brackets = [ "]", "}", ")" ]
    bracket_table = dict(zip(open_brackets, close_brackets))
    open_paren = list()
    for x in code:
        if x in open_brackets:
            open_paren.append(x)
        if x in close_brackets:
            if len(open_paren) == 0:
                return False
            pop_open = open_paren.pop()
            if bracket_table[pop_open] != x:
                return False
    return len(open_paren) == 0


# Tests
class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)