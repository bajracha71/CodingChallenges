# Cake Thief
# *********** # 

# You are a renowned thief who has recently switched from stealing precious 
# metals to stealing cakes because of the insane profit margins. 
# You end up hitting the jackpot, breaking into the world's largest privately owned 
# stock of cakes—the vault of the Queen of England.

# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
# Each type of cake has a weight and a value, stored in a tuple with two indices:
# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British shillings
# For example:

#   # Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)

# # Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)

# You brought a duffel bag that can hold limited weight, and you want to make 
# off with the most valuable haul possible.

# Write a function max_duffel_bag_value() that takes a list of cake 
# type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

# For example:

#   cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20

# # Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
# max_duffel_bag_value(cake_tuples, capacity)
 
# # Weights and values may be any non-negative integer. Yes, it's weird to 
# think about cakes that weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our algorithms flexible and comprehensive.

import unittest


def max_duffel_bag_value(cake_tuples, weight_capacity):

    # Calculate the maximum value we can carry
    # Order matter? No
    # Replacement ? Yes
    
    def helper(i, weight_capacity, cache):
        
        if i >= len(cake_tuples) or weight_capacity <= 0:
            return 0
         
        my_key = (i, weight_capacity)
        
        if my_key not in cache:
            current_weight = cake_tuples[i][0]
            current_value = cake_tuples[i][1]
        
            if current_weight == 0 and current_value > 0:
                
                cache[my_key] =  float("inf")
                return  cache[my_key]
        
            if current_weight == 0 or  current_weight > weight_capacity:
                cache[my_key] = helper(i+1, weight_capacity, cache)
                return  cache[my_key]
                
        
            remaining_weight =  weight_capacity - current_weight
    
        
            include = current_value + helper(i, remaining_weight, cache)
        
            exclude = helper(i+1, weight_capacity, cache)
        
            cache[my_key] =  max( include, exclude )
        
        return cache[my_key]

    cache = dict()
    
    return helper(0, weight_capacity, cache)


# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

# Complexity :
# Time : O(m * n) where m is the weight capacity and n is the number of elements in cake_tupes
# Space : O(m * n )