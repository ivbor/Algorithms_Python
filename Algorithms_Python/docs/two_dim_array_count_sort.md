<h1>Two-Dimensional Array Count Sort Module</h1>
  This module provides a function, `two_dim_array_count_sort`, for sorting a 2-dimensional array consisting of whole numbers. The function can sort the 1-dimensional arrays inside a 2-dimensional array in ascending order by all indexes (by default) or by exact indexes in the order they are presented.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-two_dim_array_count_sort'><code>
two_dim_array_count_sort(a: list[list[int]], keys: str | list | int = 'all')
    Sorts a 2-dimensional array consisting of whole numbers.
</code></a> <br> </li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-two_dim_array_count_sort">
<strong>Function</strong>
<code>two_dim_array_count_sort</code></h1>
Sorts a 2-dimensional array consisting of whole numbers.

This function sorts the 1-dimensional arrays inside a 2-dimensional array
in ascending order by all indexes (by default) or by exact indexes
in the order they are presented. Be mindful that this sort populates
an array with absent places in each row's key position with sentinel
values (-inf). In this case the ascending sort will always lead to rows
with absent values being put higher than ones without them.


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The 2-dimensional array to be sorted. <br></li>
<li> <strong>keys</strong>: <em>'all', list of int, or int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Specifies the indexes to sort by. If 'all', it sorts by all indexes (default). If a list of integers is provided, it sorts by the exact indexes in the specified order. If an integer is provided, it sorts by a single index. <br></li>
</ul>
<h2>Returns</h2>
<em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The sorted 2-dimensional array.   <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the 'keys' argument is of an unsupported type. <br>

---