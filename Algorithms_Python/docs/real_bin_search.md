<h1>Real Binary Search Module</h1>
 This module provides a binary search function for finding an approximate input value (x) for which a given function func(x) is close to func_value within a specified epsilon. The binary search algorithm is suitable for monotonic functions.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-real_bin_search'><code>
real_bin_search(func, func_value, left_edge,
    right_edge, eps=1e-6, check=False)
    Performs a binary search among real numbers to find an x
    where func(x) is approximately equal to func_value.
</code></a> <br> </li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-real_bin_search">
<strong>Function</strong>
<code>real_bin_search</code></h1>
This function performs a binary search among real numbers to find an x
where func(x) is approximately equal to func_value.

It works only for monotonic functions and
has a time complexity of O(log2(n)),
where n is the number of epsilon intervals that can fit in the
absolute difference between right_edge and left_edge.


<h2>Parameters</h2>
<ul>
<li> <strong>func</strong>: <em>callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The function for which we are searching for an input value. <br></li>
<li> <strong>func_value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The target value we want to find an input value for. <br></li>
<li> <strong>left_edge</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left edge of the search interval. The function is assumed to exist within this interval. <br></li>
<li> <strong>right_edge</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right edge of the search interval. The function is assumed to exist within this interval. <br></li>
<li> <strong>eps</strong>: <em>float, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The epsilon value that determines the desired accuracy of the result. The search will stop when the interval size becomes smaller than this epsilon. Default is 1e-6. <br></li>
<li> <strong>check</strong>: <em>bool, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If True, the function will perform a check to ensure that the func_value is reachable within the given edges. Default is False. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The approximate input value (x) for which func(x) is close to func_value within the specified epsilon.   <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Is raised if the check parameter is set to True and the func_value is unreachable within the given edges. <br>

---