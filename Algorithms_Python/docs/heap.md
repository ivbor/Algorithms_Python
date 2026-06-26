<h1>Binary Heap and Sort</h1>
  A module for implementing a binary tree-based min-heap data structure and heap sort algorithm. This module contains classes and functions for working with binary tree-based min-heaps and performing heap sort. A binary tree-based min-heap is a data structure where the minimum value is stored at the root, and each parent node contains elements smaller than its children.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-heap_sort'><code>
heap_sort(array: list[float]) -> list[float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sorts an array in ascending order using the heap sort algorithm.
    Heap sort is an efficient comparison-based sorting algorithm that uses
    a binary heap to perform the sorting.
<br></li>
<li> <a href='#function-sift_up'><code>
sift_up(array: list[float], element_index: int, size: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs the sift-up operation to maintain the heap property.
<br></li>
<li> <a href='#function-sift_down'><code>
sift_down(array: list[float], element_index: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs the sift-down operation to maintain the heap property.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-Heap'><code>
Heap
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A binary tree-based min-heap that extends the Vector class to represent    the heap. It provides methods for insertion, removal of the minimum    element, and other heap-related operations.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Heap">
<strong>Class</strong>
<code>Heap</code></h1>
A binary tree-based min-heap data structure.

This class extends the Vector class to represent a binary
tree-based min-heap, where the minimum value is stored at the root,
and each parent node contains elements smaller than its children.


<h2>Attributes</h2>
<ul>
<li> <strong>elements</strong>: <em>list or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An optional list of initial elements for the heap, by default None. <br></li>
<li> <strong>size</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial size of the heap, by default 0. <br></li>
<li> <strong>capacity</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the heap, by default 1. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, elements: list[float] | None = None,
   size: int = 0, capacity: int = 1) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize the heap.
<br></li>
<li> <a href='#function-append'><code>
append(self, x: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Append an element to the heap.
<br></li>
<li> <a href='#function-get_children'><code>
get_children(self, i: int) -> tuple(float, float) or float or None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Get the children of a node at the specified index.
<br></li>
<li> <a href='#function-height'><code>
height(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate the height of the heap.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, x: float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Insert an element into the heap.
<br></li>
<li> <a href='#function-remove_min'><code>
remove_min(self) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Remove and return the minimum element from the heap.
<br></li>
<li> <a href='#function-__repr__'><code>
__repr__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return a string representation of the heap.
<br></li>
<li> <a href='#function-erase'><code>
erase(self) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Alias for `remove_min`.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a new Heap instance.


<h2>Parameters</h2>
<ul>
<li> <strong>elements</strong>: <em>list or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An optional list of initial elements for the heap, by default None. <br></li>
<li> <strong>size</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial size of the heap, by default 0. <br></li>
<li> <strong>capacity</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the heap, by default 1. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-append">
<strong>Function</strong>
<code>append</code></h1>
Append an element to the heap.

This method is an alias for `insert`.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to append to the heap. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_children">
<strong>Function</strong>
<code>get_children</code></h1>
Get the children of a node at the specified index.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the node for which to retrieve children. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple or float or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing the left and right children of the node if both exist, the left child if only the left child exists, or None if the node has no children. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-height">
<strong>Function</strong>
<code>height</code></h1>
Calculate the height of the heap.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The height of the heap. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert an element into the heap.

If the size of the heap becomes equal to its capacity after
insertion, the capacity is increased.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to insert into the heap. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-remove_min">
<strong>Function</strong>
<code>remove_min</code></h1>
Remove and return the minimum element from the heap.

If the size of the heap becomes less than or equal to one-fourth
of its capacity after removal, the capacity is decreased.


<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The minimum element in the heap.   <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the heap is empty. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__repr__">
<strong>Function</strong>
<code>__repr__</code></h1>
Return a string representation of the heap.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A string representation of the heap in a tree-like format. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-erase">
<strong>Function</strong>
<code>erase</code></h1>
Alias for `remove_min`.


<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The minimum element in the heap. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-sift_up">
<strong>Function</strong>
<code>sift_up</code></h1>
Perform the sift-up operation to maintain heap property.


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list representing the elements of the heap. <br></li>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which the sift-up operation is performed. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-sift_down">
<strong>Function</strong>
<code>sift_down</code></h1>
Perform the sift-down operation to maintain heap property.


<h2>Parameters</h2>
<ul>
<li> <strong>a</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list representing the elements of the heap. <br></li>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which the sift-down operation is performed. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the heap. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-heap_sort">
<strong>Function</strong>
<code>heap_sort</code></h1>
Sort an array in ascending order using the heap sort algorithm.
Heap sort is a comparison-based sorting algorithm that builds a binary
heap data structure and repeatedly extracts the minimum element from the
heap. The sorted elements are stored in the original array. This algorithm
has a time complexity of O(n log n) in the worst case, making it efficient
for large datasets. However, it is not an in-place sorting algorithm since
it requires additional space for the heap, making its O(n) space
complexity.
The heap sort algorithm consists of two main phases: heapify and sorting.
The "heapify" phase builds a binary heap from the input array,
ensuring that the heap property is maintained (parent nodes have smaller
values than their children).
The "sorting" phase repeatedly removes the minimum element from the heap
and places it at the end of the array until the heap is empty.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list to be sorted. <br></li>
</ul>
<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The sorted list in ascending order. <br>

---