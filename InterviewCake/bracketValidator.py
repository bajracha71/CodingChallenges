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


def validateBrackets(bracketList):
    bracket = {"[":"]", "{":"}", "(": ")"}
    openStack = []
    bracketQ = False

    for b in bracketList:
        if b in bracket:
            openStack.append(b)
            bracketQ = True
        if b in bracket.values():
            bracketQ = True
            if len(openStack) != 0:
                openBracket = openStack.pop()
                # check if close bracket b match with corresponding open
                closeBracket = bracket[openBracket]
                if closeBracket != b:
                    return False
            else:
                return False

    return bracketQ and len(openStack) == 0

# Time Complexity : O(n)
# Space Complexity: O(1)


import unittest

class Test(unittest.TestCase):

    def test1(self):
        actual = validateBrackets("((()))")
        expected = True
        self.assertEqual(actual, expected)
    
    def test2(self):
        actual = validateBrackets("()[")
        self.assertFalse(actual)

    def test3(self):
        actual = validateBrackets("([({})])")
        self.assertTrue(actual)
    
    def test4(self):
        self.assertFalse(validateBrackets("("))
    
    def test5(self):
        self.assertFalse(validateBrackets(")"))
    
    def test6(self):
        self.assertFalse(validateBrackets("hello"))

    def test7(self):
        self.assertFalse(validateBrackets(""))


unittest.main(verbosity= 2)
    


