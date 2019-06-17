# Parenthesis Matching
# ******************* # 


# I like parentheticals (a lot).

# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above,
# along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 
# 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

import unittest



class Stack():
    def __init__(self):
        self.items = []
        self.size = 0
        
    def push(self, elem):
        self.items.append(elem)
        self.size += 1
        
        
    def pop(self):
        
        if self.size == 0:
            return None
       
        self.size -= 1
        return self.items.pop()
        
    def peek(self):
        if self.size == 0:
            return None
        
        return self.items[-1]
        
    def emptyQ(self):
        return self.size == 0
        
def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    
    # stack1 is the container for open brackets
    stack1 = Stack()
    resultDict = dict()
    
    for i, x in enumerate(sentence):
        # when we encounter new "(" push its index into stack
        if x == "(":
            stack1.push(i)
        # When we encounter new ")" remove elem from stack1
        if x == ")" :
            if not stack1.emptyQ():
                index = stack1.pop()
                resultDict[index] = i
            else:
                raise Exception("sentence do not have valid parenthesis")


    return resultDict[opening_paren_index]

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