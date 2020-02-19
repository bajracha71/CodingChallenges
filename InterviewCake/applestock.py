# Stock price
#*************#
# Write an efficient function that takes stock_prices and 
# returns the best profit I could have made from one purchase and
# one sale of one share of Apple stock yesterday

# For example:
#--------------#
# stock_prices = [10, 7, 5, 8, 11, 9]
# get_max_proift( stock_prices ) returns 6 ( buying for 5 and 
# selling for 11 )

# Constraints:
#-------------#
# No "shorting" - you need to buy before you can sell. 
# Also you cannot buy and sell in the same time step - at least
# 1 minute has to pass. 

"""
Algorithm
=========
stock_prices = [p0, p1, ... , pN]
n = len(stock_prices)
N = n - 1

i => {0, 1, 2, ..., n - 1}

let max_profit(t) be maximum profit at time t
We can only have one transaction

max_profit(t) = max{
                    do not sell at time t => max_profit(t-1)
                    ,
                    sell it at time t => max( p(t) - p(m) , where m = [0, 1, .. , t-1] )
                }

max_profit(t) = max(max_profit(t-1), includingCurr(t))

max_profit(0) = 0

let includingCurr(t) = max( p(t) - p(m))

t = 0, includingCurr(0) = p(0)
t = 1, includingCurr(1) = max(p(1) - p(0))
t = 2, includingCurr(2) = max(
                                p(2) - p(0),
                                p(2) - p(1)
                            )
                        = p(2) - min(p(0), p(1))

t = 3, includingCurr(3) = max(  p(3) - p(0),
                                p(3) - p(1),
                                p(3) - p(2)
                             )
                        = p(3) - min(p(0), p(1), p(2))

t = t, includingCurr(t) = p(t) - min( p(0), p(1), ... , p(t-1))

min( p(0), p(1), ... , p(t-1))  is running minimum

max_profit(t) = max( max_profit(t-1), p(t) - runningminimum )
max_profit(0) = 0

"""
def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise Exception("stock prices must have at least 2 prices")

    # Calculate the max profit
    max_profit = float("-inf")
    runningmin = stock_prices[0]
    for p in stock_prices[1:]:
        max_profit = max(max_profit, p - runningmin )
        runningmin = min(runningmin, p)

    return max_profit



# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)

# Complexity:
#-----------#
# Time = O(n) where n is the number of stock_prices
# Space = O(1)