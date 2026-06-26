<h1>Quick Sort Module</h1>
  This module provides Quick Sort implementations for efficiently sorting a list of elements. Quick Sort is a divide-and-conquer algorithm that selects a pivot value, divides the input array, and sorts the resulting parts.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-quick_sort'><code>
quick_sort(array: list[float], pivot_str: str = 'random') -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts a list of elements using the Quick Sort algorithm.
<br></li>
<li> <a href='#function-split'><code>
split(a: list[float], pivot: float, left_edge: int, right_edge: int) ->
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    tuple
    Divides the input array into two parts relative to the pivot value.
<br></li>
<li> <a href='#function-avg'><code>
avg(a: list[float], left_edge: int, right_edge: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates the average value of elements in a specified range.
<br></li>
<li> <a href='#function-clst_avg'><code>
clst_avg(a: list[float], avg: float, left_edge: int, right_edge: int) ->
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    float
    Finds the element closest to the average value in a specified range.
<br></li>
<li> <a href='#function-_quick_sort'><code>
_quick_sort(array: list[float], left_edge: int, right_edge: int,
 pivot_str: str = 'random') -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs the Quick Sort algorithm on a given array within specified
    indices.
<br></li>
<li> <a href='#function-median_of_medians'><code>
median_of_medians(array: list[float], left: int, right: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the index of median of medians for a given array within specified
    indices.
<br></li>
<li> <a href='#function-partition_small'><code>
partition_small(array: list[float], left: int, right: int, opt: bool = True)
 -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts a small portion of the array using a bubble sort to find a
    median inside this array portion.
    Optimised version (opt=True) calls Insertion Sort for small arrays.
<br></li>
<li> <a href='#function-median_of_three'><code>
median_of_three(array: list[float], left: int, right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the median of three elements in a given array within specified
    indices.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-split">
<strong>Function</strong>
<code>split</code></h1>
Split Function

Divide the input array  into two parts relative to the pivot value.
Elements less than pivot are moved to the left,
and elements greater or equal are moved to the right.


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be split. <br></li>
<li> <strong>pivot</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The pivot value used for splitting the array. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the split operation. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the split operation. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing two indices that represent the new boundaries for the split parts. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-clst_avg">
<strong>Function</strong>
<code>clst_avg</code></h1>
Calculate the average value of elements in a specified range.


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the range. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the range. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The average value of elements in the specified range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-partition_small">
<strong>Function</strong>
<code>partition_small</code></h1>
Partition a small portion of the array using a bubble sort algorithm.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array. <br></li>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the range. <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the range. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index representing the partitioned element. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-median_of_medians">
<strong>Function</strong>
<code>median_of_medians</code></h1>
Find the median of medians for a given array within specified indices.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array. <br></li>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the range. <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the range. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The median of medians. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-median_of_three">
<strong>Function</strong>
<code>median_of_three</code></h1>
Find the median of three elements in a given array within specified
indices.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array. <br></li>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the range. <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the range. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The median of three elements. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_quick_sort">
<strong>Function</strong>
<code>_quick_sort</code></h1>
Quick Sort Function

Sort the input array using the Quick Sort algorithm. This function
performs a divide-and-conquer approach by selecting a pivot value and
splitting the array into two parts: elements less than the pivot and
elements greater or equal to the pivot.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting index for the sort operation. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The ending index (exclusive) for the sort operation. <br></li>
<li> <strong>pivot_str</strong>: <em>'random', 'clst_avg', 'm3' or 'mm'</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A strategy to choose pivot element. 'random' for random selection among the elements, works well for random or uniformly distributed data. 'clst_avg' for selection of element close to the average of the array,  works well for data with known distribution. 'm3' or median of three provides some resistance against worst cases, works well on data with some outliers or some degree of ordering but not fully sorted. 'mm' of median of medians or introselect performs well consistently regardless of the input data <br></li>
<li> <strong>no_recursion</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Switcher between recursive and non-recursive algorithms. <br></li>
</ul>
<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The sorted array. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-quick_sort">
<strong>Function</strong>
<code>quick_sort</code></h1>
Quick Sort Function (Wrapper)

Sort the input list using the Quick Sort algorithm. This function is a
wrapper for the `_quick_sort` function and sets initial values for the
sorting process. A wide selection of pivot strategies is available.
Average and worst space complexities:
- random: O(log n), O(n)
- closest to the average: O(log n), O(n)
- median of three: O(log n), O(log n)
- median of medians: O(log n), O(log n)
Average and worst time complexities:
- random: O(n * log n), O(n ** 2)
- closest to the average: O(n * log n), O(n * log n)
- median of three: O(n * log n), O(n * log n)
- median of medians: O(n * log n), O(n * log n)
Important considerations:
O(n ** 2) performance is so extremely rare, it has no implications in
practical usage. Median of medians pivot calculation suffers from
big constant factor, which makes it impractical for small arrays.
It is worth noting that quick sort is unstable.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
<li> <strong>pivot_str</strong>: <em>'random', 'clst_avg', 'm3' or 'mm'</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A strategy to choose pivot element. 'random' for random selection among the elements, works well for random or uniformly distributed data. 'clst_avg' for selection of element close to the average of the array, works well for data with known distribution. 'm3' or median of three provides some resistance against worst cases, works well on data with some outliers or some degree of ordering but not fully sorted. 'mm' of median of medians or introselect performs well consistently regardless of the input data. <br></li>
<li> <strong>no_recursion</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Switcher between recursive and non-recursive algorithms. <br></li>
</ul>
<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The sorted list. <br>

---