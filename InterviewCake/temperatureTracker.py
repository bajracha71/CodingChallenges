# You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.

# Write a class TempTracker with these methods:

# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean ↴ of all temps we've seen so far
# get_mode()—returns a mode ↴ of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

# get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

# If there is more than one mode, return any of the modes.

import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and 
    
    def __init__(self):
        self.temp_list = list()
        self.max_so_far = float("-inf")
        self.min_so_far = float("inf")
        self.list_size = 0
        self.total_temp = 0
        self.mean = None
        
        self.hashmap = dict()
        self.mode = None
        self.max_occurance = 0


    def insert(self, temperature):
        self.temp_list.append(temperature)
        self.max_so_far = max(temperature, self.max_so_far)
        self.min_so_far = min(temperature, self.min_so_far)
        self.list_size += 1
        self.total_temp += temperature
        self.mean = self.total_temp / self.list_size
        
        if temperature in self.hashmap:
            self.hashmap[temperature] += 1
        else:
            self.hashmap[temperature] = 1
            
        if self.hashmap[temperature] > self.max_occurance:
            self.max_occurance = self.hashmap[temperature]
            self.mode = temperature
            

    def get_max(self):
        return self.max_so_far

    def get_min(self):
        return self.min_so_far
        
    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)