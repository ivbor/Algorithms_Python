"""
Dynamic Programming Module
==========================

In this module are outlined solutions to some DP problems utilizing
objective-oriented approach.

Classes
-------
DynamicProgrammingProblem
    Base class for dynamic programming problems. Other classes in this file
    inherit from it. It has a solution() method to actually solve the
    problem.

KnapsackProblem
    Class for KnapsackProblem solution.

LongestCommonSubsequence
    Class for searching for LongestCommonSubsequence in the string.

LongestPalindromicSubsequence
    Class for finding the LongestPalindromicSubsequence in the string.

DamerauLevensteinDistance
    Class for calculating edit distance between strings using
    Damerau-Levenstein approach.

LongestIncreasingSubsequence
    Class for searching for LongestIncreasingSubsequence in the string.

maxSubarraySum
    Class for finding the maximum sum in the array among provided queries.

TravellingSalesmanProblem
    Class for solving TSP using weighted_graph and bitmask approach.

"""

from Algorithms_Python.weighted_graph import WeightedGraph


class DynamicProgrammingProblem:
    """
    Base class for dynamic programming problems.

    Attributes
    ----------
    dp: list[Unknown]
        Dynamic programming memory. Can be an array of anything or multiple
        arrays depending on the problem requirements

    Methods
    -------
    solve(self) -> None
        Subclasses must implement this method.

    """

    def __init__(self):
        '''
            Creates an instance of the DynamicProgrammingProblem class

            Returns
            -------
            None
        '''
        self.dp = None

    def solve(self):
        """
        Subclasses must implement this method to solve a specific problem.

        Raises
        ------
        NotImplementedError
            Raised to indicate that this method should be overridden in
            subclasses.

        """
        raise NotImplementedError("Subclasses must implement the solve method")


class KnapsackProblem(DynamicProgrammingProblem):
    """
    Class for solving the Knapsack problem using dynamic programming.

    Knapsack problem is an optimization problem. It can be described the
    next way. You have a set of items, each with a weight and a value, and you
    have a knapsack with a maximum weight capacity. The goal is to determine
    the combination of items to include in the knapsack that maximizes the
    total value while not exceeding the weight capacity.
    Dynamic programming offers an option to solve this problem within O(n*w)
    time where n - amount of items, w - knapsack capacity. Since this is
    well-known NP-hard problem, usual time to solve is O(2**n).

    Attributes
    ----------
    weights: list[int]
        Array of weights for the knapsack problem.

    values: list[int]
        Array of values for the knapsack problem.

    capacity: int
        Capacity of the knapsack.


    Methods
    -------
    solve(self) -> int
        Solves the Knapsack problem and returns the maximum value.

    """

    def __init__(self, weights, values, capacity):
        '''
            Creates an instance of the KnapsackProblem class

            Parameters
            ----------
            weights: list[int]
                Array of weights for the knapsack problem.

            values: list[int]
                Array of values for the knapsack problem.

            capacity: int
                Capacity of the knapsack.

            Returns
            -------
            None
        '''
        super().__init__()
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(weights)

    def solve(self):
        """
        Solves the Knapsack problem using dynamic programming.

        Returns
        -------
        int
            The maximum value that can be obtained.

        """

        # dynamic programming table for this problem includes
        # amount of rows equal to the amount of items and
        # amount of columns equal to the capacity
        # for capacity == 0 there are no items we can place
        self.dp = [[0] * (self.capacity + 1)
                   for _ in range(self.num_items + 1)]

        # start to fill the table
        for i in range(1, self.num_items + 1):
            for w in range(1, self.capacity + 1):

                # check if weight of i-1 item can fit inside
                # current capacity which is w
                if self.weights[i - 1] <= w:
                    self.dp[i][w] = max(
                        self.dp[i - 1][w],
                        self.dp[i - 1][w - self.weights[i - 1]] +
                        self.values[i - 1])
                else:
                    self.dp[i][w] = self.dp[i - 1][w]

        return self.dp[self.num_items][self.capacity]


class LongestCommonSubsequence(DynamicProgrammingProblem):
    """
    Class for finding the Longest Common Subsequence (LCS) of two strings.

    This problem has a naive solution with time complexity O(2**n) where n is
    the length of the longest string. Dynamic programming offers solution
    with O(n^2) time complexity, where n and m are the length of strings.

    Attributes
    ----------
    str1: str
        First string of the two to find LCS for.

    str2: str
        Second string of the two to find LCS for.

    Methods
    -------
    solve(self) -> int
        Finds the LCS of the two input strings.

    """

    def __init__(self, str1, str2):
        '''
            Creates an instance of the LongestCommonSubsequence class

            Parameters
            ----------
            str1: str
                First string of the two to find LCS for.

            str2: str
                Second string of the two to find LCS for.

            Returns
            -------
            None
        '''
        super().__init__()
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)

    def solve(self):
        """
        Finds the Longest Common Subsequence (LCS) of two strings.

        Returns
        -------
        int
            The length of the LCS.

        """
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.dp[i][j] = self.dp[i - 1][j - 1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])
        return self.dp[self.m][self.n]


class LongestPalindromicSubsequence(DynamicProgrammingProblem):
    """
    Class for finding the Longest Palindromic Subsequence (LPS).

    A subsequence keeps the original order of characters, but it may skip
    characters. That is why this problem is different from the longest
    palindromic substring problem, where the chosen characters must be
    contiguous.

    Dynamic programming works by solving every interval text[left:right + 1].
    If both ends are equal, they can be wrapped around the best answer inside
    the interval. Otherwise one of the ends must be skipped.

    Attributes
    ----------
    text: str
        String where LPS will be determined and its length found.

    Methods
    -------
    solve(self) -> int
        Finds the length of the Longest Palindromic Subsequence.

    """

    def __init__(self, text):
        '''
            Creates an instance of the LongestPalindromicSubsequence class

            Parameters
            ----------
            text: str
                String where to find the length of the LPS.

            Returns
            -------
            None
        '''
        super().__init__()
        self.text = text
        self.n = len(text)

    def solve(self):
        """
        Finds the length of the Longest Palindromic Subsequence (LPS).

        Returns
        -------
        int
            The length of the Longest Palindromic Subsequence.

        """
        if self.n == 0:
            self.dp = []
            return 0

        # dp[left][right] stores the LPS length inside the closed interval:
        #
        #     text:  b b b a b
        #            ^     ^
        #          left   right
        #
        # Every one-character interval is already a palindrome of length 1.
        self.dp = [[0] * self.n for _ in range(self.n)]
        for index in range(self.n):
            self.dp[index][index] = 1

        # Shorter intervals must be solved before longer intervals because
        # dp[left][right] depends on:
        #
        #   dp[left + 1][right - 1]  when both ends are used,
        #   dp[left + 1][right]      when the left end is skipped,
        #   dp[left][right - 1]      when the right end is skipped.
        for interval_length in range(2, self.n + 1):
            for left in range(self.n - interval_length + 1):
                right = left + interval_length - 1

                if self.text[left] == self.text[right]:
                    # Matching ends can sit at the two ends of a palindrome.
                    # For a two-character interval the inside length is zero;
                    # otherwise reuse the already solved inner interval.
                    inside = 0
                    if interval_length > 2:
                        inside = self.dp[left + 1][right - 1]
                    self.dp[left][right] = inside + 2
                else:
                    # If the ends do not match, no optimal palindrome can use
                    # both ends together. Try dropping either side and keep the
                    # better interval.
                    self.dp[left][right] = max(
                        self.dp[left + 1][right],
                        self.dp[left][right - 1],
                    )

        return self.dp[0][self.n - 1]


class DamerauLevensteinDistance(DynamicProgrammingProblem):
    """
    Class for calculating the Damerau-Levenshtein distance
    between two strings using dynamic programming.

    Damerau-Levenshtein distance is the option for the edit distance
    between two strings. It calculates the difference based on the amount
    of 4 operations needed to convert the first string to the second.
    These are insertion, deletion, substitution and transposition. It is
    important to note that transpositions are made only between adjacent
    characters.

    Attributes
    ----------
    str1: str
        First string of the two to find LCS for.

    str2: str
        Second string of the two to find LCS for.

    Methods
    -------
    solve(self) -> int
        Calculates the Damerau-Levenshtein distance between the two input
        strings.

    solve_optimized(self) -> int


    """

    def __init__(self, str1, str2):
        '''
            Creates an instance of the DamerauLevensteinDistance class

            Parameters
            ----------
            str1: str
                First string of the two to find DLD for.

            str2: str
                Second string of the two to find DLD for.

            Returns
            -------
            None
        '''
        super().__init__()
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)

    def solve(self):
        """
        Calculates the Damerau-Levenshtein distance between the two input
        strings.

        Returns
        -------
        int
            The Damerau-Levenshtein distance.

        """
        self.dp = [[0] * (self.n + 1)
                   for _ in range(self.m + 1)]
        for i in range(self.m + 1):
            self.dp[i][0] = i
        for j in range(self.n + 1):
            self.dp[0][j] = j

        for i in range(self.m):
            for j in range(self.n):
                cost = 0 \
                    if self.str1[i] == self.str2[j] else 1
                self.dp[i + 1][j + 1] = min(
                    self.dp[i][j + 1] + 1,  # Deletion
                    self.dp[i + 1][j] + 1,  # Insertion
                    self.dp[i][j] + cost  # Substitution
                )
                if (i >= 1 and j >= 1
                        and self.str1[j] == self.str2[i - 1]) \
                        and (self.str1[j - 1] == self.str2[i]):
                    self.dp[i + 1][j + 1] = min(
                        self.dp[i + 1][j + 1],
                        self.dp[i - 1][j - 1] + 1)  # Transposition
                # if (i > 1 and j > 1
                #         and self.str1[j] == self.str2[i - 2]) \
                #         and (self.str1[j - 2] == self.str2[i]):
                #     self.dp[i + 1][j + 1] = min(
                #         self.dp[i + 1][j + 1],
                #         self.dp[i - 1][j - 1] + 1)  # Transposition
        return self.dp[self.m][self.n]

    def solve_optimized(self):
        """
        Calculates the Damerau-Levenshtein distance between the two input
        strings with dynamic programming memory reduced to O(m) instead of
        O(m*n), where
        m - the length of the longest string,
        n - the length of the shortest string.

        Returns
        -------
        int
            The Damerau-Levenshtein distance.

        """
        len1, len2 = len(self.str1), len(self.str2)

        # Ensure str1 is the shorter string
        if len1 > len2:
            self.str1, self.str2, len1, len2 = \
                self.str2, self.str1, len2, len1

        # Initialize a 3*m array to store the current, previous and
        # preprevious rows
        self.dp = [[0] * (len1 + 1) for _ in range(3)]

        # Initialize the first row
        for i in range(len1 + 1):
            self.dp[0][i] = i

        current_row = 0
        next_row = 1
        for i in range(len2):

            # Update the first element in the current row
            self.dp[current_row][0] = i
            self.dp[next_row][0] = i + 1

            for j in range(len1):
                cost = \
                    0 if self.str1[j] == self.str2[i] else 1

                # fix current_row + 1
                insert_cost = self.dp[next_row][j] + 1
                delete_cost = self.dp[current_row][j + 1] + 1
                replace_cost = self.dp[current_row][j] + cost

                self.dp[next_row][j + 1] = \
                    min(insert_cost, delete_cost, replace_cost)
                if (i >= 1 and j >= 1
                    and self.str1[j] == self.str2[i - 1]
                        and self.str1[j - 1] == self.str2[i]):
                    self.dp[next_row][j + 1] = \
                        min(self.dp[next_row][j + 1],
                            self.dp[current_row - 1][j - 1] + 1)
                # if (i > 1 and j > 1
                #         and self.str1[j] == self.str2[i - 2]) \
                #         and (self.str1[j - 2] == self.str2[i]):
                #     self.dp[next_row][j + 1] = \
                #         min(self.dp[next_row][j + 1],
                #             self.dp[current_row - 1][j - 1] + 1)

            # Go to the next row inside the table
            current_row = 1 + current_row if current_row < 2 else 0
            next_row = current_row + 1 if current_row < 2 else 0

        return self.dp[current_row][len1]


class LongestIncreasingSubsequence(DynamicProgrammingProblem):
    """
    Class for finding the length of the Longest Increasing Subsequence (LIS)
    in a list of numbers using dynamic programming.

    This problem has a naive solution with time complexity O(2**n) where n is
    the length of the longest string. Dynamic programming offers solution
    with O(n^2) time complexity, where n and m are the length of strings.

    Attributes
    ----------
    nums: list[float]
        The list where LIS will be determined and its length found.

    Methods
    -------
    solve(self) -> int
        Finds the length of the Longest Increasing Subsequence (LIS).

    """

    def __init__(self, nums):
        '''
            Creates an instance of the LongestIncreasingSubsequence class

            Parameters
            ----------
            nums: list[float]
                The list where to find the length of the LIS.

            Returns
            -------
            None
        '''
        super().__init__()
        self.nums = nums

    def solve(self):
        """
        Finds the length of the Longest Increasing Subsequence (LIS)
        in the list of numbers.

        Returns
        -------
        int
            The length of the Longest Increasing Subsequence.

        """
        if not self.nums:
            return 0

        n = len(self.nums)
        # Initialize the LIS array with a length of 1 for each element
        self.dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if self.nums[i] > self.nums[j]:
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)

        return max(self.dp)

    def solve_optimized(self):
        """
        Finds the length of the Longest Increasing Subsequence (LIS)
        in the list of numbers with time of work reduced from O(n^2) to
        O(n*logn) by using binary search.

        Returns
        -------
        int
            The length of the Longest Increasing Subsequence.

        """
        if not self.nums:
            return 0

        n = len(self.nums)

        # using dp for representing the smallest tail of all
        # increasing subsequences of length i
        self.dp = [0] * n
        self.dp[0] = self.nums[0]

        # Initialize the length of the LIS to 1
        length = 1

        for i in range(1, n):
            if self.nums[i] < self.dp[0]:
                self.dp[0] = self.nums[i]
            elif self.nums[i] > self.dp[length - 1]:
                self.dp[length] = self.nums[i]
                length += 1
            else:

                # Find the position of the smallest element in tails
                # that is greater than or equal to nums[i]
                # using binary search
                left, right = 0, length - 1
                while left < right:
                    mid = (left + right) // 2
                    if self.dp[mid] < self.nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                self.dp[left] = self.nums[i]
        return length


class maxSubarraySum(DynamicProgrammingProblem):
    '''
        This class provides a solution to the Maximum Subarray Sum problem
        using Mo's algorithm and dynamic programming. It allows you to find
        the maximum sum of a subarray within a given array for multiple
        queries.

        Attributes
        ----------
        arr : list[int]
            The input array for which maximum subarray sums will be
            calculated.

        queries : list[tuple]
            A list of queries, each represented as a tuple (l, r) where
            l and r are the left and right endpoints of the subarray to
            consider.

        Methods
        -------
        solve(self, arr: list[int]) -> int
            Solves the Maximum Subarray Sum problem for each query in the
            sorted order of left endpoints and returns the maximum subarray
            sum for each query using Mo's algorithm.

        solve_optimized(self) -> int
            Solves the Maximum Subarray Sum problem for each query in the
            sorted order of left endpoints and returns the maximum subarray
            sum for each query using dynamic programming.
    '''

    def __init__(self, arr, queries):
        """
        Initializes a new maxSubarraySum instance with the provided input
        array and a list of queries.

        Parameters
        ----------
        arr : list[int]
            The input array for which maximum subarray sums will be
            calculated.

        queries : list[tuple]
            A list of queries, each represented as a tuple (l, r) where l
            and r are the left and right endpoints of the subarray to
            consider.

        Returns
        -------
        None
        """

        super().__init__()

        # In the dp prefixSum is stored
        self.dp = [0]
        for i in range(len(arr)):
            self.dp.append(self.dp[-1] + arr[i])
        self.queries = queries

    def solve_optimized(self):
        """
        Solves the Maximum Subarray Sum problem for each query in the sorted
        order of left endpoints using dynamic programming. Time complexity
        is O(Q), space complexity is O(array length).

        Returns
        -------
        list[int]
            A list of maximum subarray sums for each query.

        """

        maxSum = float('-inf')

        # Sort queries based on their left endpoints
        sortedQueries = sorted(self.queries, key=lambda x: x[0])

        for query in sortedQueries:

            l, r = query

            currentSum = self.dp[r + 1] - self.dp[l]

            maxSum = max(maxSum, currentSum)

        return maxSum

    def solve(self, arr):
        """
        Solves the Maximum Subarray Sum problem for each query in an
        optimized manner using Mo's algorithm.

        The time complexity of this method is O(Q * sqrt(N)) for Q queries,
        where N is the length of the input array.
        This is because, in the worst case, each query requires
        O(sqrt(N)) operations to adjust the pointers.
        The space complexity of this method is O(1),
        since it requires nothing, but 4 pointers and 2 variables for
        storing sums.

        Returns
        -------
        int
            The maximum subarray sum among queries.
        """
        maxSum = float('-inf')
        left = 0
        right = 0
        currentSum = 0

        for query in self.queries:
            l, r = query
            r += 1

            # Adjust the pointers to the range of the query
            while right < r:
                currentSum += arr[right]
                right += 1

            while right > r:
                right -= 1
                currentSum -= arr[right]

            while left < l:
                currentSum -= arr[left]
                left += 1

            while left > l:
                left -= 1
                currentSum += arr[left]

            maxSum = max(maxSum, currentSum)

        return maxSum


class TravellingSalesmanProblem(DynamicProgrammingProblem):

    def __init__(self, cities, edges):
        super().__init__()

        # Make a graph to store the cities and distances between them
        self.graph = WeightedGraph()
        self.n = len(cities)
        for city in cities:
            self.graph.add_vertex(data=city)
        for u, v, weight in edges:
            self.graph.add_edge(u, v, weight=weight)

        # Initialize dp to store a minimum distance to visit the subset
        # of cities represented by using bitmask, where the bit at
        # position i is 1 if the city has been visited and 0 otherwise,
        # and ending in the city i (dp[mask][i], mask = 1 << i)
        self.dp = [[float('inf')] * self.n
                   for _ in range(1 << self.n)]
        self.dp[1][0] = 0

    def solve(self):
        for mask in range(1, 1 << self.n):
            for last in range(self.n):
                # check if `last` city is the last in the mask
                # if it is not - there is no point in this iteration
                # and we are skipping it
                if mask & (1 << last):
                    # get the subset of the cities before the last
                    prev_mask = mask ^ (1 << last)
                    # iterate through the subset of predecessors
                    for k in range(self.n):
                        # if city `k` gets to be visited in this subset -
                        # add its weight to the appropriate dp cell
                        if prev_mask & (1 << k) and \
                                last in self.graph.vertices[k].edges.keys():
                            weight = self.graph.vertices[k]\
                                .edges[last].weight
                            self.dp[mask][last] = \
                                min(self.dp[mask][last],
                                    self.dp[prev_mask][k] + weight)
        min_cost = float('inf')
        for j in range(1, self.n):
            if 0 in self.graph.vertices[j].edges.keys():
                return_path_weight = \
                    self.graph.vertices[j].edges[0].weight
                min_cost = min(min_cost,
                               self.dp[(1 << self.n) - 1][j] +
                               return_path_weight)
        return min_cost
