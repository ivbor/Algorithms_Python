from Algorithms_Python.trie import aho_corasick, PrefixTrie


def test_prefix_trie_insert_search_prefix_and_delete():
    trie = PrefixTrie()
    for word in ("car", "card", "care", "dog", "door", ""):
        trie.insert(word)

    assert trie.size == 6
    assert trie.search("car") is True
    assert trie.search("card") is True
    assert trie.search("ca") is False
    assert trie.search("") is True
    assert trie.starts_with("do") is True
    assert trie.starts_with("z") is False

    assert trie.delete("card") is True
    assert trie.search("card") is False
    assert trie.search("car") is True
    assert trie.starts_with("car") is True
    assert trie.delete("card") is False
    assert trie.size == 5


def test_aho_corasick_finds_overlapping_patterns():
    text = "ushers"
    patterns = ["he", "she", "his", "hers"]
    expected = {"he": [2], "she": [1], "his": [], "hers": [2]}

    assert aho_corasick(text, patterns) == expected


def test_aho_corasick_reports_nested_and_repeated_matches():
    text = "abccab"

    assert aho_corasick(text, ["a", "ab", "bc", "c", "cab"]) == {
        "a": [0, 4],
        "ab": [0, 4],
        "bc": [1],
        "c": [2, 3],
        "cab": [3],
    }


def test_aho_corasick_handles_empty_and_duplicate_patterns():
    matches = aho_corasick("aaa", ["", "a", "aa", "a"])

    assert matches == {
        "": [0, 1, 2, 3],
        "a": [0, 1, 2],
        "aa": [0, 1],
    }


def test_aho_corasick_uses_all_patterns_in_one_search():
    assert aho_corasick("ababa", ["aba", "bab"]) == {
        "aba": [0, 2],
        "bab": [1],
    }
