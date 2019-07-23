# 2.5. You have two numbers represented by a linked list,
# where each node contains a single digit.
# The digits are stored in reverse order, such that the Ts digit
# is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.

# EXAMPLE

# - Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# - Output: 2 -> 1 -> 9.That is, 912.

# Followup

# Suppose the digits are stored in forward order.
# EXAMPLE

# - Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# - Output: 9 -> 1 -> 2.That is, 912.


# Note: ListNode, print_linkedlist and create_linkedlist is define in
# linkedlist_helper.py
import linkedlist_helper as ll


def add_backward(head1, head2):
    ptr1 = head1
    ptr2 = head2
    carry = 0

    while ptr1 and ptr2:

        add_res = ptr1.value + ptr2.value + carry

        if add_res < 10:
            ptr1.value = add_res
            carry = 0
        else:
            carry = 1
            ptr1.value = add_res % 10

        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr1 and carry > 0:
        add_res = ptr1.value + carry
        if add_res < 10:
            ptr1.value = add_res
            carry = 0
        else:
            ptr1.value = add_res % 10
            carry = 1

        ptr1 = ptr1.next

    while ptr2 and carry > 0:
        add_res = ptr2.value + carry
        if add_res < 10:
            newnode = ll.ListNode(add_res)
            carry = 0
            ptr1.next = newnode
            ptr1 = newnode
        else:
            newnode = ll.ListNode(add_res % 10)
            carry = 1
            ptr1.next = newnode
            ptr1 = newnode

    if carry > 0:
        newnode = ll.ListNode(carry)
        ptr1.next = newnode

    return head1


def reverseList(head):

    curr = head
    prev = None

    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev


def add_forward(head1, head2):
    revhead1 = reverseList(head1)
    revhead2 = reverseList(head2)
    result = add_backward(revhead1, revhead2)
    return reverseList(result)


def main():
    head1 = ll.create_linkedlist(7, 1, 6)
    head2 = ll.create_linkedlist(5, 9, 2)
    addB = add_backward(head1, head2)
    ll.print_linkedlist(addB)
    print("\nUsing add_backward: \n")
    revaddB = reverseList(addB)
    ll.print_linkedlist(revaddB)

    # - Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
    # - Output: 9 -> 1 -> 2.That is, 912.

    print("\nUsing add_forward: \n")
    head3 = ll.create_linkedlist(6, 1, 7)
    head4 = ll.create_linkedlist(2, 9, 5)
    addF = add_forward(head3, head4)
    ll.print_linkedlist(addF)


if __name__ == "__main__":
    main()
