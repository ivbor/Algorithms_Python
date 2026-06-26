<h1>Real Binary Search Module</h1>
  This module provides a binary search function for finding an element at a specified index in an array as if it was already sorted in ascending order. The binary search algorithm uses a randomized pivot selection and partitioning to efficiently search for the element.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-split_find'><code>
split_find(a, index)
    Searches for an element with the specified index in an array as if it was
    already sorted in ascending order. It is a wrapper for _split_find
    function.
</code></a> <br> </li>
<li> <a href='#function-split'><code>
split(array, pivot, left_edge, right_edge)
    Splits an array into two parts based on a pivot value. Elements less
    than the pivot are moved to the left subarray, and elements equal to
    or greater than the pivot are moved to the right subarray.
</code></a> <br> </li>
<li> <a href='#function-_split_find'><code>
_split_find(array, left_edge, right_edge, index)
    Recursively finds the element at the specified index inside an array as
    if it were sorted in ascending order. It uses random pivot selection
    and the split function to partition the array while narrowing down
    the search range.
</code></a> <br> </li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-split">
<strong>Function</strong>
<code>split</code></h1>
Splits an array into two parts based on a pivot value.

This function partitions the input array into two subarrays.
Elements less than pivot are moved to the left subarray,
and elements equal to pivot (within a small tolerance)
or greater are moved to the right subarray.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array to be split and partially sorted. <br></li>
<li> <strong>pivot</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The pivot value used for partitioning the array. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index of the subarray to be split. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) of the subarray to be split. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple[int, int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing the new left and right edges of the split subarrays. If all elements are moved to one side, it returns (0, 0). <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_split_find">
<strong>Function</strong>
<code>_split_find</code></h1>
Recursively finds the element at the specified index
inside array as if that array would be sorted in ascending order.

This function recursively searches for the element
at the given index within the subarray defined by left_edge
and right_edge inside array.
It uses random pivot selection and the split function to partition
the array while narrowing down the search range.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array in which to search for the element. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index of the subarray in which to search. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) of the subarray in which to search. <br></li>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The target index of the element to find. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element found at the specified index. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-split_find">
<strong>Function</strong>
<code>split_find</code></h1>
Searches for an element with the specified index in an array
as if it was already sorted in ascending order.

This function searches for the element at the specified index in
ascending order in the input array without fully sorting the array.
It uses the _split_find function to perform the search.
If an array is already sorted this algorithm becomes Binary search.
If not - average and worst cases lead to O(n^2) time complexity
(as if you would have to perform the entire quick sort before search).


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array in which to search for the element. <br></li>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The target index of the element to find. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element found at the specified 'index'. <br>

---