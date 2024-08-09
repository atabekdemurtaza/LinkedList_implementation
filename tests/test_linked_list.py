import pytest
from node import Node
from linked_list import LinkedList

@pytest.fixture
def llist():
    return LinkedList()

def test_add_first(llist):
    llist.add_first(Node('a'))
    assert llist.head.val == 'a'
    assert str(llist) == 'a -> None'

    llist.add_first(Node('b'))
    assert llist.head.val == 'b'
    assert str(llist) == 'b -> a -> None'

def test_add_last(llist):
    llist.add_first(Node('a'))
    llist.add_last(Node('b'))
    assert str(llist) == 'a -> b -> None'

    llist.add_last(Node('c'))
    assert str(llist) == 'a -> b -> c -> None'

def test_add_after(llist):
    llist.add_first(Node('a'))
    llist.add_last(Node('b'))
    llist.add_after('a', Node('c'))
    assert str(llist) == 'a -> c -> b -> None'

    llist.add_after('c', Node('d'))
    assert str(llist) == 'a -> c -> d -> b -> None'

def test_add_before(llist):
    llist.add_first(Node('b'))
    llist.add_before('b', Node('a'))
    assert str(llist) == 'a -> b -> None'

    llist.add_last(Node('c'))
    llist.add_before('c', Node('b2'))
    assert str(llist) == 'a -> b -> b2 -> c -> None'


def test_add_after_exception(llist):
    with pytest.raises(Exception) as excinfo:
        llist.add_after('x', Node('a'))
    assert str(excinfo.value) == "List is empty."

    # After adding a node, now test the 'Node not found' exception
    llist.add_first(Node('a'))
    with pytest.raises(Exception) as excinfo:
        llist.add_after('x', Node('b'))
    assert str(excinfo.value) == "Node with data 'x' not found."


def test_add_before_exception(llist):
    with pytest.raises(Exception) as excinfo:
        llist.add_before('x', Node('a'))
    assert str(excinfo.value) == "List is empty."

    # After adding a node, now test the 'Node not found' exception
    llist.add_first(Node('a'))
    with pytest.raises(Exception) as excinfo:
        llist.add_before('x', Node('b'))
    assert str(excinfo.value) == "Node with data 'x' not found."


def test_add_before_first_node(llist):
    llist.add_first(Node('b'))
    llist.add_before('b', Node('a'))
    assert str(llist) == 'a -> b -> None'


def test_remove_node(llist):
    # Test removing from an empty list
    with pytest.raises(Exception) as excinfo:
        llist.remove_node('a')
    assert str(excinfo.value) == "List is empty"

    # Add nodes and remove them
    llist.add_first(Node('a'))
    llist.add_first(Node('b'))
    llist.add_first(Node('c'))
    assert str(llist) == 'c -> b -> a -> None'

    llist.remove_node('b')
    assert str(llist) == 'c -> a -> None'

    llist.remove_node('a')
    assert str(llist) == 'c -> None'

    llist.remove_node('c')
    assert str(llist) == 'None'

    # Test removing non-existent node after the list is empty again
    llist.add_first(Node('a'))
    with pytest.raises(Exception) as excinfo:
        llist.remove_node('d')
    assert str(excinfo.value) == "Node with data 'd' not found"


def test_remove_node_first_node(llist):
    llist.add_first(Node('a'))
    llist.add_first(Node('b'))
    llist.remove_node('b')
    assert str(llist) == 'a -> None'
