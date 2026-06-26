<h1>Sparse table module</h1>
  This module defines a SparseTable class for efficient range queries on an array. It allows you to quickly compute the minimum, maximum, and sum of values within a specified range. The data structure is built on a tuple for immutability, making it suitable for scenarios where the input array should not be modified after construction.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-SparseTable'><code>
SparseTable
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class for creating and querying a sparse table for efficient range    queries.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-SparseTable">
<strong>Class</strong>
<code>SparseTable</code></h1>
A class for creating and querying a sparse table for efficient range
queries on an array.



<h2>Attributes</h2>
<ul>
<li> <strong>arr</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array on which range queries will be performed. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-append'><code>
append(self, x: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Raises an error, overwriting append for tuple, so that Sparse table
    would be completely unchangeable after creation.
<br></li>
<li> <a href='#function-extend'><code>
extend(self, x: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Raises an error, overwriting extend for tuple, so that Sparse table
    would be completely unchangeable after creation.
<br></li>
<li> <a href='#function-query_min'><code>
query_min(self, left: int, right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Query the minimum value within a specified range, both parameters
    included.
<br></li>
<li> <a href='#function-query_max'><code>
query_max(self, left: int, right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Query the maximum value within a specified range, both parameters
    included.
<br></li>
<li> <a href='#function-query_sum'><code>
query_sum(self, left: int, right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Query the cumulative sum of values within a specified range, both
    parameters included.
<br></li>
<li> <a href='#function-__new__'><code>
__new__(cls, arr: Iterable) -> SparseTable
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Create a new instance of SparseTable using tuple's __new__()
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a SparseTable instance with the given input array.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array on which range queries will be performed. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__new__">
<strong>Function</strong>
<code>__new__</code></h1>
Create a new SparseTable instance.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The input array on which range queries will be performed. <br></li>
</ul>
<h2>Returns</h2>
<em>SparseTable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A new instance of the SparseTable class. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-append">
<strong>Function</strong>
<code>append</code></h1>
This method raises a TypeError because SparseTable instances are
immutable and cannot be changed after creation.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to be appended. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;SparseTable cannot be changed after creation.   <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-extend">
<strong>Function</strong>
<code>extend</code></h1>
This method raises a TypeError because SparseTable instances are
immutable and cannot be changed after creation.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list with elements to append. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;SparseTable cannot be changed after creation.   <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-query_min">
<strong>Function</strong>
<code>query_min</code></h1>
Query the minimum value within a specified range.


<h2>Parameters</h2>
<ul>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left index of the range (inclusive). <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right index of the range (inclusive). <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The minimum value within the specified range [left, right]. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-query_max">
<strong>Function</strong>
<code>query_max</code></h1>
Query the maximum value within a specified range.


<h2>Parameters</h2>
<ul>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left index of the range (inclusive). <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right index of the range (inclusive). <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum value within the specified range [left, right]. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-query_sum">
<strong>Function</strong>
<code>query_sum</code></h1>
Query the cumulative sum of values within a specified range.


<h2>Parameters</h2>
<ul>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left index of the range (inclusive). <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right index of the range (inclusive). <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The cumulative sum of values within the specified range [left, right]. <br>

---