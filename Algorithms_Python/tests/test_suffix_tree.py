import pytest

from Algorithms_Python.suffix_tree import (
    mccreight_suffix_tree, SuffixTree, ukkonen_suffix_tree
)


@pytest.mark.parametrize("builder",
                         (SuffixTree, mccreight_suffix_tree,
                          ukkonen_suffix_tree))
@pytest.mark.parametrize("text",
                         ("banana", "mississippi", "abracadabra",
                          "aaaaa", "abcabxabcd", "zażółć zażółć"))
def test_suffix_tree_builders_store_suffixes_and_substrings(builder, text):
    tree = builder(text)

    assert tree.suffix_indexes() == list(range(len(text)))
    for start in range(len(text)):
        assert tree.search(text[start:]) is True

    substrings = {""}
    for start in range(len(text)):
        substrings.add(text[start:start + 1])
        substrings.add(text[start:start + 3])
        substrings.add(text[start:len(text)])
    for substring in substrings:
        assert tree.search(substring) is True

    assert tree.search(text + "#") is False
    assert tree.starts_with(text[:3]) is True


@pytest.mark.parametrize("builder",
                         (SuffixTree, mccreight_suffix_tree,
                          ukkonen_suffix_tree))
def test_suffix_tree_delete_is_not_supported(builder):
    tree = builder("banana")

    with pytest.raises(NotImplementedError):
        tree.delete("ana")


@pytest.mark.parametrize("builder",
                         (mccreight_suffix_tree, ukkonen_suffix_tree))
def test_suffix_tree_algorithm_builders_create_suffix_links(builder):
    tree = builder("mississippi")
    internal_nodes = []
    stack = list(tree.root.children.values())
    while stack:
        node = stack.pop()
        if node.children:
            internal_nodes.append(node)
            stack.extend(node.children.values())

    assert len(internal_nodes) > 0
    assert all(node.suffix_link is not None for node in internal_nodes)
