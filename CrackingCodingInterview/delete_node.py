# 2.3 Implement an algorithm to delete a node in the middle of
#  a singly linked list, given only access to that node


def delete_node(node_to_delete):
    if node_to_delete.next is None:
        raise Exception("Last node cannot be deleted by this method")

    nextNode = node_to_delete.next
    node_to_delete.value = nextNode.value
    node_to_delete.next = nextNode.next


class ListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.value, end="=>")
        curr = curr.next
    print("None")


def create_linked_list(*args):
    head = ListNode(0)
    nodelist = list()
    curr = head
    for x in args:
        newnode = ListNode(x)
        if x % 2 == 0:
            nodelist.append(newnode)

        curr.next = newnode
        curr = newnode

    return [head, nodelist]

if __name__ == "__main__":
    head, nodelist = create_linked_list(1, 2,  3, 5)
    print_linkedlist(head)
    print("node to delete: ", nodelist[0].value)

    delete_node(nodelist[0])
    print("node is deleted")
    print_linkedlist(head)
