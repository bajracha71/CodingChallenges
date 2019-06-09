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


def get_max_profit(stock_prices):
    num_of_prices = len(stock_prices)

    if num_of_prices < 2:
        raise Exception("Invalide list of stock prices")
# Leetcode link:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


    bought_price = stock_prices[0]
    max_profit = stock_prices[1] - bought_price

    for sell_price in stock_prices[1:]:
        curr_profit = sell_price - bought_price

        if max_profit < curr_profit:
            # update max profit
            max_profit = curr_profit
       
        if sell_price < bought_price:
            # update bought_price
            bought_price = sell_price
    
    return max_profit


# Tests
import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1,5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    
    def test_price_goes_down_then_up(self):
        actual = get_max_profit([5,2, 4,9, 10])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        acutal = get_max_profit([2,3,4,5])
        expected = 3
        self.assertEqual(acutal, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([10, 4, 2, 1])
        expected = -1
        self.assertEqual(actual, expected)
    
    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1,1,1,1])
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])



unittest.main(verbosity=2)


# Complexity:
#-----------#
# Time = O(n) where n is the number of stock_prices
# Space = O(1)