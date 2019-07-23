# 2.1 Write code to remove duplicates from an unsorted linked list.
# - Follow up: How would you solve this problem if a temporary buffere
# is not allowed? With no extra space, it will take time $O(n^2)$ and $O(1)$
# space.


class ListNode(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def print_linkedlist(head):
    if head is None:
        print("None")
        return
    else:
        print(head.value, end="=>")
        print_linkedlist(head.next)


def remove_duplicates(head):

    node_set = set()

    curr = head
    prev = None
    while curr:
        val = curr.value
        nextnode = curr.next
        if val in node_set:
            prev.next = nextnode
            curr.next = None
        else:
            node_set.add(val)
            prev = curr
        curr = nextnode

    return head


if __name__ == "__main__":
    headnode = ListNode(0)
    nextnode1 = ListNode(1)
    nextnode2 = ListNode(2)
    nextnode3 = ListNode(1)
    nextnode4 = ListNode(5)
    headnode.next = nextnode1
    nextnode1.next = nextnode2
    nextnode2.next = nextnode3
    nextnode3.next = nextnode4
    nextnode4.next = ListNode(0)

    print("Original linked list:")
    print_linkedlist(headnode)
    remove_duplicates(headnode)
    print("After removing duplicates:")
    print_linkedlist(headnode)
