# Making change:
#--------------_#

# Your quirky boss collects rare, old coins...

# They found out you're a programmer and asked you to solve something they've been wondering for a long time.

# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢), your program would output 44—the number of ways to make 44¢ with those denominations:

# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢

import unittest


def change_possibilities(amount, denominations):

    # Calculate the number of ways to make change
    
    def helper(amount, i, cache):
        
        if amount == 0:
            return 1
        if amount < 0 or i >= len(denominations):
            return 0
            
        my_key = (amount, i)
        
        curr_deno = denominations[i]
        
        if my_key not in cache:
            include_curr = helper(amount - curr_deno, i, cache)
            exclude_curr = helper(amount, i + 1 , cache )
            
            cache[my_key] = include_curr + exclude_curr
        
        return cache[my_key]
        
    cache = dict()

    return helper(amount, 0, cache)

# Complexity:
# Time = O(amount * n) where n is the number of denomination after using memoization
# If memoization is not used then brute force will have time complexity of O( amount ^ n )

# Space complexity = O(amount * n)



# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)