from typing import Iterator, Optional

from loguru import logger

from node import ListNode


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        logger.info("Initialized an empty LinkedList.")

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self) -> Iterator[ListNode]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Inserting from the beginning.
    def add_first(self, node: Optional[ListNode]) -> None:
        logger.info(f"Adding {node.val} at the beginning.")
        node.next = self.head
        self.head = node

    # Inserting from the end
    def add_last(self, node: Optional[ListNode]) -> None:
        logger.info(f"Adding {node.val} at the end.")
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    # Inserting Between Two Nodes
    def add_after(self, target_node_data: int, new_node: ListNode) -> None:
        logger.info(f"Adding {new_node.val} after {target_node_data}.")
        if self.head is None:
            raise Exception("List is empty.")

        for node in self:
            if node.val == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found.")

    # Inserting Before
    def add_before(self, target_node_data: int, new_node: Optional[ListNode]) -> None:
        logger.info(f"Adding {new_node.val} before {target_node_data}.")
        if self.head is None:
            raise Exception("List is empty.")

        if self.head.val == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.val == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found." % target_node_data)

    # Removing node
    def remove_node(self, target_node_data: int):
        logger.info(f"Removing {target_node_data}")
        if self.head is None:
            raise Exception("List is empty")

        if self.head.val == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.val == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")
