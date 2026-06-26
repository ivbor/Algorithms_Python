<h1>Insertion Sort</h1>
  A module with Insertion Sort algorithm to sort a list of elements. Insertion Sort is a simple sorting algorithm that works by iterating through the input list and, for each element, comparing it with the elements to its left and inserting it into its correct position within the already sorted portion of the list. This process continues until the entire list is sorted.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-insert_sort'><code>
insert_sort(array: list[float]) -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts a list of elements using the Insertion Sort algorithm.
<br></li>
<li> <a href='#function-bin_search_fl'><code>
bin_search_fl(array: list[float], value: float, start: int, end: int) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    A binary search in the array slice consisting of floats.
<br></li>
<li> <a href='#function-insert_sort_opt'><code>
insert_sort_opt(array: list[float]) -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts a list of elements using the optimized Insertion Sort algorithm.
    This version uses binary search to find the correct position for each
    element, reducing the number of comparisons and improving efficiency.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert_sort">
<strong>Function</strong>
<code>insert_sort</code></h1>
This function implements the Insertion Sort algorithm
to sort a list of elements in-place.

The Insertion Sort algorithm works by iterating through the input list,
and for each element, it compares it with the elements
to its left and inserts it into its correct position within
the already sorted portion of the list.
This process continues until the entire list is sorted.
Worst and average cases time complexity - O(n^2).
Space complexity - O(1) as sorting is done in-place.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
</ul>
<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list containing the elements of the input list in sorted order. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bin_search_fl">
<strong>Function</strong>
<code>bin_search_fl</code></h1>
A binary search in the array slice consisting of floats.

It searches for the place where to put the value
while preserving an ascending order.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An array to search in. <br></li>
<li> <strong>value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A value to search a place for. <br></li>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An index pointing at the slice's left border inclusively. <br></li>
<li> <strong>end</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An index pointing at the slice's right border inclusively. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An index pointing to the place where the value should land. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert_sort_opt">
<strong>Function</strong>
<code>insert_sort_opt</code></h1>
This function implements the in-place Insertion sort algorithm
enhanced by binary search.

Sorts a list of elements using the optimized Insertion Sort algorithm.
This version uses binary search to find the correct position for each
element, reducing the number of comparisons and improving efficiency.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
</ul>
<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list containing the elements of the input list in sorted order. <br>

---