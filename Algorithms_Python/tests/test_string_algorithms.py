import pytest

from Algorithms_Python.string_algorithms import (
    are_anagrams, are_anagrams_brute_force,
    boyer_moore, find_pattern_brute_force, is_palindrome,
    is_palindrome_brute_force, kmp, prefix_function,
    kasai_lcp, rabin_karp, suffix_array_sa_is,
    z_algorithm
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
    assert boyer_moore(text, pattern) == expected


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


@pytest.mark.parametrize("text, pattern, expected",
                         (("HERE IS A SIMPLE EXAMPLE", "EXAMPLE", [17]),
                          ("abcxabcdabxabcdabcdabcy", "abcdabcy", [15]),
                          ("abababab", "abab", [0, 2, 4]),
                          ("aaaaa", "aaa", [0, 1, 2]),
                          ("mississippi", "issi", [1, 4]),
                          ("zażółć zażółć", "żół", [2, 9])))
def test_boyer_moore_pattern_search(text, pattern, expected):
    assert boyer_moore(text, pattern) == expected
    assert boyer_moore(text, pattern) == \
        find_pattern_brute_force(text, pattern)


@pytest.mark.parametrize("text, expected",
                         (("", []),
                          ("a", [0]),
                          ("aaaa", [3, 2, 1, 0]),
                          ("banana", [5, 3, 1, 0, 4, 2]),
                          ("mississippi",
                           [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]),
                          ("abracadabra",
                           [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]),
                          ("zażółć zażółć",
                           [6, 8, 1, 7, 0, 10, 3, 12, 5, 11, 4, 9, 2])))
def test_suffix_array_sa_is(text, expected):
    assert suffix_array_sa_is(text) == expected


@pytest.mark.parametrize("text, expected",
                         (("", []),
                          ("a", []),
                          ("banana", [1, 3, 0, 0, 2]),
                          ("mississippi",
                           [1, 1, 4, 0, 0, 1, 0, 2, 1, 3]),
                          ("abracadabra",
                           [1, 4, 1, 1, 0, 3, 0, 0, 0, 2])))
def test_kasai_lcp(text, expected):
    suffix_array = suffix_array_sa_is(text)
    assert kasai_lcp(text, suffix_array) == expected


def test_kasai_lcp_rejects_invalid_suffix_array():
    with pytest.raises(ValueError):
        kasai_lcp("abc", [0, 1])
    with pytest.raises(ValueError):
        kasai_lcp("abc", [0, 1, 1])
