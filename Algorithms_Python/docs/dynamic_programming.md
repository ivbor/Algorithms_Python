<h1>Dynamic Programming Module</h1>
  In this module are outlined solutions to some DP problems utilizing objective-oriented approach.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-DynamicProgrammingProblem'><code>
DynamicProgrammingProblem
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Base class for dynamic programming problems. Other classes in this file    inherit from it. It has a solution() method to actually solve the    problem.
<br></li>
<li> <a href='#class-KnapsackProblem'><code>
KnapsackProblem
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for KnapsackProblem solution.
<br></li>
<li> <a href='#class-LongestCommonSubsequence'><code>
LongestCommonSubsequence
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for searching for LongestCommonSubsequence in the string.
<br></li>
<li> <a href='#class-DamerauLevensteinDistance'><code>
DamerauLevensteinDistance
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for calculating edit distance between strings using    Damerau-Levenstein approach.
<br></li>
<li> <a href='#class-LongestIncreasingSubsequence'><code>
LongestIncreasingSubsequence
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for searching for LongestIncreasingSubsequence in the string.
<br></li>
<li> <a href='#class-maxSubarraySum'><code>
maxSubarraySum
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for finding the maximum sum in the array among provided queries.
<br></li>
<li> <a href='#class-TravellingSalesmanProblem'><code>
TravellingSalesmanProblem
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for solving TSP using weighted_graph and bitmask approach.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-DynamicProgrammingProblem">
<strong>Class</strong>
<code>DynamicProgrammingProblem</code></h1>
Base class for dynamic programming problems.


<h2>Attributes</h2>
<ul>
<li> <strong>dp</strong>: <em>list[Unknown]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Dynamic programming memory. Can be an array of anything or multiple arrays depending on the problem requirements <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Subclasses must implement this method.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the DynamicProgrammingProblem class


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Subclasses must implement this method to solve a specific problem.


<h2>Raises</h2>
<strong>NotImplementedError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised to indicate that this method should be overridden in subclasses. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-KnapsackProblem">
<strong>Class</strong>
<code>KnapsackProblem</code></h1>
Class for solving the Knapsack problem using dynamic programming.

Knapsack problem is an optimization problem. It can be described the
next way. You have a set of items, each with a weight and a value, and you
have a knapsack with a maximum weight capacity. The goal is to determine
the combination of items to include in the knapsack that maximizes the
total value while not exceeding the weight capacity.
Dynamic programming offers an option to solve this problem within O(n*w)
time where n - amount of items, w - knapsack capacity. Since this is
well-known NP-hard problem, usual time to solve is O(2**n).


<h2>Attributes</h2>
<ul>
<li> <strong>weights</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Array of weights for the knapsack problem. <br></li>
<li> <strong>values</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Array of values for the knapsack problem. <br></li>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Capacity of the knapsack. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Solves the Knapsack problem and returns the maximum value.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the KnapsackProblem class


<h2>Parameters</h2>
<ul>
<li> <strong>weights</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Array of weights for the knapsack problem. <br></li>
<li> <strong>values</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Array of values for the knapsack problem. <br></li>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Capacity of the knapsack. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Solves the Knapsack problem using dynamic programming.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum value that can be obtained. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-LongestCommonSubsequence">
<strong>Class</strong>
<code>LongestCommonSubsequence</code></h1>
Class for finding the Longest Common Subsequence (LCS) of two strings.

This problem has a naive solution with time complexity O(2**n) where n is
the length of the longest string. Dynamic programming offers solution
with O(n^2) time complexity, where n and m are the length of strings.


<h2>Attributes</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find LCS for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find LCS for. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the LCS of the two input strings.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the LongestCommonSubsequence class


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find LCS for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find LCS for. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Finds the Longest Common Subsequence (LCS) of two strings.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the LCS. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-DamerauLevensteinDistance">
<strong>Class</strong>
<code>DamerauLevensteinDistance</code></h1>
Class for calculating the Damerau-Levenshtein distance
between two strings using dynamic programming.

Damerau-Levenshtein distance is the option for the edit distance
between two strings. It calculates the difference based on the amount
of 4 operations needed to convert the first string to the second.
These are insertion, deletion, substitution and transposition. It is
important to note that transpositions are made only between adjacent
characters.


<h2>Attributes</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find LCS for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find LCS for. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates the Damerau-Levenshtein distance between the two input
    strings.
<br></li>
<li> <a href='#function-solve_optimized'><code>
solve_optimized(self) -> int
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the DamerauLevensteinDistance class


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find DLD for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find DLD for. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Calculates the Damerau-Levenshtein distance between the two input
strings.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The Damerau-Levenshtein distance. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve_optimized">
<strong>Function</strong>
<code>solve_optimized</code></h1>
Calculates the Damerau-Levenshtein distance between the two input
strings with dynamic programming memory reduced to O(m) instead of
O(m*n), where
m - the length of the longest string,
n - the length of the shortest string.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The Damerau-Levenshtein distance. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-LongestIncreasingSubsequence">
<strong>Class</strong>
<code>LongestIncreasingSubsequence</code></h1>
Class for finding the length of the Longest Increasing Subsequence (LIS)
in a list of numbers using dynamic programming.

This problem has a naive solution with time complexity O(2**n) where n is
the length of the longest string. Dynamic programming offers solution
with O(n^2) time complexity, where n and m are the length of strings.


<h2>Attributes</h2>
<ul>
<li> <strong>nums</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list where LIS will be determined and its length found. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the length of the Longest Increasing Subsequence (LIS).
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the LongestIncreasingSubsequence class


<h2>Parameters</h2>
<ul>
<li> <strong>nums</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list where to find the length of the LIS. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Finds the length of the Longest Increasing Subsequence (LIS)
in the list of numbers.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the Longest Increasing Subsequence. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve_optimized">
<strong>Function</strong>
<code>solve_optimized</code></h1>
Finds the length of the Longest Increasing Subsequence (LIS)
in the list of numbers with time of work reduced from O(n^2) to
O(n*logn) by using binary search.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the Longest Increasing Subsequence. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-maxSubarraySum">
<strong>Class</strong>
<code>maxSubarraySum</code></h1>
This class provides a solution to the Maximum Subarray Sum problem
using Mo's algorithm and dynamic programming. It allows you to find
the maximum sum of a subarray within a given array for multiple
queries.


<h2>Attributes</h2>
<ul>
<li> <strong>arr</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array for which maximum subarray sums will be calculated. <br></li>
<li> <strong>queries</strong>: <em>list[tuple]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of queries, each represented as a tuple (l, r) where l and r are the left and right endpoints of the subarray to consider. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self, arr: list[int]) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Solves the Maximum Subarray Sum problem for each query in the
    sorted order of left endpoints and returns the maximum subarray
    sum for each query using Mo's algorithm.
<br></li>
<li> <a href='#function-solve_optimized'><code>
solve_optimized(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Solves the Maximum Subarray Sum problem for each query in the
    sorted order of left endpoints and returns the maximum subarray
    sum for each query using dynamic programming.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a new maxSubarraySum instance with the provided input
array and a list of queries.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array for which maximum subarray sums will be calculated. <br></li>
<li> <strong>queries</strong>: <em>list[tuple]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of queries, each represented as a tuple (l, r) where l and r are the left and right endpoints of the subarray to consider. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve_optimized">
<strong>Function</strong>
<code>solve_optimized</code></h1>
Solves the Maximum Subarray Sum problem for each query in the sorted
order of left endpoints using dynamic programming. Time complexity
is O(Q), space complexity is O(array length).


<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of maximum subarray sums for each query. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-solve">
<strong>Function</strong>
<code>solve</code></h1>
Solves the Maximum Subarray Sum problem for each query in an
optimized manner using Mo's algorithm.

The time complexity of this method is O(Q * sqrt(N)) for Q queries,
where N is the length of the input array.
This is because, in the worst case, each query requires
O(sqrt(N)) operations to adjust the pointers.
The space complexity of this method is O(1),
since it requires nothing, but 4 pointers and 2 variables for
storing sums.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum subarray sum among queries. <br>

---