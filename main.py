import visualize
from linked_list import LinkedList
from node import ListNode

if __name__ == "__main__":
    llist = LinkedList()
    # print(llist)

    llist.add_first(ListNode("a"))
    # print(llist)
    llist.add_first(ListNode("b"))
    # print(llist)
    llist.add_first(ListNode("c"))
    # print(llist)

    llist.add_last(ListNode("d"))
    # print(llist)
    llist.add_last(ListNode("e"))
    # print(llist)
    llist.add_last(ListNode("f"))
    # print(llist)

    llist.add_after("d", ListNode("g"))
    # print(llist)

    llist.add_before("b", ListNode("v"))
    # print(llist)

    llist.remove_node("a")
    print(llist)

    # Visualize the linked list
    visualize.visualize(llist)
