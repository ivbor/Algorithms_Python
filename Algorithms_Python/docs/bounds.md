<h1>Binary Boundaries Search Module</h1>
  This module provides implementations of lower_bound and upper_bound search algorithms for finding the first and last occurrences of a given whole-numbered value in a sorted array. The lower_bound algorithm returns the index of the first encounter of the value, while the upper_bound algorithm returns the index of the last encounter.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-_lower_bound'><code>
_lower_bound(array: list[int], left_edge: int, right_edge: int,
  value_to_search: int) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    This is lower bound search helper.
<br></li>
<li> <a href='#function-lower_bound'><code>
lower_bound(array: list[int], value_to_search: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Determines the index of the first encounter of the whole-numbered value
    in a sorted array.
<br></li>
<li> <a href='#function-upper_bound'><code>
upper_bound(array: list[int], value_to_search: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Determines the index of the last encounter of the whole-numbered value
    in a sorted array.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_lower_bound">
<strong>Function</strong>
<code>_lower_bound</code></h1>
This is lower bound search helper.

Lower bound search works on the cut,
so edges of the cut inside the array have to be provided.
Array has to be sorted already, time and complexity equal
to the binary search with recursion.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;one-dimensional array consisting of whole numbers <br></li>
<li> <strong>left_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;index inside the array meaning left edge of indexes inside array (itself included) where search will be performed <br></li>
<li> <strong>right_edge</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;index inside the array meaning right edge of indexes inside array (itself included) where search will be performed <br></li>
<li> <strong>value_to_search</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;value to be searched among the given indexes slice inside array <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;index there the lower bound with required value is located <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-lower_bound">
<strong>Function</strong>
<code>lower_bound</code></h1>
This function determines where is first encounter of the whole-
numbered value.

This function utilizes algorithm working on the cut, hence the
searching job is delegated to the function-helper. The algorithm
itself is similar to the binary search without any additional
calculation complexity.
Array where is the value to be searched for has to be already sorted.
Function assumes by-default the presence of the value to be searched.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Sorted array where to find the first encounter of the searched value. <br></li>
<li> <strong>value_to_search</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Searched value which first encounter is to be found by the function. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;index of the first encounter of the searched value <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-upper_bound">
<strong>Function</strong>
<code>upper_bound</code></h1>
This function determines where is the last encounter of the whole-
numbered value.

This function is very similar to the lower_bound() except for it
searches for the last encounter. Generally, it is done via
lower_bound of the next (+1) whole value and subtraction 1 from the
returned index.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Sorted array where to find the last encounter of the searched value. <br></li>
<li> <strong>value_to_search</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Searched value which last encounter is to be found by the function. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;index of the last encounter of the searched value <br>

---