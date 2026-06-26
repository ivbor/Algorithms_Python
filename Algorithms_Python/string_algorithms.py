"""
String Algorithms
=================

This module contains basic string algorithms.

Functions
---------
is_palindrome_brute_force(text: str) -> bool
    Checks whether a string is a palindrome by comparing it with its reverse.

is_palindrome(text: str) -> bool
    Checks whether a string is a palindrome using two pointers.

are_anagrams_brute_force(first: str, second: str) -> bool
    Checks whether two strings are anagrams by repeatedly matching
    characters.

are_anagrams(first: str, second: str) -> bool
    Checks whether two strings are anagrams using character counts.

find_pattern_brute_force(text: str, pattern: str) -> list[int]
    Finds all pattern occurrences by checking every possible position.

rabin_karp(text: str, pattern: str) -> list[int]
    Finds all pattern occurrences using Rabin-Karp rolling hash.

prefix_function(text: str) -> list[int]
    Calculates the prefix function for a string.

z_algorithm(text: str) -> list[int]
    Calculates Z-values for a string.

kmp(text: str, pattern: str) -> list[int]
    Finds all pattern occurrences using Knuth-Morris-Pratt algorithm.
"""


def is_palindrome_brute_force(text: str) -> bool:
    """
    Check whether a string is a palindrome by reversing it.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        String to check.

    Returns
    -------
    bool
        Whether the string is a palindrome.
    """
    return text == text[::-1]


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome using two pointers.

    Time complexity: O(n)
    Space complexity: O(1)

    Parameters
    ----------
    text: str
        String to check.

    Returns
    -------
    bool
        Whether the string is a palindrome.
    """
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def are_anagrams_brute_force(first: str, second: str) -> bool:
    """
    Check whether two strings are anagrams using repeated linear search.

    Time complexity: O(n ** 2)
    Space complexity: O(n)

    Parameters
    ----------
    first: str
        First string to compare.

    second: str
        Second string to compare.

    Returns
    -------
    bool
        Whether the two strings are anagrams.
    """
    if len(first) != len(second):
        return False

    unmatched = list(second)
    for character in first:
        try:
            unmatched.remove(character)
        except ValueError:
            return False
    return len(unmatched) == 0


def are_anagrams(first: str, second: str) -> bool:
    """
    Check whether two strings are anagrams using character counts.

    Time complexity: O(n)
    Space complexity: O(k), where k is the number of distinct characters.

    Parameters
    ----------
    first: str
        First string to compare.

    second: str
        Second string to compare.

    Returns
    -------
    bool
        Whether the two strings are anagrams.
    """
    if len(first) != len(second):
        return False

    counts = {}
    for character in first:
        counts[character] = counts.get(character, 0) + 1

    for character in second:
        if character not in counts:
            return False
        counts[character] -= 1
        if counts[character] == 0:
            del counts[character]

    return len(counts) == 0


def find_pattern_brute_force(text: str, pattern: str) -> list[int]:
    """
    Find all pattern occurrences by checking every possible position.

    Time complexity: O((n - m + 1) * m), where n is text length and m is
    pattern length. In the worst case this is O(n * m).
    Space complexity: O(r), where r is the number of returned matches.

    Parameters
    ----------
    text: str
        Text in which to search.

    pattern: str
        Pattern to search for.

    Returns
    -------
    list[int]
        Starting indexes of all pattern occurrences.
    """
    if pattern == "":
        return [i for i in range(len(text) + 1)]
    if len(pattern) > len(text):
        return []

    matches = []
    pattern_length = len(pattern)
    for index in range(len(text) - pattern_length + 1):
        if text[index:index + pattern_length] == pattern:
            matches.append(index)
    return matches


def rabin_karp(text: str, pattern: str) -> list[int]:
    """
    Find all pattern occurrences using Rabin-Karp rolling hash.

    Time complexity: O(n + m) on average, where n is text length and m is
    pattern length. Worst-case time complexity is O(n * m) when many hash
    collisions require direct substring checks.
    Space complexity: O(r), where r is the number of returned matches.

    Parameters
    ----------
    text: str
        Text in which to search.

    pattern: str
        Pattern to search for.

    Returns
    -------
    list[int]
        Starting indexes of all pattern occurrences.
    """
    if pattern == "":
        return [i for i in range(len(text) + 1)]
    if len(pattern) > len(text):
        return []

    base = 256
    modulus = 1_000_000_007
    pattern_length = len(pattern)
    high_order = pow(base, pattern_length - 1, modulus)
    pattern_hash = 0
    window_hash = 0

    for index in range(pattern_length):
        pattern_hash = \
            (pattern_hash * base + ord(pattern[index])) % modulus
        window_hash = \
            (window_hash * base + ord(text[index])) % modulus

    matches = []
    for index in range(len(text) - pattern_length + 1):
        if pattern_hash == window_hash and \
                text[index:index + pattern_length] == pattern:
            matches.append(index)

        if index < len(text) - pattern_length:
            window_hash = \
                (window_hash - ord(text[index]) * high_order) % modulus
            window_hash = \
                (window_hash * base + ord(text[index + pattern_length])) \
                % modulus

    return matches


def prefix_function(text: str) -> list[int]:
    """
    Calculate the prefix function for a string.

    For every position i, the returned value is the length of the longest
    proper prefix of text[:i + 1] which is also a suffix of text[:i + 1].

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        String for which the prefix function is calculated.

    Returns
    -------
    list[int]
        Prefix-function values for all positions of the string.
    """
    prefix = [0] * len(text)

    for index in range(1, len(text)):
        border = prefix[index - 1]
        while border > 0 and text[index] != text[border]:
            border = prefix[border - 1]
        if text[index] == text[border]:
            border += 1
        prefix[index] = border

    return prefix


def z_algorithm(text: str) -> list[int]:
    """
    Calculate Z-values for a string.

    For every position i, the returned value is the length of the longest
    substring starting at i which is also a prefix of the whole string.
    The first value is set to 0.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        String for which Z-values are calculated.

    Returns
    -------
    list[int]
        Z-values for all positions of the string.
    """
    z_values = [0] * len(text)
    left = 0
    right = 0

    for index in range(1, len(text)):
        if index <= right:
            z_values[index] = min(right - index + 1,
                                  z_values[index - left])

        while index + z_values[index] < len(text) and \
                text[z_values[index]] == text[index + z_values[index]]:
            z_values[index] += 1

        if index + z_values[index] - 1 > right:
            left = index
            right = index + z_values[index] - 1

    return z_values


def kmp(text: str, pattern: str) -> list[int]:
    """
    Find all pattern occurrences using Knuth-Morris-Pratt algorithm.

    This implementation uses the prefix function to avoid rechecking
    characters after a mismatch.

    Time complexity: O(n + m), where n is text length and m is pattern
    length.
    Space complexity: O(m + r), where r is the number of returned matches.

    Parameters
    ----------
    text: str
        Text in which to search.

    pattern: str
        Pattern to search for.

    Returns
    -------
    list[int]
        Starting indexes of all pattern occurrences.
    """
    if pattern == "":
        return [i for i in range(len(text) + 1)]
    if len(pattern) > len(text):
        return []

    prefix = prefix_function(pattern)
    matches = []
    matched = 0

    for index, character in enumerate(text):
        while matched > 0 and character != pattern[matched]:
            matched = prefix[matched - 1]
        if character == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            matches.append(index - len(pattern) + 1)
            matched = prefix[matched - 1]

    return matches
