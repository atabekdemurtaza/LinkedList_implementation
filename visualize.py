import uuid

from graphviz import Digraph
from loguru import logger


def visualize(linked_list, filename="./images/linkedlist"):
    unique_id = uuid.uuid4()
    filename = f"{filename}_{unique_id}"

    logger.info("Generating visualization for the linked list with UUID {unique_id}.")
    dot = Digraph()

    node = linked_list.head
    while node is not None:
        dot.node(str(id(node)), str(node.val))
        if node.next:
            dot.edge(str(id(node)), str(id(node.next)))
        node = node.next

    dot.node("None", "None")
    dot.render(filename, format="png", cleanup=True)
    logger.info(f"Linked list visual saved as {filename}.png")
