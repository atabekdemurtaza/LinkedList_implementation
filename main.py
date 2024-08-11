import visualize
from linked_list import LinkedList
from node import ListNode

if __name__ == "__main__":
    llist = LinkedList()

    llist.add_first(ListNode(val=1))
    llist.add_first(ListNode(val=2))
    llist.add_first(ListNode(val=3))

    llist.add_last(ListNode(val=4))
    llist.add_last(ListNode(val=5))
    llist.add_last(ListNode(val=6))

    llist.add_after(4, ListNode(val=7))
    llist.add_before(2, ListNode(val=8))

    llist.remove_node(1)
    print(llist)

    # Visualize the linked list
    visualize.visualize(llist)
