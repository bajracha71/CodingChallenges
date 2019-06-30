# Define class for ListNode
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Function to print linked list
def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.value, end="->")
        curr = curr.next
    print("None")


# Create linkedlist and return head of linkedlist
def create_linkedlist(*args):
    head = ListNode(value=args[0])
    curr = head
    for elem in args[1:]:
        newnode = ListNode(elem)
        curr.next = newnode
        curr = newnode
    return head


def main():
    head = create_linkedlist(1, 2, 3, 4, 5)
    print_linkedlist(head)


if __name__ == "__main__":
    main()
