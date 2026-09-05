<h1>Dynamic Programming Substring Algorithms</h1>
  This module contains substring-oriented dynamic programming problems and closely related substring algorithms.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-LongestCommonSubstring'><code>
LongestCommonSubstring
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for finding the LongestCommonSubstring of two strings.
<br></li>
<li> <a href='#class-LongestPalindromicSubstring'><code>
LongestPalindromicSubstring
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for finding the LongestPalindromicSubstring using dynamic    programming.
<br></li>
<li> <a href='#class-ManacherLongestPalindromicSubstring'><code>
ManacherLongestPalindromicSubstring
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Class for finding the LongestPalindromicSubstring using Manacher's    algorithm.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-LongestCommonSubstring">
<strong>Class</strong>
<code>LongestCommonSubstring</code></h1>
Class for finding the Longest Common Substring of two strings.

A substring is contiguous. This is the important difference from
LongestCommonSubsequence: after a mismatch the current common suffix must
reset to zero instead of carrying the best value from the left or top
table cell.


<h2>Attributes</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find the substring for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find the substring for. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the length of the Longest Common Substring.
<br></li>
<li> <a href='#function-get_substring'><code>
get_substring(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns one longest common substring.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the LongestCommonSubstring class


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string of the two to find the substring for. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string of the two to find the substring for. <br></li>
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
Finds the length of the Longest Common Substring.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the Longest Common Substring. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_substring">
<strong>Function</strong>
<code>get_substring</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- str One longest common substring. If there is no common substring, returns an empty string. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-LongestPalindromicSubstring">
<strong>Class</strong>
<code>LongestPalindromicSubstring</code></h1>
Class for finding the Longest Palindromic Substring using DP.

The dynamic programming table stores whether every closed interval
text[left:right + 1] is a palindrome. This gives O(n^2) time and O(n^2)
memory. Manacher's algorithm below solves the same task in O(n), but this
version is useful for learning the recurrence directly.


<h2>Attributes</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String where the longest palindromic substring is searched. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the length of the Longest Palindromic Substring.
<br></li>
<li> <a href='#function-get_substring'><code>
get_substring(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns one longest palindromic substring.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the LongestPalindromicSubstring class


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String where the longest palindromic substring is searched. <br></li>
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
Finds the length of the Longest Palindromic Substring.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the Longest Palindromic Substring. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_substring">
<strong>Function</strong>
<code>get_substring</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- str One longest palindromic substring. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-ManacherLongestPalindromicSubstring">
<strong>Class</strong>
<code>ManacherLongestPalindromicSubstring</code></h1>
Class for finding the Longest Palindromic Substring using Manacher.

Manacher's algorithm keeps palindrome radii around every possible center.
To avoid separate odd-length and even-length logic, the input is
transformed by inserting separators:

    text:        a b b a
    transformed: ^ # a # b # b # a # $

Every palindrome in the transformed string has an odd number of
characters, so a single expansion rule handles both original cases.


<h2>Attributes</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String where the longest palindromic substring is searched. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-solve'><code>
solve(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the length of the Longest Palindromic Substring.
<br></li>
<li> <a href='#function-get_substring'><code>
get_substring(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns one longest palindromic substring.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of the ManacherLongestPalindromicSubstring
class


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String where the longest palindromic substring is searched. <br></li>
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
Finds the length of the Longest Palindromic Substring.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of the Longest Palindromic Substring. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_substring">
<strong>Function</strong>
<code>get_substring</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- str One longest palindromic substring. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_transform">
<strong>Function</strong>
<code>_transform</code></h1>
Builds the sentinel-separated string used by Manacher's algorithm.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Transformed string with boundary sentinels and separators. <br>

---