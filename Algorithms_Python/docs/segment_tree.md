<h1>Segment Tree Module</h1>
  This module defines two classes, SegmentTree and SegmentTreeOptimized, that implement a segment tree data structure. A segment tree is a versatile data structure that allows for efficient querying and updating of segments of an array.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-SegmentTree'><code>
SegmentTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a segment tree.
<br></li>
<li> <a href='#class-SegmentTreeOptimized'><code>
SegmentTreeOptimized
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    An optimized version of the segment tree class.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-SegmentTree">
<strong>Class</strong>
<code>SegmentTree</code></h1>
A class representing a segment tree.


<h2>Attributes</h2>
<ul>
<li> <strong>n</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of array on which SegmentTree is built. <br></li>
<li> <strong>tree_size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the SegmentTree. <br></li>
<li> <strong>tree_`action`</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;SegmentTrees for each distinct operation `action`. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, arr: list) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a new instance of the `SegmentTree` class with
    the given array.
<br></li>
<li> <a href='#function-build_tree'><code>
build_tree(self, current_index: int, left: int, right: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Builds the segment tree using a recursive function.
<br></li>
<li> <a href='#function-query'><code>
query(self, action: Callable, query_left: int, query_right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs a query on the segment tree for the specified range
    (including query_left and query_right indexes) and action.
<br></li>
<li> <a href='#function-_query'><code>
_query(self, current_index: int, segment_left: int,
  segment_right: int, action: Callable, query_left: int,
  query_right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively performs a query on the segment tree.
<br></li>
<li> <a href='#function-update'><code>
update(self, index: int, new_value: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Updates the value of a specified index in the segment tree.
<br></li>
<li> <a href='#function-_update'><code>
_update(self, current_index: int, segment_left: int, segment_right: int,
  index: int, new_value: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively updates the value of a specified index in the segment
    tree.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a new instance of the `SegmentTree` class with the given
array.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An array to built the SegmentTree on. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-build_tree">
<strong>Function</strong>
<code>build_tree</code></h1>
Builds the segment tree using a recursive function.


<h2>Parameters</h2>
<ul>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates actions. <br></li>
<li> <strong>left_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the tree with root in current_index. <br></li>
<li> <strong>right_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the tree with root in current_index. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-query">
<strong>Function</strong>
<code>query</code></h1>
Performs a query on the segment tree for the specified range and
action.


<h2>Parameters</h2>
<ul>
<li> <strong>action</strong>: <em>Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation to query among available for the tree. If action is not among available (sum, min, max, gcd), raises an error. <br></li>
<li> <strong>query_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the range, included in the query. <br></li>
<li> <strong>query_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the range, included in the query. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The result of the query.   <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If query is called to perform operation not among defined. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_query">
<strong>Function</strong>
<code>_query</code></h1>
Recursively performs a query on the segment tree.


<h2>Parameters</h2>
<ul>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates actions. <br></li>
<li> <strong>segment_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the segment with root in current_index. <br></li>
<li> <strong>segment_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the segment with root in current_index. <br></li>
<li> <strong>action</strong>: <em>Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation to query among available for the tree. <br></li>
<li> <strong>query_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the range, included in the query. <br></li>
<li> <strong>query_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the range, included in the query. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The result of the query. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-update">
<strong>Function</strong>
<code>update</code></h1>
Updates the value of a specified index in the segment tree.


<h2>Parameters</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index to update. <br></li>
<li> <strong>new_value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;New value to assign to the specified index. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_update">
<strong>Function</strong>
<code>_update</code></h1>
Recursively updates the value of a specified index in the segment
tree.


<h2>Parameters</h2>
<ul>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates actions. <br></li>
<li> <strong>segment_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the segment with root in current_index. <br></li>
<li> <strong>segment_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the segment with root in current_index. <br></li>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index to update. <br></li>
<li> <strong>new_value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;New value to assign to the specified index. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-SegmentTreeOptimized">
<strong>Class</strong>
<code>SegmentTreeOptimized</code></h1>
An optimized version of the segment tree class.


<h2>Attributes</h2>
<ul>
<li> <strong>n</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The length of array on which SegmentTree is built. <br></li>
<li> <strong>tree_size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the SegmentTree. <br></li>
<li> <strong>tree</strong>: <em>list[list[float]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The main tree structure. Contains lists with the length equal to number of actions defined. <br></li>
<li> <strong>action</strong>: <em>list[Callable]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list where all defined operations are stored. <br></li>
<li> <strong>arr</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list SegmentTreeOptimized is built on <br></li>
<li> <strong>neutral</strong>: <em>dict[Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The dict defining the neutral elements for each operation. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, arr) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a new instance of the `SegmentTreeOptimized` class with
    the given array.
<br></li>
<li> <a href='#function-determine_queries'><code>
determine_queries(self, left_index: int, right_index: int) ->
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    tuple[Callable, Callable] | tuple[Callable, float] |
    tuple[float, float]
    Determines the queries for the left and right indices.
<br></li>
<li> <a href='#function-build_tree'><code>
build_tree(self, arr: list[float], current_index: int,
 left: int, right: int, action: Callable | None = None) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Builds the segment tree using a recursive function.
<br></li>
<li> <a href='#function-query'><code>
query(self, action: Callable, query_left: int, query_right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs a query on the segment tree for the specified range
    (including query_left and query_right indexes) and action.
<br></li>
<li> <a href='#function-_query'><code>
_query(self, current_index: int, segment_left: int,
 segment_right: int, action: Callable, query_left: int,
 query_right: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively performs a query on the segment tree.
<br></li>
<li> <a href='#function-update'><code>
update(self, index: int, new_value: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Updates the value of a specified index in the segment tree.
<br></li>
<li> <a href='#function-_update'><code>
_update(self, current_index: int, segment_left: int,
 segment_right: int, index: int, new_value: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively updates the value of a specified index in the segment
    tree.
<br></li>
<li> <a href='#function-new_action'><code>
new_action(self, func: Callable, neutral: float)
    Adds a new action to the segment tree and updates the
    tree accordingly.
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a new instance of the `SegmentTreeOptimized` class with
the given array.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An array to build the SegmentTree on. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-determine_queries">
<strong>Function</strong>
<code>determine_queries</code></h1>
Determines the queries for the left and right indices.
Its purpose is to give the same looking calls for the queries
with only one element and with more than one element.


<h2>Parameters</h2>
<ul>
<li> <strong>left_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left index. <br></li>
<li> <strong>right_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right index. <br></li>
</ul>
<h2>Returns</h2>
<em>left_query: Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A lambda function representing the query for the left index.  right_query: Callable A lambda function representing the query for the right index. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-build_tree">
<strong>Function</strong>
<code>build_tree</code></h1>
Builds the segment tree using a recursive function.


<h2>Parameters</h2>
<ul>
<li> <strong>arr</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The array on which the SegmentTreeOptimized is built. <br></li>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates action. <br></li>
<li> <strong>left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the tree with root in current_index. <br></li>
<li> <strong>right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the tree with root in current_index. <br></li>
<li> <strong>action</strong>: <em>Callable, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation to query among available for the tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-query">
<strong>Function</strong>
<code>query</code></h1>
Performs a query on the segment tree for the specified range and
action.


<h2>Parameters</h2>
<ul>
<li> <strong>action</strong>: <em>Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation to query among available for the tree. If action is not among available, raises an error. <br></li>
<li> <strong>query_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the range, included in the query. <br></li>
<li> <strong>query_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the range, included in the query. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The result of the query. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_query">
<strong>Function</strong>
<code>_query</code></h1>
Recursively performs a query on the segment tree.


<h2>Parameters</h2>
<ul>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates actions. <br></li>
<li> <strong>segment_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the segment with root in current_index. <br></li>
<li> <strong>segment_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the segment with root in current_index. <br></li>
<li> <strong>action</strong>: <em>Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Operation to query among available for the tree. <br></li>
<li> <strong>query_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the range, included in the query. <br></li>
<li> <strong>query_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the range, included in the query. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The result of the query. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-update">
<strong>Function</strong>
<code>update</code></h1>
Updates the value of a specified index in the segment tree.


<h2>Parameters</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index to update. <br></li>
<li> <strong>new_value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;New value to assign to the specified index. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_update">
<strong>Function</strong>
<code>_update</code></h1>
Recursively updates the value of a specified index in the
segment tree.


<h2>Parameters</h2>
<ul>
<li> <strong>current_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index for which the function currently calculates actions. <br></li>
<li> <strong>segment_left</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Left border of the segment with root in current_index. <br></li>
<li> <strong>segment_right</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Right border of the segment with root in current_index. <br></li>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index to update. <br></li>
<li> <strong>new_value</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;New value to assign to the specified index. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-new_action">
<strong>Function</strong>
<code>new_action</code></h1>
Adds a new action to the segment tree and updates the tree
accordingly.


<h2>Parameters</h2>
<ul>
<li> <strong>func</strong>: <em>Callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new action to add to the segment tree. <br></li>
<li> <strong>neutral</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The neutral element associated with the new action. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---