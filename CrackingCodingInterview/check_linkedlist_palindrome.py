# 2.7 Implement a function to check if a linked list is
# a palindrome

import unittest
import linkedlist_helper as ll


def isLinkedListPalindrome(head):
    slow = head
    fast = head
    liststack = []

    while fast and fast.next:
        liststack.append(slow.value)
        slow = slow.next
        fast = fast.next.next


    # if fast is not None then it has odd number of node
    if fast is not None:
        slow = slow.next

    while slow:
        top = liststack.pop()
        if slow.value != top:
            return False

        slow = slow.next

    return True


class Test(unittest.TestCase):

    def test1(self):
        head = ll.create_linkedlist(1,2,3,2,1)
        self.assertTrue(isLinkedListPalindrome(head), True)

    def test2(self):
        head = ll.create_linkedlist(1,2,2,1)
        self.assertTrue(isLinkedListPalindrome(head), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)