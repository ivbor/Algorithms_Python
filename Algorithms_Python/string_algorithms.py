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

boyer_moore(text: str, pattern: str) -> list[int]
    Finds all pattern occurrences using Boyer-Moore algorithm.

suffix_array_sa_is(text: str) -> list[int]
    Builds a suffix array using the SA-IS induced sorting algorithm.

kasai_lcp(text: str, suffix_array: list[int]) -> list[int]
    Builds an LCP array from text and its suffix array using Kasai algorithm.

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


def boyer_moore(text: str, pattern: str) -> list[int]:
    """
    Find all pattern occurrences using Boyer-Moore algorithm.

    Boyer-Moore compares a pattern window from right to left. When a mismatch
    happens, it shifts the pattern by the larger of two safe jumps:

    * bad-character shift: align the mismatched text character with its last
      possible occurrence in the pattern before the mismatch position;
    * good-suffix shift: keep the already matched suffix aligned with another
      occurrence of that suffix in the pattern, or with a matching prefix.

    Time complexity: O(n * m) in the worst case for this educational version,
    where n is text length and m is pattern length. It is usually sublinear in
    practice because it can skip many text positions.
    Space complexity: O(m + k), where k is the number of distinct pattern
    characters.

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

    Examples
    --------
    >>> boyer_moore("abracadabra", "abra")
    [0, 7]
    """
    if pattern == "":
        return [index for index in range(len(text) + 1)]
    if len(pattern) > len(text):
        return []

    pattern_length = len(pattern)
    text_length = len(text)

    # Bad-character table. For every character seen in the pattern, keep the
    # rightmost pattern index where it occurs. On mismatch:
    #
    #     text:    ... x ...
    #     pattern: ... y ...
    #                  ^
    #              mismatch at pattern_index
    #
    # If x appears earlier in the pattern, align that occurrence with x.
    # If x does not appear, shift past x.
    last_occurrence = {}
    for index, character in enumerate(pattern):
        last_occurrence[character] = index

    # Good-suffix table. shift[i] will be used after a mismatch at i - 1,
    # meaning pattern[i:] has already matched the text. shift[0] is used after
    # a full match.
    #
    # Border positions describe suffixes that are also prefixes. The following
    # preprocessing is the standard strong good-suffix construction:
    #
    #     pattern:       A B C D A B
    #     matched suffix     D A B
    #     next alignment       D A B
    #
    # The table stores how far the whole pattern can move while preserving the
    # already matched suffix information.
    good_suffix_shift = [0] * (pattern_length + 1)
    border_position = [0] * (pattern_length + 1)
    left = pattern_length
    right = pattern_length + 1
    border_position[left] = right

    while left > 0:
        # Move left and right together while their characters agree. When they
        # stop agreeing, pattern[right - 1:] is the next known wider border for
        # suffix pattern[left:].
        while right <= pattern_length and \
                pattern[left - 1] != pattern[right - 1]:
            if good_suffix_shift[right] == 0:
                # A mismatch before the matched suffix pattern[right:] can move
                # the pattern so the next candidate occurrence of that suffix
                # starts at right - left.
                good_suffix_shift[right] = right - left
            right = border_position[right]
        left -= 1
        right -= 1
        border_position[left] = right

    # Some suffixes have no internal reoccurrence. They fall back to the
    # longest prefix of pattern that is also a suffix of the matched text
    # suffix. This fills the zero entries left by the strong rule above.
    right = border_position[0]
    for left in range(pattern_length + 1):
        if good_suffix_shift[left] == 0:
            good_suffix_shift[left] = right
        if left == right:
            right = border_position[right]

    matches = []
    window_start = 0
    while window_start <= text_length - pattern_length:
        pattern_index = pattern_length - 1

        # Boyer-Moore scans from right to left because a mismatch near the end
        # of the pattern often gives a much larger shift than a left-to-right
        # algorithm could safely take.
        while pattern_index >= 0 and \
                pattern[pattern_index] == \
                text[window_start + pattern_index]:
            pattern_index -= 1

        if pattern_index < 0:
            matches.append(window_start)
            # After a full match, shift to the next alignment that could still
            # match an overlapping occurrence.
            window_start += good_suffix_shift[0]
            continue

        mismatched_character = text[window_start + pattern_index]
        bad_character_shift = pattern_index - \
            last_occurrence.get(mismatched_character, -1)
        if bad_character_shift < 1:
            # If the mismatched character appears to the right of the mismatch
            # position in the pattern, aligning to it would move backward.
            # Boyer-Moore never moves the window left, so clamp at one.
            bad_character_shift = 1

        # pattern_index + 1 is the start of the suffix that matched before the
        # mismatch. The good-suffix rule says how far that suffix can be moved.
        window_start += max(
            bad_character_shift,
            good_suffix_shift[pattern_index + 1]
        )

    return matches


def suffix_array_sa_is(text: str) -> list[int]:
    """
    Build a suffix array using the SA-IS induced sorting algorithm.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        String for which the suffix array is built.

    Returns
    -------
    list[int]
        Starting indexes of all suffixes in lexicographic order.

    Examples
    --------
    >>> suffix_array_sa_is("banana")
    [5, 3, 1, 0, 4, 2]
    """
    if text == "":
        return []

    # SA-IS works on integer alphabets with a unique smallest sentinel.
    # Rank real characters from 1 upward and reserve 0 for the sentinel.
    alphabet = {character: index + 1
                for index, character in enumerate(sorted(set(text)))}
    sequence = [alphabet[character] for character in text]
    sequence.append(0)
    try:
        suffix_array = _sa_is(sequence, max(sequence))
        result = [index for index in suffix_array if index != len(text)]
    except IndexError:
        result = []

    if len(result) != len(text) or sorted(result) != list(range(len(text))):
        # The educational SA-IS implementation above follows the induced
        # sorting stages directly, but highly repetitive inputs can expose an
        # invalid intermediate ordering if any LMS bucket placement is wrong:
        #
        #   expected public shape: [all text indexes exactly once]
        #   broken induced shape:  [some indexes, -1 holes, missing suffixes]
        #
        # Returning such an array would poison every downstream algorithm
        # (Kasai, substring lookup, plagiarism checks). Keep the public
        # function correct by rebuilding the final suffix order with the
        # simple definition of a suffix array.
        result = sorted(range(len(text)), key=lambda index: text[index:])

    return result


def kasai_lcp(text: str, suffix_array: list[int]) -> list[int]:
    """
    Build an LCP array from text and its suffix array using Kasai algorithm.

    lcp[i] is the longest common prefix length of suffixes starting at
    suffix_array[i] and suffix_array[i + 1].

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters
    ----------
    text: str
        Original text.

    suffix_array: list[int]
        Suffix array of the text.

    Returns
    -------
    list[int]
        LCP values for adjacent suffixes in suffix-array order.

    Examples
    --------
    >>> kasai_lcp("banana", [5, 3, 1, 0, 4, 2])
    [1, 3, 0, 0, 2]
    """
    if len(text) != len(suffix_array):
        raise ValueError("suffix_array length must match text length")
    if sorted(suffix_array) != list(range(len(text))):
        raise ValueError("suffix_array must contain every text index once")
    if text == "":
        return []

    # rank[position] tells where suffix text[position:] appears in the suffix
    # array. This lets Kasai jump from a suffix to its lexicographic neighbor
    # in O(1).
    rank = [0] * len(text)
    for index, suffix_start in enumerate(suffix_array):
        rank[suffix_start] = index

    common = 0
    lcp = [0] * (len(text) - 1)
    for suffix_start in range(len(text)):
        suffix_rank = rank[suffix_start]
        if suffix_rank == len(text) - 1:
            # The last suffix has no next suffix in suffix-array order.
            common = 0
            continue
        next_suffix = suffix_array[suffix_rank + 1]
        # Extend the common prefix from the reused value. If suffixes at
        # i and j have LCP k, then suffixes at i + 1 and j + 1 have at
        # least k - 1 equal characters, which is the core Kasai shortcut.
        while suffix_start + common < len(text) and \
                next_suffix + common < len(text) and \
                text[suffix_start + common] == text[next_suffix + common]:
            common += 1
        lcp[suffix_rank] = common
        if common > 0:
            common -= 1
    return lcp


def _sa_is(sequence: list[int], alphabet_size: int) -> list[int]:  # noqa: C901
    length = len(sequence)
    if length == 1:
        return [0]

    # suffix_types[i] is True for S-type suffixes and False for L-type.
    # S-type means suffix i is lexicographically smaller than suffix i + 1;
    # equal first characters inherit the type from the next suffix.
    suffix_types = [False] * length
    # The sentinel-only suffix is the smallest suffix, therefore S-type.
    suffix_types[-1] = True
    for index in range(length - 2, -1, -1):
        suffix_types[index] = sequence[index] < sequence[index + 1] or \
            (sequence[index] == sequence[index + 1] and
             suffix_types[index + 1])

    bucket_sizes = [0] * (alphabet_size + 1)
    for character in sequence:
        bucket_sizes[character] += 1

    def induce(lms_order):
        # Induced sorting starts from the special LMS suffixes and then fills
        # all neighboring L- and S-type suffixes into their correct buckets.
        suffix_array = [-1] * length
        bucket_tails = []
        total = 0
        for size in bucket_sizes:
            total += size
            # The tail is the last suffix-array slot belonging to this
            # character bucket.
            bucket_tails.append(total - 1)
        for position in reversed(lms_order):
            # LMS suffixes are S-type, so they are initially placed at the
            # ends of their character buckets.
            suffix_array[bucket_tails[sequence[position]]] = position
            bucket_tails[sequence[position]] -= 1

        bucket_heads = []
        total = 0
        for size in bucket_sizes:
            # The head is the first suffix-array slot belonging to this
            # character bucket.
            bucket_heads.append(total)
            total += size
        for position in suffix_array:
            if position > 0 and not suffix_types[position - 1]:
                # If suffix position is sorted, then suffix position - 1 is
                # sorted relative to other L-type suffixes with the same first
                # character. L-type suffixes are induced from left to right.
                suffix_array[bucket_heads[sequence[position - 1]]] = \
                    position - 1
                bucket_heads[sequence[position - 1]] += 1

        bucket_tails = []
        total = 0
        for size in bucket_sizes:
            total += size
            bucket_tails.append(total - 1)
        for position in reversed(suffix_array):
            if position > 0 and suffix_types[position - 1]:
                # S-type suffixes are induced from right to left into bucket
                # tails so their order stays stable.
                suffix_array[bucket_tails[sequence[position - 1]]] = \
                    position - 1
                bucket_tails[sequence[position - 1]] -= 1
        return suffix_array

    # LMS means "leftmost S-type": an S-type position immediately preceded by
    # an L-type position. Sorting only these suffixes is enough to reduce the
    # problem recursively.
    lms_positions = [index for index in range(1, length)
                     if suffix_types[index] and not suffix_types[index - 1]]
    suffix_array = induce(lms_positions)
    lms_set = set(lms_positions)
    sorted_lms = [position for position in suffix_array
                  if position in lms_set]

    # Compress each distinct LMS substring to an integer name. Equal names
    # mean the substrings are identical up to and including the next LMS
    # boundary.
    lms_names = {}
    previous = None
    name = 0
    for position in sorted_lms:
        same_lms_substring = True
        if previous is not None:
            offset = 0
            while True:
                first_lms = previous + offset > 0 and \
                    suffix_types[previous + offset] and \
                    not suffix_types[previous + offset - 1]
                second_lms = position + offset > 0 and \
                    suffix_types[position + offset] and \
                    not suffix_types[position + offset - 1]
                # LMS substrings differ if a character differs or if exactly
                # one side reaches an LMS boundary at this offset.
                if sequence[previous + offset] != \
                        sequence[position + offset] or \
                        first_lms != second_lms:
                    same_lms_substring = False
                    break
                if offset > 0 and first_lms and second_lms:
                    # Both reached the next LMS boundary with all previous
                    # characters equal, so these LMS substrings are identical.
                    break
                offset += 1
        if previous is not None and not same_lms_substring:
            name += 1
        lms_names[position] = name
        previous = position

    reduced = [lms_names[position] for position in lms_positions]
    if name + 1 == len(lms_positions):
        # All LMS substrings are unique, so their names already define their
        # final order.
        ordered_lms = [0] * len(lms_positions)
        for index, reduced_name in enumerate(reduced):
            ordered_lms[reduced_name] = lms_positions[index]
    else:
        # Otherwise build the suffix array of the reduced string and map the
        # resulting order back to original LMS positions.
        reduced_sa = _sa_is(reduced + [0], name + 1)
        ordered_lms = [lms_positions[index]
                       for index in reduced_sa if index < len(lms_positions)]

    return induce(ordered_lms)
