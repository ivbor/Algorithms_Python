import pytest

from Algorithms_Python.string_algorithms import (
    are_anagrams, are_anagrams_brute_force,
    find_pattern_brute_force, is_palindrome,
    is_palindrome_brute_force, kmp, prefix_function,
    rabin_karp, z_algorithm
)


@pytest.mark.parametrize("text, expected",
                         (("", True),
                          ("a", True),
                          ("abba", True),
                          ("abcba", True),
                          ("abca", False),
                          ("Aa", False)))
def test_palindrome_checks(text, expected):
    assert is_palindrome_brute_force(text) is expected
    assert is_palindrome(text) is expected


@pytest.mark.parametrize("first, second, expected",
                         (("", "", True),
                          ("listen", "silent", True),
                          ("triangle", "integral", True),
                          ("aabbcc", "abcabc", True),
                          ("abc", "ab", False),
                          ("abc", "abd", False),
                          ("Aa", "aA", True)))
def test_anagram_checks(first, second, expected):
    assert are_anagrams_brute_force(first, second) is expected
    assert are_anagrams(first, second) is expected


@pytest.mark.parametrize("text, pattern, expected",
                         (("", "", [0]),
                          ("abc", "", [0, 1, 2, 3]),
                          ("", "a", []),
                          ("abracadabra", "abra", [0, 7]),
                          ("aaaa", "aa", [0, 1, 2]),
                          ("abcdef", "gh", []),
                          ("abc", "abcd", [])))
def test_pattern_search(text, pattern, expected):
    assert find_pattern_brute_force(text, pattern) == expected
    assert rabin_karp(text, pattern) == expected
    assert kmp(text, pattern) == expected


def test_rabin_karp_matches_brute_force_for_unicode_text():
    text = "zażółć zażółć"
    pattern = "żół"

    assert rabin_karp(text, pattern) == \
        find_pattern_brute_force(text, pattern)


@pytest.mark.parametrize("text, expected",
                         (("", []),
                          ("a", [0]),
                          ("aaaa", [0, 1, 2, 3]),
                          ("abacaba", [0, 0, 1, 0, 1, 2, 3]),
                          ("abcabcd", [0, 0, 0, 1, 2, 3, 0]),
                          ("aabaaab", [0, 1, 0, 1, 2, 2, 3])))
def test_prefix_function(text, expected):
    assert prefix_function(text) == expected


@pytest.mark.parametrize("text, expected",
                         (("", []),
                          ("a", [0]),
                          ("aaaa", [0, 3, 2, 1]),
                          ("abacaba", [0, 0, 1, 0, 3, 0, 1]),
                          ("aabcaabxaaaz",
                           [0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0])))
def test_z_algorithm(text, expected):
    assert z_algorithm(text) == expected


@pytest.mark.parametrize("text, pattern, expected",
                         (("abcxabcdabxabcdabcdabcy", "abcdabcy", [15]),
                          ("abababab", "abab", [0, 2, 4]),
                          ("mississippi", "issi", [1, 4]),
                          ("zażółć zażółć", "żół", [2, 9])))
def test_kmp_pattern_search(text, pattern, expected):
    assert kmp(text, pattern) == expected
    assert kmp(text, pattern) == find_pattern_brute_force(text, pattern)
