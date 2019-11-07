# Recursive String Permutation
# **************************** #

# Write a recursive function for generating all permutations of an input string. Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops—it just needs to also be recursive.


import unittest


def get_permutations(string):

    # Generate all permutations of the input string

    res = set()
    permute(list(string), 0, res)
    return res


def permute(nums, i, res):
    if i == len(nums):
        temp = "".join(nums)
        res.add(temp)
        return

    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        permute(nums, i + 1, res)
        nums[i], nums[j] = nums[j], nums[i]


# Time Complexity ; O(n * n!)
# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


if __name__ == "__main__":

    unittest.main(verbosity=2)
