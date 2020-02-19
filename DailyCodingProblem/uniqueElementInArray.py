# This problem was asked by Facebook.
#
# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
# find the two elements that appear only once.
#
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
#
# Follow-up: Can you do this in linear time and constant space?


def unique_elems(nums):
    d = dict()
    for x in nums:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    res = [k for k, v in d.items() if v == 1]
    return res

print(unique_elems([2, 4, 6, 8, 10, 2, 6, 10]))
