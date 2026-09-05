"""
Suffix Tree
===========

This module contains compressed suffix tree structures and construction
algorithms.

Classes
-------
SuffixTreeNode
    Node used by compressed suffix trees.

SuffixTree
    Compressed suffix tree with substring search and suffix-index traversal.

Functions
---------
mccreight_suffix_tree(text: str) -> SuffixTree
    Builds a suffix tree using McCreight construction.

ukkonen_suffix_tree(text: str) -> SuffixTree
    Builds a suffix tree using Ukkonen construction.
"""

from Algorithms_Python.trie import AbstractTrie


class SuffixTreeNode:
    """
    Node used by compressed suffix trees.

    Attributes
    ----------
    children: dict[str, SuffixTreeNode]
        Outgoing compressed edges by their first character.

    start: int
        Inclusive edge-label start in the tree text.

    end: int
        Exclusive edge-label end in the tree text.

    suffix_index: int | None
        Starting position of the suffix ending at this leaf.
    """

    def __init__(self, start=-1, end=-1, parent=None):
        self.children = {}
        # Edge labels are not copied. A node stores the slice
        # text[start:end] that labels the edge from its parent.
        self.start = start
        self.end = end
        self.parent = parent
        self.suffix_index = None
        self.suffix_link = None


class SuffixTree(AbstractTrie):
    """
    Compressed suffix tree with substring search.

    The tree stores all suffixes of one text. A private terminator is appended
    when needed so every suffix ends at a distinct leaf.

    Attributes
    ----------
    text: str
        Original text without the private terminator.

    root: SuffixTreeNode
        Root node of the compressed suffix tree.

    Methods
    -------
    insert(text: str)
        Rebuild the suffix tree for text.

    search(text: str) -> bool
        Check whether text is a substring of the stored text.

    starts_with(prefix: str) -> bool
        Check whether the stored text starts with prefix.

    delete(text: str) -> bool
        Not supported for suffix trees.

    suffix_indexes() -> list[int]
        Return all suffix indexes represented by leaves.

    Examples
    --------
    >>> tree = SuffixTree("banana")
    >>> tree.search("ana")
    True
    >>> tree.suffix_indexes()
    [0, 1, 2, 3, 4, 5]
    """

    def __init__(self, text=""):
        self.root = SuffixTreeNode()
        self.text = ""
        self._tree_text = ""
        self._terminator = ""
        if text != "":
            self.insert(text)

    def insert(self, text: str):
        """
        Rebuild the suffix tree for text.
        """
        self.root = SuffixTreeNode()
        self.root.suffix_link = self.root
        self.text = text
        # A unique terminator makes no suffix a prefix of another suffix.
        # That guarantees every suffix ends at its own leaf.
        self._terminator = _choose_terminator(text)
        self._tree_text = text + self._terminator
        for start in range(len(self._tree_text)):
            node = self.root
            position = start

            while position < len(self._tree_text):
                character = self._tree_text[position]
                child = node.children.get(character)
                if child is None:
                    # No edge begins with this character, so the rest of the
                    # suffix becomes one compressed leaf edge.
                    leaf = SuffixTreeNode(
                        position, len(self._tree_text), node
                    )
                    leaf.suffix_index = start
                    node.children[character] = leaf
                    break

                edge_position = child.start
                # Walk along the compressed edge while the suffix and the edge
                # label agree character by character.
                while edge_position < child.end and \
                        position < len(self._tree_text) and \
                        self._tree_text[edge_position] == \
                        self._tree_text[position]:
                    edge_position += 1
                    position += 1

                if edge_position == child.end:
                    # The whole edge matched. Continue matching from the child
                    # node, where the next character chooses another edge.
                    node = child
                    continue

                # A mismatch in the middle of an edge splits that edge:
                # parent -> split contains the common prefix,
                # split -> old child contains the old unmatched suffix,
                # split -> new leaf contains the suffix being inserted.
                split = SuffixTreeNode(child.start, edge_position, node)
                node.children[character] = split
                child.start = edge_position
                child.parent = split
                split.children[self._tree_text[child.start]] = child

                leaf = SuffixTreeNode(position, len(self._tree_text), split)
                leaf.suffix_index = start
                split.children[self._tree_text[position]] = leaf
                break

    def search(self, text: str) -> bool:
        """
        Check whether text is a substring of the stored text.
        """
        if text == "":
            return True

        node = self.root
        position = 0
        while position < len(text):
            child = node.children.get(text[position])
            if child is None:
                return False
            edge_position = child.start
            # A substring may end in the middle of a compressed edge, so
            # reaching the end of the query is already a successful match.
            while edge_position < child.end and position < len(text):
                if self._tree_text[edge_position] != text[position]:
                    return False
                edge_position += 1
                position += 1
            node = child
        return True

    def starts_with(self, prefix: str) -> bool:
        """
        Check whether the stored text starts with prefix.
        """
        return self.text.startswith(prefix)

    def delete(self, text: str) -> bool:
        """
        Suffix trees in this module are static and do not support deletion.
        """
        raise NotImplementedError("SuffixTree does not support deletion")

    def suffix_indexes(self) -> list[int]:
        """
        Return all suffix indexes represented by leaves.
        """
        indexes = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.suffix_index is not None:
                indexes.append(node.suffix_index)
            stack.extend(node.children.values())
        return sorted(index for index in indexes if index < len(self.text))


def mccreight_suffix_tree(text: str) -> SuffixTree:
    """
    Build a suffix tree using McCreight construction.

    McCreight construction inserts suffixes from left to right. After an
    insertion creates a head node, the next suffix starts from that head's
    suffix link and uses fast-find to descend over already-known edge labels.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        Text for which the suffix tree is built.

    Returns
    -------
    SuffixTree
        Compressed suffix tree storing all suffixes of text.

    Examples
    --------
    >>> tree = mccreight_suffix_tree("banana")
    >>> tree.search("ana")
    True
    """
    # This function intentionally follows the textbook McCreight story:
    #
    # 1. Insert suffix 0 as one leaf edge.
    # 2. For suffix i, start near where suffix i - 1 was inserted.
    # 3. Use suffix links to drop the first character from a known path label.
    # 4. Use "fast-find" to skip whole compressed edges whenever the path is
    #    already known to exist.
    # 5. Finish with at most one edge split and one new leaf.
    #
    # The main thing to track is the path label of an internal node. If a node
    # spells xA from the root, its suffix link points to the node/locus spelling
    # A. McCreight makes those loci explicit whenever a link would otherwise
    # land in the middle of an edge.
    tree = SuffixTree()
    tree.root = SuffixTreeNode()
    tree.root.suffix_link = tree.root
    tree.text = text
    tree._terminator = _choose_terminator(text)
    tree._tree_text = text + tree._terminator

    if tree._tree_text == "":
        return tree

    # Suffix 0 has no previous suffix to reuse. Store it as a single compressed
    # edge from the root:
    #
    #     root
    #       |
    #       | text[0:]
    #       v
    #     leaf(0)
    #
    # Later insertions only refine this tree by splitting edges.
    first_leaf = SuffixTreeNode(0, len(tree._tree_text), tree.root)
    first_leaf.suffix_index = 0
    tree.root.children[tree._tree_text[0]] = first_leaf
    previous_leaf = first_leaf

    for suffix_start in range(1, len(tree._tree_text)):
        # The previous leaf was attached under the "head" of suffix i - 1:
        #
        #     root -- xA --> head -- tail of suffix i-1 --> previous_leaf
        #
        # Suffix i is suffix i - 1 with the first character removed, so the
        # useful starting point is the suffix link of head:
        #
        #     suffix_link(head spelling xA) = node/locus spelling A
        #
        # From there, only the part after A still needs to be inserted.
        head = previous_leaf.parent
        if head is tree.root:
            start_node = tree.root
        else:
            start_node = _mccreight_suffix_link(tree, head)

        # Fast-find has already consumed the whole path label of start_node.
        # Calculate that string-depth so position points at the first character
        # of suffix_start that is not represented by start_node's path.
        consumed = 0
        depth_node = start_node
        while depth_node.parent is not None:
            consumed += depth_node.end - depth_node.start
            depth_node = depth_node.parent
        position = suffix_start + consumed

        # Now perform the only slow part of this insertion: scan from the
        # known locus until either an edge is missing or an existing edge must
        # be split. The amortized proof says these scans stay linear overall
        # because suffix links and fast-find avoid rescanning full paths.
        node = start_node
        while position < len(tree._tree_text):
            character = tree._tree_text[position]
            child = node.children.get(character)
            if child is None:
                # No outgoing edge begins with the next suffix character.
                # The rest of this suffix becomes a new compressed leaf:
                #
                #     node
                #       |
                #       | text[position:]
                #       v
                #     leaf(suffix_start)
                previous_leaf = SuffixTreeNode(
                    position, len(tree._tree_text), node
                )
                previous_leaf.suffix_index = suffix_start
                node.children[character] = previous_leaf
                break

            edge_position = child.start
            # Compare inside the compressed edge until the suffix diverges or
            # the whole edge has matched.
            while edge_position < child.end and \
                    position < len(tree._tree_text) and \
                    tree._tree_text[edge_position] == \
                    tree._tree_text[position]:
                edge_position += 1
                position += 1

            if edge_position == child.end:
                # We consumed a whole edge label. Continue at the child node;
                # no structural change is needed yet.
                node = child
                continue

            # Mismatch inside an edge. Make the common prefix explicit and
            # branch into the old suffix and the newly inserted suffix:
            #
            # Before:
            #
            #     node -- common + old_tail --> child
            #
            # After:
            #
            #     node -- common --> split
            #                       /     \
            #              old_tail       new_tail
            #                 |              |
            #               child       leaf(suffix_start)
            #
            # This is the only split McCreight needs for this suffix.
            split = _mccreight_split_edge(tree, node, child, edge_position)
            previous_leaf = SuffixTreeNode(
                position, len(tree._tree_text), split
            )
            previous_leaf.suffix_index = suffix_start
            split.children[tree._tree_text[position]] = previous_leaf
            break

    return tree


def ukkonen_suffix_tree(text: str) -> SuffixTree:
    """
    Build a suffix tree using Ukkonen construction.

    Ukkonen construction adds the text one phase at a time while maintaining
    an active point and a remainder of suffixes still to extend.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        Text for which the suffix tree is built.

    Returns
    -------
    SuffixTree
        Compressed suffix tree storing all suffixes of text.

    Examples
    --------
    >>> tree = ukkonen_suffix_tree("banana")
    >>> tree.search("nan")
    True
    """
    # Ukkonen builds the tree online, one character (one phase) at a time.
    #
    # At the start of phase i, the tree represents text[:i]. The phase appends
    # text[i] and extends every suffix of text[:i + 1] that is not already
    # represented. The algorithm avoids explicitly touching every suffix by
    # keeping three pieces of state:
    #
    #     active_node
    #     active_edge    index of the first character on the active edge
    #     active_length  how far down that edge the active point lies
    #
    # Diagrammatically the active point is either at a node:
    #
    #     active_node
    #        ^
    #        active_length == 0
    #
    # or inside a compressed edge:
    #
    #     active_node -- text[active_edge : active_edge + active_length] --
    #                    ^ active point
    #
    # remainder counts how many suffixes from the current phase still require
    # an explicit action. Suffix links move from one pending suffix to the next
    # shorter pending suffix without restarting from root.
    tree = SuffixTree()
    tree.root = SuffixTreeNode()
    tree.root.suffix_link = tree.root
    tree.text = text
    tree._terminator = _choose_terminator(text)
    tree._tree_text = text + tree._terminator

    active_node = tree.root
    active_edge = 0
    active_length = 0
    remainder = 0
    leaf_end = _UkkonenEnd(0)

    for phase in range(len(tree._tree_text)):
        # Phase i appends tree._tree_text[i]. All leaves share the same mutable
        # leaf_end object, so every existing leaf edge grows automatically:
        #
        #     leaf edge label before: text[start : leaf_end.value]
        #     phase increments leaf_end.value
        #     leaf edge label after:  text[start : leaf_end.value]
        #
        # This is the "global end" trick that makes leaf extension O(1).
        leaf_end.value = phase + 1
        remainder += 1
        previous_internal = None

        while remainder > 0:
            if active_length == 0:
                # With no characters currently matched on an edge, the active
                # edge starts at the current phase character. In Ukkonen
                # notation, the active point is exactly active_node.
                active_edge = phase

            edge_character = tree._tree_text[active_edge]
            child = active_node.children.get(edge_character)

            if child is None:
                # Extension rule 2, leaf case:
                #
                #     active_node
                #        |
                #        | tree_text[phase:]
                #        v
                #      new leaf
                #
                # There is no edge for the active suffix's next character, so
                # the current suffix becomes a new leaf.
                leaf = SuffixTreeNode(phase, leaf_end, active_node)
                active_node.children[edge_character] = leaf
                if previous_internal is not None:
                    # The previous extension in this same phase created an
                    # internal node. Its suffix link should point to the node
                    # reached by the next shorter suffix.
                    previous_internal.suffix_link = active_node
                    previous_internal = None
            else:
                edge_end = child.end.value \
                    if isinstance(child.end, _UkkonenEnd) else child.end
                edge_length = edge_end - child.start
                if active_length >= edge_length:
                    # Skip/count trick:
                    #
                    #     active_node -- whole edge --> child
                    #
                    # If active_length covers this entire edge, jump to child
                    # in O(1) and keep the leftover active_length. This avoids
                    # repeatedly walking long compressed labels character by
                    # character.
                    active_edge += edge_length
                    active_length -= edge_length
                    active_node = child
                    continue

                next_character = tree._tree_text[child.start + active_length]
                if next_character == tree._tree_text[phase]:
                    # Extension rule 3:
                    #
                    # The current phase character is already present after the
                    # active point:
                    #
                    #     active_node -- matched -- phase_char ...
                    #
                    # Therefore this suffix, and every still shorter suffix in
                    # this phase, is already represented implicitly. Increase
                    # active_length and finish the phase.
                    active_length += 1
                    if previous_internal is not None:
                        previous_internal.suffix_link = active_node
                    break

                # Extension rule 2, split case. The active point is inside an
                # edge and the next character differs:
                #
                # Before:
                #
                #     active_node -- common + old_tail --> child
                #
                # After:
                #
                #     active_node -- common --> split
                #                           /       \
                #                   old_tail         tree_text[phase:]
                #                      |                 |
                #                    child            new leaf
                #
                # split becomes an explicit internal node, so it may need a
                # suffix link after the next extension in this phase.
                split_end = child.start + active_length
                split = SuffixTreeNode(child.start, split_end, active_node)
                active_node.children[edge_character] = split

                leaf = SuffixTreeNode(phase, leaf_end, split)
                split.children[tree._tree_text[phase]] = leaf

                child.start = split_end
                child.parent = split
                split.children[tree._tree_text[child.start]] = child

                if previous_internal is not None:
                    previous_internal.suffix_link = split
                previous_internal = split

            remainder -= 1
            if active_node is tree.root and active_length > 0:
                # Canonize at root. The next pending suffix is one character
                # shorter, so drop the first character from the active path:
                #
                #     root -- cA -- active point
                #       becomes
                #     root --  A -- active point
                #
                # active_edge shifts right to the first character of A.
                active_length -= 1
                active_edge = phase - remainder + 1
            elif active_node is not tree.root:
                # Away from root, suffix links do the same "drop the first
                # character" operation, but in one jump:
                #
                #     node spelling cA  --suffix_link-->  node spelling A
                active_node = active_node.suffix_link or tree.root

    # Convert leaf ends from the shared mutable _UkkonenEnd object to ordinary
    # integers. After construction the tree is static, so immutable endpoints
    # are simpler for search and suffix-index traversal.
    stack = [tree.root]
    while stack:
        node = stack.pop()
        if isinstance(node.end, _UkkonenEnd):
            node.end = node.end.value
        stack.extend(node.children.values())

    # Assign suffix indexes to leaves. The string-depth of a leaf is the length
    # of its suffix including the private terminator, so:
    #
    #     suffix_start = len(tree_text) - string_depth
    #
    # Internal nodes do not correspond to one suffix and keep suffix_index None.
    stack = [(tree.root, 0)]
    while stack:
        node, depth = stack.pop()
        if not node.children:
            node.suffix_index = len(tree._tree_text) - depth
            continue
        node.suffix_index = None
        for child in node.children.values():
            stack.append((child, depth + child.end - child.start))

    return tree


def _choose_terminator(text: str) -> str:
    # Prefer NUL because it sorts before ordinary printable characters.
    # If the input already contains it, scan upward until a missing code point
    # is found. The exact value does not matter, only uniqueness does.
    terminator = "\0"
    code_point = 1
    while terminator in text:
        terminator = chr(code_point)
        code_point += 1
    return terminator


def _mccreight_suffix_link(tree: SuffixTree, node: SuffixTreeNode):
    # Return the explicit node representing node.path_label[1:].
    #
    # Suppose node spells xA from the root:
    #
    #     root -- xA --> node
    #
    # The suffix link should point to A:
    #
    #     root -- A --> suffix_link(node)
    #
    # If A ends in the middle of a compressed edge, split that edge so the link
    # still points to a real node. That explicit-node invariant is what makes
    # later McCreight fast-find steps straightforward.
    if node.suffix_link is not None:
        return node.suffix_link

    parent = node.parent
    if parent is tree.root:
        # If the parent is root, the first character to remove lies on this
        # node's incoming edge, so fast-find consumes edge_label[1:].
        link_start = tree.root
        edge_start = node.start + 1
    else:
        # Otherwise the first character was part of the parent's path label.
        # The parent's suffix link has already removed it, so consume this
        # whole incoming edge from there.
        link_start = _mccreight_suffix_link(tree, parent)
        edge_start = node.start

    if edge_start >= node.end:
        node.suffix_link = link_start
    else:
        start = edge_start
        end = node.end
        link_node = link_start
        while start < end:
            child = link_node.children[tree._tree_text[start]]
            edge_length = child.end - child.start
            remaining = end - start
            if remaining < edge_length:
                # Fast-find finished inside an edge:
                #
                #     link_node -- A + B --> child
                #
                # Split after A so node.suffix_link can point at an explicit
                # node:
                #
                #     link_node -- A --> split -- B --> child
                link_node = _mccreight_split_edge(
                    tree, link_node, child, child.start + remaining
                )
                break
            start += edge_length
            link_node = child
        node.suffix_link = link_node
    return node.suffix_link


def _mccreight_split_edge(tree: SuffixTree, parent: SuffixTreeNode,
                          child: SuffixTreeNode, split_end: int):
    split = SuffixTreeNode(child.start, split_end, parent)
    parent.children[tree._tree_text[split.start]] = split
    child.start = split_end
    child.parent = split
    split.children[tree._tree_text[child.start]] = child
    return split


class _UkkonenEnd:
    def __init__(self, value: int):
        self.value = value
