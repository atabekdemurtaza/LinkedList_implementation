import pytest
from unittest.mock import patch
from node import Node
from linked_list import LinkedList
import visualize

@patch("visualize.Digraph.render")
@patch("visualize.logger.info")
def test_visualize(mock_logger_info, mock_render):
    llist = LinkedList()

    llist.add_first(Node('a'))
    visualize.visualize(llist, filename='./images/test_linkedlist_1')

    llist.add_first(Node('b'))
    visualize.visualize(llist, filename='./images/test_linkedlist_2')

    llist.add_first(Node('c'))
    visualize.visualize(llist, filename='./images/test_linkedlist_3')

    assert mock_render.call_count == 3

    # Check that the filenames used for saving start with the expected prefix
    filenames = [call.args[0] for call in mock_render.call_args_list]
    assert all(fname.startswith('./images/test_linkedlist_') for fname in filenames)
