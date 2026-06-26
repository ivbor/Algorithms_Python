<h1>Edit Distance Calculation Module</h1>
  This module provides functions to calculate the edit distance between two strings using different distance metrics. It includes functions for Hamming distance, Jaro similarity, and uses the Longest Common Subsequence and Damerau-Levenshtein distance algorithms for more complex edit distance calculations.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-edit_distance'><code>
edit_distance(str1: str, str2: str, distance: str = 'dl') -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Compute the edit distance between two strings using a specified distance
    metric.
<br></li>
<li> <a href='#function-hamming_distance'><code>
hamming_distance(str1: str, str2: str) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate the Hamming distance between two strings.
<br></li>
<li> <a href='#function-jaro_distance'><code>
jaro_distance(str1: str, str2: str) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate the Jaro similarity between two strings.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-edit_distance">
<strong>Function</strong>
<code>edit_distance</code></h1>
Compute the edit distance between two strings.

This function calculates the edit distance between two input strings
using one of the available distance metrics. You can choose the
following metrics: Jaro, Hamming, LongestCommonSubsequence or
DamerauLevensteinDistance.

DamerauLevensteinDistance is the most universal of them.
Jaro distance can be the metric for the distance between the strings
containing matching and transposing characters.
LongestCommonSubsequence distance is a metric for edit distance, using
the length of LCS of the strings.
Hamming distance works only for the strings with the same length and
share a large share of characters (including their positions), e.g.
'karoline' and 'kathrine'.


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first input string. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The second input string. <br></li>
<li> <strong>distance</strong>: <em>str, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The distance metric to use. Possible values are 'jaro' for Jaro distance, 'hamming' for Hammimg distance, 'lcs' for distance based on the LongestCommonSubsequence or 'dl' for DamerauLevensteinDistance. Default is 'dl'. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The computed edit distance based on the selected distance metric.   <br>
<h2>Raises</h2>
<strong>ValueError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the distance is 'hamming' and the input strings have different lengths. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-hamming_distance">
<strong>Function</strong>
<code>hamming_distance</code></h1>
Calculate the Hamming distance between two strings.

The Hamming distance is the number of positions at which the
corresponding elements in the input strings of the same length are
different.


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first input string. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The second input string. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The Hamming distance between the two input strings.   <br>
<h2>Raises</h2>
<strong>ValueError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the input strings have different lengths. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-jaro_distance">
<strong>Function</strong>
<code>jaro_distance</code></h1>
Calculate the Jaro similarity between two strings.

The Jaro similarity measures the similarity between two strings.
A higher value indicates more similarity between the strings.
The general formula looks the following way:
d = (matches / length1 + matches / length2 + (matches - transpositions)
/ matches) / 3, where
matches are matches of the characters in the strings if they are not
not farther than int(max(length1, length2) / 2) - 1 characters apart,
length1 and length2 are lengths of the first and the second strings
accordingly,
transpositions is the number of matching characters that are not in the
right order.


<h2>Parameters</h2>
<ul>
<li> <strong>str1</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first input string. <br></li>
<li> <strong>str2</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The second input string. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The Jaro similarity between the two input strings. <br>

---