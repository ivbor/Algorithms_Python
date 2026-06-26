<h1>String Algorithms</h1>
  This module contains basic string algorithms.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-is_palindrome_brute_force'><code>
is_palindrome_brute_force(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks whether a string is a palindrome by comparing it with its reverse.
<br></li>
<li> <a href='#function-is_palindrome'><code>
is_palindrome(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks whether a string is a palindrome using two pointers.
<br></li>
<li> <a href='#function-are_anagrams_brute_force'><code>
are_anagrams_brute_force(first: str, second: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks whether two strings are anagrams by repeatedly matching
    characters.
<br></li>
<li> <a href='#function-are_anagrams'><code>
are_anagrams(first: str, second: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks whether two strings are anagrams using character counts.
<br></li>
<li> <a href='#function-find_pattern_brute_force'><code>
find_pattern_brute_force(text: str, pattern: str) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds all pattern occurrences by checking every possible position.
<br></li>
<li> <a href='#function-rabin_karp'><code>
rabin_karp(text: str, pattern: str) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds all pattern occurrences using Rabin-Karp rolling hash.
<br></li>
<li> <a href='#function-prefix_function'><code>
prefix_function(text: str) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates the prefix function for a string.
<br></li>
<li> <a href='#function-z_algorithm'><code>
z_algorithm(text: str) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates Z-values for a string.
<br></li>
<li> <a href='#function-kmp'><code>
kmp(text: str, pattern: str) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds all pattern occurrences using Knuth-Morris-Pratt algorithm.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-is_palindrome_brute_force">
<strong>Function</strong>
<code>is_palindrome_brute_force</code></h1>
Check whether a string is a palindrome by reversing it.

Time complexity: O(n)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String to check. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the string is a palindrome. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-is_palindrome">
<strong>Function</strong>
<code>is_palindrome</code></h1>
Check whether a string is a palindrome using two pointers.

Time complexity: O(n)
Space complexity: O(1)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String to check. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the string is a palindrome. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-are_anagrams_brute_force">
<strong>Function</strong>
<code>are_anagrams_brute_force</code></h1>
Check whether two strings are anagrams using repeated linear search.

Time complexity: O(n ** 2)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>first</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string to compare. <br></li>
<li> <strong>second</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string to compare. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the two strings are anagrams. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-are_anagrams">
<strong>Function</strong>
<code>are_anagrams</code></h1>
Check whether two strings are anagrams using character counts.

Time complexity: O(n)
Space complexity: O(k), where k is the number of distinct characters.


<h2>Parameters</h2>
<ul>
<li> <strong>first</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;First string to compare. <br></li>
<li> <strong>second</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Second string to compare. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the two strings are anagrams. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find_pattern_brute_force">
<strong>Function</strong>
<code>find_pattern_brute_force</code></h1>
Find all pattern occurrences by checking every possible position.

Time complexity: O((n - m + 1) * m), where n is text length and m is
pattern length. In the worst case this is O(n * m).
Space complexity: O(r), where r is the number of returned matches.


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text in which to search. <br></li>
<li> <strong>pattern</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Pattern to search for. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Starting indexes of all pattern occurrences. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-rabin_karp">
<strong>Function</strong>
<code>rabin_karp</code></h1>
Find all pattern occurrences using Rabin-Karp rolling hash.

Time complexity: O(n + m) on average, where n is text length and m is
pattern length. Worst-case time complexity is O(n * m) when many hash
collisions require direct substring checks.
Space complexity: O(r), where r is the number of returned matches.


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text in which to search. <br></li>
<li> <strong>pattern</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Pattern to search for. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Starting indexes of all pattern occurrences. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prefix_function">
<strong>Function</strong>
<code>prefix_function</code></h1>
Calculate the prefix function for a string.

For every position i, the returned value is the length of the longest
proper prefix of text[:i + 1] which is also a suffix of text[:i + 1].

Time complexity: O(n)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String for which the prefix function is calculated. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Prefix-function values for all positions of the string. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-z_algorithm">
<strong>Function</strong>
<code>z_algorithm</code></h1>
Calculate Z-values for a string.

For every position i, the returned value is the length of the longest
substring starting at i which is also a prefix of the whole string.
The first value is set to 0.

Time complexity: O(n)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;String for which Z-values are calculated. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Z-values for all positions of the string. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-kmp">
<strong>Function</strong>
<code>kmp</code></h1>
Find all pattern occurrences using Knuth-Morris-Pratt algorithm.

This implementation uses the prefix function to avoid rechecking
characters after a mismatch.

Time complexity: O(n + m), where n is text length and m is pattern
length.
Space complexity: O(m + r), where r is the number of returned matches.


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text in which to search. <br></li>
<li> <strong>pattern</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Pattern to search for. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Starting indexes of all pattern occurrences. <br>

---