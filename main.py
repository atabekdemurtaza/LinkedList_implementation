import visualize
from node import Node
from linked_list import LinkedList


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    llist.add_first(Node('a'))
    print(llist)
    llist.add_first(Node('b'))
    print(llist)
    llist.add_first(Node('c'))
    print(llist)

    llist.add_last(Node('d'))
    print(llist)
    llist.add_last(Node('e'))
    print(llist)
    llist.add_last(Node('f'))
    print(llist)

    llist.add_after('d', Node('g'))
    print(llist)

    llist.add_before('b', Node('v'))
    print(llist)

    llist.remove_node('a')
    print(llist)

    # Visualize the linked list
    visualize.visualize(llist)
