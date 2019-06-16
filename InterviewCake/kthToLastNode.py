# Kth to the last node in linked list
# *********************************** # 

# Write a function kth_to_last_node() that takes an integer k and 
# the head_node of a singly-linked list,
# and returns the kkth to last node in the list.

# Took me 15 minutes to solve this without writing test cases

import unittest


def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list
    if k == 0:
        raise Exception("k must be greater than or equal to 1")
    
    fast = head
    i = 0
    while i < k:
        fast = fast.next
        i += 1
    
    slow = head
    
    while fast:
        fast = fast.next
        slow = slow.next


    return slow


# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)