<h1>Binary Search Module</h1>
  This module provides implementations of binary search algorithms for searching a value within a sorted one-dimensional array of whole numbers. Two implementations are available: one with recursion and another without recursion. The choice between the two depends on your requirements for space efficiency and time complexity.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-bin_search'><code>
bin_search(array: list[int], value_to_search: int, no_recursion=False) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Binary search in a sorted array.
<br></li>
<li> <a href='#function-_bin_search'><code>
_bin_search(array, left_edge, right_edge, value_to_search) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Helper function for binary search with recursion.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_bin_search">
<strong>Function</strong>
<code>_bin_search</code></h1>
This is the binary search with recursion implementation helper.

Binary search with recursion works on the cut,
so edges of the cut inside the array have to be provided.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;One-dimensional array consisting of whole numbers. <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index inside the array meaning left edge of indexes inside array (itself included) where search will be performed. <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index inside the array meaning right edge of indexes inside array (itself included) where search will be performed. <br></li>
<li> <strong>value_to_search</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Value to be searched among the given indexes slice inside array. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether searched value is inside the array <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bin_search">
<strong>Function</strong>
<code>bin_search</code></h1>
This function performs a binary search inside sorted array
consisting of whole numbers.
Time to work: O(log2 of the size of the array) - best case


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;One-dimensional array consisting of whole numbers <br></li>
<li> <strong>value_to_search</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Value to be searched inside the array <br></li>
<li> <strong>no_recursion</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Since binary search in general has two implementations, with or without recursion, this is the switcher between them. The no_recursion implementation requires exactly 3 variables which makes it very space efficient (O(1) to be exact), however time takes damage up to O(size of array). The recursion implementation requires space up to O(log2 of the size of the array), and time cuts up to the same value. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether searched value is inside the array <br>

---