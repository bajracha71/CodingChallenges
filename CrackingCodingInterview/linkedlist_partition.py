# 2.4 Write a code to partition a linked list around a value x,
# such that all nodes less than x comes before all nodes greater
# than or equal to x


class ListNode():

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def partition(head, value):
    newhead = ListNode()
    newtail = newhead

    curr = head
    prev = None

    while curr:
        nextnode = curr.next
        if curr.value > value:
            prev = curr
        elif curr.value == value:
            curr.next = head.next
            head = curr
        else:
            if prev:
                prev.next = nextnode
                curr.next = None
                newtail.next = curr
                newtail = curr
            else:
                head = nextnode
                curr.next = None
                newhead.value = curr.value
        curr = nextnode

    newtail.next = head
    return newhead


def createList(args):
    head = ListNode(args[0])
    curr = head
    for x in args[1:]:
        newnode = ListNode(x)
        curr.next = newnode
        curr = curr.next

    return head


def printList(head):
    curr = head
    while curr:
        print(curr.value, end="->")
        curr = curr.next
    print("None")


def main():
    head = createList([1, 2, 100, 20, 2, 4, 5, 6, 8, 7, 11, 10])
    print("Before partition:")
    printList(head)
    print("After partition:")
    par = partition(head, 8)
    printList(par)

if __name__ == "__main__":
    main()

# Time: O(n) , Space O(1)
