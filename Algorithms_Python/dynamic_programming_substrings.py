"""
Dynamic Programming Substring Algorithms
========================================

This module contains substring-oriented dynamic programming problems and
closely related substring algorithms.

Classes
-------
LongestCommonSubstring
    Class for finding the LongestCommonSubstring of two strings.

LongestPalindromicSubstring
    Class for finding the LongestPalindromicSubstring using dynamic
    programming.

ManacherLongestPalindromicSubstring
    Class for finding the LongestPalindromicSubstring using Manacher's
    algorithm.

"""

from Algorithms_Python.dynamic_programming import DynamicProgrammingProblem


class LongestCommonSubstring(DynamicProgrammingProblem):
    """
    Class for finding the Longest Common Substring of two strings.

    A substring is contiguous. This is the important difference from
    LongestCommonSubsequence: after a mismatch the current common suffix must
    reset to zero instead of carrying the best value from the left or top
    table cell.

    Attributes
    ----------
    str1: str
        First string of the two to find the substring for.

    str2: str
        Second string of the two to find the substring for.

    Methods
    -------
    solve(self) -> int
        Finds the length of the Longest Common Substring.

    get_substring(self) -> str
        Returns one longest common substring.

    """

    def __init__(self, str1, str2):
        '''
            Creates an instance of the LongestCommonSubstring class

            Parameters
            ----------
            str1: str
                First string of the two to find the substring for.

            str2: str
                Second string of the two to find the substring for.

            Returns
            -------
            None
        '''
        super().__init__()
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)
        self.end_index = 0
        self.length = 0

    def solve(self):
        """
        Finds the length of the Longest Common Substring.

        Returns
        -------
        int
            The length of the Longest Common Substring.

        """
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.length = 0
        self.end_index = 0

        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    # dp[i][j] means "length of the common suffix ending at
                    # str1[i - 1] and str2[j - 1]".
                    #
                    #     str1: ... A B C
                    #                   ^
                    #     str2: ... X B C
                    #                   ^
                    #
                    # If both ends match, extend the previous diagonal suffix.
                    self.dp[i][j] = self.dp[i - 1][j - 1] + 1

                    if self.dp[i][j] > self.length:
                        self.length = self.dp[i][j]
                        self.end_index = i
                else:
                    # A mismatch breaks contiguity. Unlike subsequence LCS,
                    # there is no max(top, left) transition here.
                    self.dp[i][j] = 0

        return self.length

    def get_substring(self):
        """
        Returns one longest common substring.

        Returns
        -------
        str
            One longest common substring. If there is no common substring,
            returns an empty string.

        """
        if self.dp is None:
            self.solve()
        start = self.end_index - self.length
        return self.str1[start:self.end_index]


class LongestPalindromicSubstring(DynamicProgrammingProblem):
    """
    Class for finding the Longest Palindromic Substring using DP.

    The dynamic programming table stores whether every closed interval
    text[left:right + 1] is a palindrome. This gives O(n^2) time and O(n^2)
    memory. Manacher's algorithm below solves the same task in O(n), but this
    version is useful for learning the recurrence directly.

    Attributes
    ----------
    text: str
        String where the longest palindromic substring is searched.

    Methods
    -------
    solve(self) -> int
        Finds the length of the Longest Palindromic Substring.

    get_substring(self) -> str
        Returns one longest palindromic substring.

    """

    def __init__(self, text):
        '''
            Creates an instance of the LongestPalindromicSubstring class

            Parameters
            ----------
            text: str
                String where the longest palindromic substring is searched.

            Returns
            -------
            None
        '''
        super().__init__()
        self.text = text
        self.n = len(text)
        self.start = 0
        self.length = 0

    def solve(self):
        """
        Finds the length of the Longest Palindromic Substring.

        Returns
        -------
        int
            The length of the Longest Palindromic Substring.

        """
        if self.n == 0:
            self.dp = []
            self.start = 0
            self.length = 0
            return 0

        self.dp = [[False] * self.n for _ in range(self.n)]
        self.start = 0
        self.length = 1

        for index in range(self.n):
            self.dp[index][index] = True

        # Fill intervals by length so the inner interval is already known
        # before it is used:
        #
        #     text:  a b b a
        #            ^     ^
        #          left   right
        #
        # The outer characters must match, and the inside "bb" must already be
        # a palindrome. Length 2 is a special case because the inside interval
        # is empty.
        for interval_length in range(2, self.n + 1):
            for left in range(self.n - interval_length + 1):
                right = left + interval_length - 1
                ends_match = self.text[left] == self.text[right]
                inner_is_palindrome = interval_length == 2 or \
                    self.dp[left + 1][right - 1]

                if ends_match and inner_is_palindrome:
                    self.dp[left][right] = True
                    if interval_length > self.length:
                        self.start = left
                        self.length = interval_length

        return self.length

    def get_substring(self):
        """
        Returns one longest palindromic substring.

        Returns
        -------
        str
            One longest palindromic substring.

        """
        if self.dp is None:
            self.solve()
        return self.text[self.start:self.start + self.length]


class ManacherLongestPalindromicSubstring(DynamicProgrammingProblem):
    """
    Class for finding the Longest Palindromic Substring using Manacher.

    Manacher's algorithm keeps palindrome radii around every possible center.
    To avoid separate odd-length and even-length logic, the input is
    transformed by inserting separators:

        text:        a b b a
        transformed: ^ # a # b # b # a # $

    Every palindrome in the transformed string has an odd number of
    characters, so a single expansion rule handles both original cases.

    Attributes
    ----------
    text: str
        String where the longest palindromic substring is searched.

    Methods
    -------
    solve(self) -> int
        Finds the length of the Longest Palindromic Substring.

    get_substring(self) -> str
        Returns one longest palindromic substring.

    """

    def __init__(self, text):
        '''
            Creates an instance of the ManacherLongestPalindromicSubstring
            class

            Parameters
            ----------
            text: str
                String where the longest palindromic substring is searched.

            Returns
            -------
            None
        '''
        super().__init__()
        self.text = text
        self.n = len(text)
        self.start = 0
        self.length = 0

    def solve(self):
        """
        Finds the length of the Longest Palindromic Substring.

        Returns
        -------
        int
            The length of the Longest Palindromic Substring.

        """
        if self.n == 0:
            self.dp = []
            self.start = 0
            self.length = 0
            return 0

        transformed = self._transform()
        self.dp = [0] * len(transformed)
        center = 0
        right_edge = 0

        for index in range(1, len(transformed) - 1):
            mirror = 2 * center - index

            if index < right_edge:
                # The current index is inside the rightmost palindrome:
                #
                #        mirror       center       index       right_edge
                #           v           v            v             v
                #     ... [ . . . . . . . . . . . . . ] ...
                #
                # The mirror radius is known. It is safe to copy only the part
                # that definitely stays inside right_edge; any extra length has
                # to be checked by direct expansion below.
                self.dp[index] = min(
                    right_edge - index,
                    self.dp[mirror],
                )

            # Try to grow the palindrome around index one layer at a time.
            # Sentinels '^' and '$' stop expansion at the boundaries without
            # separate index checks.
            while transformed[index + self.dp[index] + 1] == \
                    transformed[index - self.dp[index] - 1]:
                self.dp[index] += 1

            if index + self.dp[index] > right_edge:
                center = index
                right_edge = index + self.dp[index]

            if self.dp[index] > self.length:
                self.length = self.dp[index]
                self.start = (index - self.dp[index]) // 2

        return self.length

    def get_substring(self):
        """
        Returns one longest palindromic substring.

        Returns
        -------
        str
            One longest palindromic substring.

        """
        if self.dp is None:
            self.solve()
        return self.text[self.start:self.start + self.length]

    def _transform(self):
        """
        Builds the sentinel-separated string used by Manacher's algorithm.

        Returns
        -------
        str
            Transformed string with boundary sentinels and separators.

        """
        return "^#" + "#".join(self.text) + "#$"
