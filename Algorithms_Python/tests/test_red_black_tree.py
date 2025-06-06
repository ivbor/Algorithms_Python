import pytest
import random
import math

from Algorithms_Python.red_black_tree import RedBlackTree, TreeNode


@pytest.fixture
def rb_tree():
    tree = RedBlackTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    return tree


def test_insert(rb_tree):
    assert rb_tree.in_order_traversal() == [2, 3, 4, 5, 6, 7, 8]


def test_rotations():
    node0 = TreeNode(data=5)
    node1 = TreeNode(data=4)
    node2 = TreeNode(data=6)
    node3 = TreeNode(data=7)
    node2.parent = node3
    node0.parent = node2
    node1.parent = node0
    node3.children = [None, node2]
    node2.children = [node0, None]
    node0.children = [node1, None]
    RedBlackTree._right_rotate(self=RedBlackTree(), node=node2)
    assert node0.children == [node1, node2]
    assert node1.parent == node0
    assert node2.parent == node0


def test_delete(rb_tree):
    rb_tree.delete(4)
    assert rb_tree.in_order_traversal() == [2, 3, 5, 6, 7, 8]
    rb_tree.delete(5)
    assert rb_tree.in_order_traversal() == [2, 3, 6, 7, 8]
    rb_tree.delete(2)
    assert rb_tree.in_order_traversal() == [3, 6, 7, 8]
    rb_tree.delete(8)
    assert rb_tree.in_order_traversal() == [3, 6, 7]


def test_delete_with_error(rb_tree):
    rb_tree_list = rb_tree.in_order_traversal()
    for _ in range(7):
        elt_to_delete = random.choice(rb_tree_list)
        rb_tree.delete(elt_to_delete)
    with pytest.raises(IndexError):
        rb_tree.delete(None)


def test_search(rb_tree):
    assert rb_tree._search(rb_tree.root, 3) is not None
    assert rb_tree._search(rb_tree.root, 9) is None


def test_random_length_and_elts():
    rbtree = RedBlackTree()
    rbtree_length = random.randint(1000, 2000)
    for _ in range(rbtree_length):
        rbtree.insert(random.randint(-1000, 1000))
        assert rbtree.max_height() <= 3 * int(math.log2(rbtree.size + 1) + 1)
    list_rbtree = rbtree.in_order_traversal()
    assert len(list_rbtree) == rbtree_length
    assert sorted(list_rbtree) == list_rbtree
    for _ in range(rbtree_length):
        elt_to_delete = random.choice(list_rbtree)
        rbtree.delete(elt_to_delete)
        list_rbtree.remove(elt_to_delete)
        assert len(list_rbtree) == rbtree.size
        assert sorted(list_rbtree) == rbtree.in_order_traversal()
    assert len(rbtree.in_order_traversal()) == 0
