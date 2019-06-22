# 9.1 A child is running up a staircase with n steps, and can hop
# either 1 step, 2 step or 3 steps at a time. Implement a method
# to count how many possible ways the child can run up the stairs. 

# Solution:
# Order matters? Yes !!! . For example if there is 3 steps, then 
# Reaching 3 floor by taking ( 1 step, 2 step ) is different than 
# (2 step, 1 step )

# With Repalcement? Yes !!! Because each time we take either 1 or 2 or 3 step, 
# next time we have same options. 

# Order Matters => Go through every options
# Order does not matter => Think of it as include, exclude problem

# Recurcive solution;
# For every option 1, 2 or 3 step we have
# countWays( n , stepsList, i ) = countWays( n - stepList[i] , stepList, i + 1)


def countWays(n):
	if ( n == 0 ):
		return 1
	if ( n < 0 ):
		return 0
	
	stepList = [1,2,3]
	ways = 0
	
	for step in stepList:
		ways += countWays(n - step)
	
	return ways

def countWaysOptimized(n):
	
	if ( n < 0 ):
		 return 0
	if ( n == 0 ):
		 return 1
	if ( n <= 2 ):
		 return n
	
	n0 = 1
	n1 = 1
	n2 = 2

	for x in range(3, n + 1):
		res = n0 + n1 + n2
		n0, n1, n2 = n1, n2, res
	return res
 

def solution(n):
	if (n == 0):
		return 1
	if (n < 0):
		return 0
	return solution(n-1) + solution(n - 2) + solution(n - 3)

# Test
# ***** #

import unittest

class Tests(unittest.TestCase):
	def test1(self):
		actual = countWaysOptimized(3)
		expected = solution(3)
		self.assertTrue(actual, expected)
	
	def test2(self):
		actual = countWaysOptimized(10)
		expected = solution(10)
		self.assertTrue(actual, expected)

	def test3(self):
		n = 20
		acutal = countWaysOptimized(n)
		expected = solution(n)
		self.assertTrue(acutal, expected)

unittest.main(verbosity = 2)
