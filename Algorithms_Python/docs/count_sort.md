<h1>Counting Sort Module</h1>
  This module provides an implementation of the counting sort algorithm for sorting an array of whole numbers.  The counting sort algorithm counts the occurrences of each whole number in the input array and uses this information to create a sorted array. It is particularly efficient when the range of values is small compared to the array size.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-count_sort'><code>
count_sort(array: list[int]) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts an array of whole numbers using the counting sort algorithm.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-count_sort">
<strong>Function</strong>
<code>count_sort</code></h1>
This function implements counting sort on the array of whole numbers.

The algorithm of counting sort employs the basic counting
of the whole numbers inside array. It creates another array with
(max - min + 1) size, and counts, how many elements with each number
are inside the array to be sorted.
Time to work: O(size of array + difference between the biggest and
the smallest elements)


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;array to be sorted consisting of whole numbers <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;sorted array <br>

---