<h1>Merge Sort Module</h1>
  A module containing Merge Sort algorithms and a helper function for merging arrays. This module specializes in various implementations of the Merge Sort algorithm and a helper function for merging two sorted arrays into a single sorted array.  
<h2>Constants</h2>
<ul>
<li> <strong>MERGE_OPT</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Determines whether the merge sort will utilize insertion sort at all or not. Assumes a value automatically based on whether it is possible to import insertion sort function. <br></li>
<li> <strong>MAX_DEPTH</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Recursion control constant. Determines the depth after which parallel merge sort implementation will not call recursion any longer. Default is set to cpu_count. <br></li>
</ul>
<h2>Functions</h2>
<ul>
<li> <a href='#function-merge'><code>
merge(array: list[float], part_one: list[float], part_two: list[float])
 -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Merge two sorted arrays into a single sorted array.
<br></li>
<li> <a href='#function-merge_sort'><code>
merge_sort(array: list[float], opt: bool = True, batch_size: int = 3)
 -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sort a list of elements using the Merge Sort algorithm.
    Optimised version (opt=True) calls Insertion Sort for small arrays.
<br></li>
<li> <a href='#function-merge_sort_parallel'><code>
merge_sort_parallel(array: list[float], batch_size=None, depth=0)
 -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sort a list of elements with multiprocessing using the Merge Sort
    algorithm.
<br></li>
<li> <a href='#function-parallel_merge_sort'><code>
parallel_merge_sort(arr: list[float], batch_size=None, depth=0)
 -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Function-helper for merge_sort_parallel which handles recursion
    and multiprocessing.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-merge">
<strong>Function</strong>
<code>merge</code></h1>
Merge Two Sorted Arrays

This function merges two sorted arrays, `part_one` and `part_two`, into
a single sorted array. This is a helper for the Merge Sort function.
Both space and time complexities are O(n), where n - the number of
elements inside two arrays combined.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The resulting array <br></li>
<li> <strong>part_one</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first sorted array to be merged. <br></li>
<li> <strong>part_two</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The second sorted array to be merged. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-merge_sort">
<strong>Function</strong>
<code>merge_sort</code></h1>
Merge Sort

This function implements the Merge Sort algorithm
to sort a list of elements.

The Merge Sort algorithm works by dividing the input list into
two halves, recursively sorting each half, and then merging the
two sorted halves into one sorted list.
Time Complexity is O(n*log(n)), space complexity - O(n).
Space is used for storing divided subarrays during sorting.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
<li> <strong>opt</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A switch between faster version using Insertion Sort on small arrays and slower version without it. Default is True. <br></li>
<li> <strong>batch_size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A threshold for switching between further dividing the input and binary search optimized insertion sort, if opt is True. Default, tuned for the best performance, value is 3. <br></li>
</ul>
<h2>Returns</h2>
<em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A new list containing the elements of the input list in sorted order. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-merge_sort_parallel">
<strong>Function</strong>
<code>merge_sort_parallel</code></h1>
Parallel Merge Sort using dynamic ThreadPoolExecutor

This function implements the Merge Sort algorithm in parallel
to sort a list of elements.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input list to be sorted. <br></li>
<li> <strong>batch_size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A threshold to switch from parallel algorithm to the usual one once the part to be sorted will become as small as a batch_size. Default is None, which would later translate to (len(array) // 100) + 1 <br></li>
<li> <strong>depth</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Recursion depth control parameter, used for avoiding overheading. Default is 4. If set to None will translate to the number of cores. <br></li>
</ul>
<h2>Returns</h2>
<em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A new list containing the elements of the input list in sorted order. <br>

---