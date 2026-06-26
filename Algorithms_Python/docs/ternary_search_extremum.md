<h1>Ternary Search Module</h1>
  This module provides two functions, `tern_search_min` and `tern_search_max`, for finding the minimum and maximum values of a function within a specified range, respectively. These search algorithms are suitable for cases where the function has only one minimum or maximum value within the given range.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-tern_search_min'><code>
tern_search_min(func, start, end, eps=1e-6)
    Find the minimum value of a function within a specified range.
</code></a> <br> </li>
<li> <a href='#function-tern_search_max'><code>
tern_search_max(func, start, end, eps=1e-6)
    Find the maximum value of a function within a specified range.
</code></a> <br> </li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tern_search_min">
<strong>Function</strong>
<code>tern_search_min</code></h1>
Ternary search for finding the minimum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one minimum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.


<h2>Parameters</h2>
<ul>
<li> <strong>func</strong>: <em>callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The function for which to find the minimum value. <br></li>
<li> <strong>start</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The start of the range for the search. <br></li>
<li> <strong>end</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The end of the range for the search. <br></li>
<li> <strong>eps</strong>: <em>float, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The epsilon parameter controlling the accuracy of search. Default is 1e-6. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The approximate x-coordinate of the minimum value of the function within the specified range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tern_search_max">
<strong>Function</strong>
<code>tern_search_max</code></h1>
Ternary search for finding the maximum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one maximum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.


<h2>Parameters</h2>
<ul>
<li> <strong>func</strong>: <em>callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The function for which to find the maximum value. <br></li>
<li> <strong>start</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The start of the range for the search. <br></li>
<li> <strong>end</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The end of the range for the search. <br></li>
<li> <strong>eps</strong>: <em>float, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The epsilon parameter controlling the accuracy of the search. Default is 1e-6. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The approximate x-coordinate of the maximum value of the function within the specified range. <br>

---