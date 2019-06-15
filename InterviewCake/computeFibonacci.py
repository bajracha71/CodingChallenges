# Compute nth Fibonacci numbers
# ******************************* #

# Write a function fib() that takes an integer nn and 
# returns the nnth Fibonacci ↴ number.

# Let's say our Fibonacci series is 0-indexed and 
# starts with 0. 
# 
# So:

#   fib(0)  # => 0
# fib(1)  # => 1
# fib(2)  # => 1
# fib(3)  # => 2
# fib(4)  # => 3
# ...

import unittest


def fib(n):

    # Compute the nth Fibonacci number
    
    if n == 0 or n == 1:
        return n 
    
    f_1 = 0
    f_2 = 1
    
    for i in range(2, n+1):
        res = f_1 + f_2
        f_1, f_2 = f_2, res

    return res
    
    # Complexity:
    # Time = O(n)
    # Space = O(1)


# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)