# 2.6 Given a circular linked list, implement an algorith which returns the node at the beginning of the loop.

# - Definition

#     - Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

# - Example
#     - Input: A -> B -> C -> D -> E -> C [the same C as earlier]
#     - output: C


import linkedlist_helper as ll
import unittest


def loopnode(head):
    slow = head
    fast = head

    # detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        raise Exception("Linked list do not have cycle")

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def test1():
    node1 = ll.ListNode(value=1)
    node2 = ll.ListNode(value=2)
    node3 = ll.ListNode(value=3)
    node4 = ll.ListNode(value=4, next=node2)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    loop = loopnode(node1)
    return loop == node2


class Test(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(test1(), True)

    def testException(self):
        with self.assertRaises(Exception):
            l1 = ll.create_linkedlist(1, 2, 3, 4)
            loopnode(l1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
