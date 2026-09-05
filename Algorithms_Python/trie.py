"""
Trie Structures
===============

This module contains trie-like string data structures and algorithms.

Classes
-------
AbstractTrie
    Common interface for trie-like string data structures.

TrieNode
    Node used by trie-like structures.

PrefixTrie
    Concrete prefix trie for storing whole words and prefix queries.

Functions
---------
aho_corasick(text: str, patterns: list[str]) -> dict[str, list[int]]
    Finds all occurrences of many patterns using the Aho-Corasick algorithm.

"""

from abc import ABC, abstractmethod


class AbstractTrie(ABC):
    """
    Common interface for trie-like string data structures.

    Methods
    -------
    insert(text: str)
        Insert text into the trie-like structure.

    search(text: str) -> bool
        Check whether text is present.

    starts_with(prefix: str) -> bool
        Check whether at least one stored text starts with prefix.

    delete(text: str) -> bool
        Delete text if the concrete structure supports deletion.
    """

    @abstractmethod
    def insert(self, text: str):
        """
        Insert text into the trie-like structure.
        """

    @abstractmethod
    def search(self, text: str) -> bool:
        """
        Check whether text is present.
        """

    @abstractmethod
    def starts_with(self, prefix: str) -> bool:
        """
        Check whether at least one stored text starts with prefix.
        """

    @abstractmethod
    def delete(self, text: str) -> bool:
        """
        Delete text from the trie-like structure.
        """


class TrieNode:
    """
    Node used by trie-like structures.

    Attributes
    ----------
    children: dict[str, TrieNode]
        Outgoing transitions by character.

    is_terminal: bool
        Whether this node ends an inserted word.

    output: list[str]
        Patterns ending exactly at this node.

    matched_output: list[str]
        Patterns reported by Aho-Corasick when it reaches this node. It
        contains this node's output and outputs inherited through failure
        links.

    failure: TrieNode | None
        Aho-Corasick fallback link to the longest proper suffix represented by
        another trie node.
    """

    def __init__(self):
        self.children = {}
        self.is_terminal = False
        self.output = []
        self.matched_output = []
        self.failure = None


class PrefixTrie(AbstractTrie):
    """
    Concrete prefix trie for storing words.

    Attributes
    ----------
    root: TrieNode
        Root node of the trie.

    size: int
        Number of distinct words stored in the trie.

    Methods
    -------
    insert(text: str)
        Insert a word.

    search(text: str) -> bool
        Check whether a word is stored.

    starts_with(prefix: str) -> bool
        Check whether a stored word has the given prefix.

    delete(text: str) -> bool
        Delete a stored word.

    Examples
    --------
    >>> trie = PrefixTrie()
    >>> trie.insert("cart")
    >>> trie.starts_with("car")
    True
    >>> trie.search("car")
    False
    """

    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, text: str):
        """
        Insert a word.
        """
        node = self.root
        for character in text:
            # Every edge in a prefix trie is one character. If the edge is
            # missing, create the next node; otherwise reuse the existing
            # path shared with another word.
            node = node.children.setdefault(character, TrieNode())
        if not node.is_terminal:
            self.size += 1
        node.is_terminal = True

    def _find_node(self, text: str):
        node = self.root
        for character in text:
            # Missing edge means the word or prefix is not represented.
            if character not in node.children:
                return None
            node = node.children[character]
        return node

    def search(self, text: str) -> bool:
        """
        Check whether a word is stored.
        """
        node = self._find_node(text)
        return node is not None and node.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """
        Check whether a stored word has the given prefix.
        """
        return self._find_node(prefix) is not None

    def delete(self, text: str) -> bool:
        """
        Delete a stored word.
        """
        path = []
        node = self.root
        for character in text:
            if character not in node.children:
                return False
            # Remember the path so we can remove nodes that become useless
            # after unmarking the terminal node.
            path.append((node, character))
            node = node.children[character]
        if not node.is_terminal:
            return False

        node.is_terminal = False
        self.size -= 1
        for parent, character in reversed(path):
            child = parent.children[character]
            # Stop pruning as soon as the node is still needed either as a
            # branching point or as the end of another stored word.
            if child.children or child.is_terminal:
                break
            del parent.children[character]
        return True


def aho_corasick(text: str, patterns: list[str]) -> dict[str, list[int]]:
    """
    Find all occurrences of many patterns using Aho-Corasick algorithm.

    The algorithm first builds a prefix trie of the patterns. Then it adds
    failure links, which are the multi-pattern analogue of the fallback links
    used by Knuth-Morris-Pratt: after a mismatch, the search jumps to the
    longest suffix that is also a prefix of at least one pattern.

    Time complexity: O(n + m + z), where n is text length, m is the total
    pattern length, and z is the number of reported matches.
    Space complexity: O(m + z).

    Parameters
    ----------
    text: str
        Text in which to search.

    patterns: list[str]
        Patterns to search for. Duplicate patterns are treated as one pattern
        because the result is keyed by pattern text.

    Returns
    -------
    dict[str, list[int]]
        Mapping from every distinct pattern to all starting indexes where it
        occurs in the text.

    Examples
    --------
    >>> aho_corasick("ushers", ["he", "she", "his", "hers"])
    {'he': [2], 'she': [1], 'his': [], 'hers': [2]}
    """
    trie = PrefixTrie()
    distinct_patterns = []
    seen_patterns = set()

    for pattern in patterns:
        trie.insert(pattern)
        if pattern not in seen_patterns:
            seen_patterns.add(pattern)
            distinct_patterns.append(pattern)
            # Store the whole pattern at its terminal trie node. Later, when
            # the scan reaches this node, the pattern length gives the match
            # start index.
            trie._find_node(pattern).output.append(pattern)

    trie.root.failure = trie.root
    trie.root.matched_output = list(trie.root.output)
    queue = []

    for child in trie.root.children.values():
        # Root children have no non-empty proper suffix state to fall back to,
        # so a mismatch from them returns to the root.
        child.failure = trie.root
        child.matched_output = child.output + trie.root.matched_output
        queue.append(child)

    # Breadth-first order is important: a child failure link depends on its
    # parent's failure link, so parents must be processed before descendants.
    queue_index = 0
    while queue_index < len(queue):
        node = queue[queue_index]
        queue_index += 1

        for character, child in node.children.items():
            fallback = node.failure
            # Failure links are KMP-style fallbacks between trie nodes. Follow
            # them until a state has the needed transition or the root is
            # reached.
            while fallback is not trie.root and \
                    character not in fallback.children:
                fallback = fallback.failure

            if character in fallback.children:
                child.failure = fallback.children[character]
            else:
                child.failure = trie.root

            # If the fallback state ends any pattern, reaching this child also
            # means that shorter suffix pattern has just matched.
            child.matched_output = child.output + child.failure.matched_output
            queue.append(child)

    matches = {pattern: [] for pattern in distinct_patterns}
    if "" in matches:
        matches[""] = [index for index in range(len(text) + 1)]

    node = trie.root
    for index, character in enumerate(text):
        # Move through failure links on mismatches instead of restarting the
        # scan. This is what keeps the search linear in the text length plus
        # the number of reported matches.
        while node is not trie.root and character not in node.children:
            node = node.failure

        if character in node.children:
            node = node.children[character]
        else:
            node = trie.root

        for pattern in node.matched_output:
            if pattern != "":
                matches[pattern].append(index - len(pattern) + 1)

    return matches
