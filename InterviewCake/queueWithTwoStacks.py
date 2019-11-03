# 19. Implement Queue with two stacks
# ******************************* #

# Implement a queue ↴ with 2 stacks.  Your queue should have an enqueue and a 
# dequeue method and it should be "first in first out" (FIFO).

# Optimize for the time cost of mm calls on your queue.
#  These can be any mix of enqueue and dequeue calls.

# Assume you already have a stack implementation and 
# it gives O(1) time push and pop.

# Queue : First In First Out (FIFO)
# Stacks: Last In First Out (LIFO)

class QueueWithTwoStacks(object):
    def __init__(self):
        self.insert_stack = list()
        self.remove_stack = list()
        self.size = 0

    def enqueue(self, elem):
        self.size += 1
        self.insert_stack.append(elem)

    def dequeue(self):
        if self.size <= 0:
            raise Exception("Queue is empty")

        if not self.remove_stack:  # self.remove_stack == []
            # move all element in insert_stack to remove_stack by popping its element
            while self.insert_stack:
                popped = self.insert_stack.pop()
                self.remove_stack.append(popped)

        self.size -= 1
        return self.remove_stack.pop()


# Complexity
# Time : O(n)

# Tests
# ------ # 
import unittest


class Tests(unittest.TestCase):

    def test1(self):
        q = QueueWithTwoStacks()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        actual = q.dequeue()
        expected = 1
        self.assertTrue(actual, expected)

        actual = q.dequeue()
        expected = 2
        self.assertTrue(actual, expected)

        actual = q.dequeue()
        expected = 3
        self.assertTrue(actual, expected)

        with self.assertRaises(Exception):
            q.dequeue()

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueWithTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueWithTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)
