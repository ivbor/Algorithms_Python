import pytest

from Algorithms_Python.dynamic_programming_substrings import (
    LongestCommonSubstring,
    LongestPalindromicSubstring,
    ManacherLongestPalindromicSubstring,
)


@pytest.mark.parametrize('test_input, expected_length, expected_substrings',
                         [(
                             ('abcXYZdef', 'abc123def'),
                             3,
                             {'abc', 'def'},
                         ),
                          (('workattech', 'branch'), 2, {'ch'}),
                          (('helloworld', 'playword'), 3, {'wor'}),
                          (('abcdef', 'uvwxyz'), 0, {''}),
                          (('', 'abc'), 0, {''}),
                          (('same', 'same'), 4, {'same'})])
def test_longest_common_substring(
    test_input,
    expected_length,
    expected_substrings,
):
    instance = LongestCommonSubstring(*test_input)

    assert instance.solve() == expected_length
    assert instance.get_substring() in expected_substrings


def test_longest_common_substring_resets_after_mismatch():
    instance = LongestCommonSubstring('abcXYZdef', 'abc123def')

    assert instance.solve() == 3
    assert instance.dp[4][4] == 0


@pytest.mark.parametrize('klass', [
    LongestPalindromicSubstring,
    ManacherLongestPalindromicSubstring,
])
@pytest.mark.parametrize('text, expected_length, expected_substrings',
                         [('babad', 3, {'bab', 'aba'}),
                          ('cbbd', 2, {'bb'}),
                          ('bbbab', 3, {'bbb'}),
                          ('forgeeksskeegfor', 10, {'geeksskeeg'}),
                          ('aaaaaa', 6, {'aaaaaa'}),
                          ('abcdef', 1, set('abcdef')),
                          ('a', 1, {'a'}),
                          ('', 0, {''})])
def test_longest_palindromic_substring_algorithms(
    klass,
    text,
    expected_length,
    expected_substrings,
):
    instance = klass(text)

    assert instance.solve() == expected_length
    assert instance.get_substring() in expected_substrings


def test_manacher_and_dp_palindrome_substring_agree():
    text = 'abacdfgdcaba'
    dp_instance = LongestPalindromicSubstring(text)
    manacher_instance = ManacherLongestPalindromicSubstring(text)

    assert dp_instance.solve() == manacher_instance.solve()
    assert dp_instance.get_substring() in {'aba'}
    assert manacher_instance.get_substring() in {'aba'}


def test_palindromic_substring_is_not_palindromic_subsequence():
    instance = LongestPalindromicSubstring('bbbab')

    assert instance.solve() == 3
    assert instance.get_substring() == 'bbb'
