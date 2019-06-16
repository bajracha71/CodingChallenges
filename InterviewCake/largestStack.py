# Largest Stack 
# ************** #

# You want to be able to access the largest element in a stack. ↴

# You've already implemented this Stack class:

# Use your Stack class to implement a new class MaxStack with a method 
# get_max() that returns the largest element in the stack. get_max() should not remove the item.

# Your stacks will contain only integers.

import unittest


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    # Implement the push, pop, and get_max methods


    def __init__(self):
        
        self.items = Stack()
        self.maxlist = Stack()

    def push(self, item):
        
        lastmax = self.maxlist.peek()
        
        if not lastmax or item >= lastmax:
            self.maxlist.push(item)
        
        self.items.push(item)

    def pop(self):
        
        poped = self.items.pop()
        
        if not poped:
            return None
        
        if poped == self.maxlist.peek():
            self.maxlist.pop()
        
        return poped

    def get_max(self):
        return self.maxlist.peek()




# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)