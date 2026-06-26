<h1>Vector Class Module</h1>
  This module defines a Python class, `Vector`, which implements a self-expanding array, also known as a dynamic array. A dynamic array can resize itself to accommodate additional elements as needed.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-Vector'><code>
Vector
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A self-expanding array implementation.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Vector">
<strong>Class</strong>
<code>Vector</code></h1>
A self-expanding array implementation, also known as a dynamic array.

This class defines a vector by specifying its starting capacity
(and optional initial elements). The vector can dynamically resize
itself to accommodate additional elements when needed.


<h2>Attributes</h2>
<ul>
<li> <strong>elements</strong>: <em>list or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An optional list of initial elements for the vector, by default None. <br></li>
<li> <strong>size</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial size of the vector, by default 0. <br></li>
<li> <strong>capacity</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the vector, by default 1. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, elements: list[Any] | None = None, size: int = 0,
   capacity: int = 1) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a new Vector instance with optional initial elements,
    size, and capacity.
<br></li>
<li> <a href='#function-__len__'><code>
__len__(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns the number of elements in the vector.
<br></li>
<li> <a href='#function-__contains__'><code>
__contains__(self, x: Any) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks if a given element is present in the vector.
<br></li>
<li> <a href='#function-__setitem__'><code>
__setitem__(self, i: int, x: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sets the element at the specified index in the vector.
<br></li>
<li> <a href='#function-__getitem__'><code>
__getitem__(self, i: int) -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieves the element at the specified index from the vector.
<br></li>
<li> <a href='#function-__delitem__'><code>
__delitem__(self, i: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Deletes the element at the specified index from the vector.
<br></li>
<li> <a href='#function-copy_to_new_vector'><code>
copy_to_new_vector(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Creates a new vector and copies elements from the current vector
    to the new one.
<br></li>
<li> <a href='#function-increase_capacity'><code>
increase_capacity(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Increases the capacity of the vector and copies elements
    to the new vector.
<br></li>
<li> <a href='#function-decrease_capacity'><code>
decrease_capacity(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Decreases the capacity of the vector and copies elements
    to the new vector.
<br></li>
<li> <a href='#function-erase'><code>
erase(self, i: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes the element at the specified index from the vector.
<br></li>
<li> <a href='#function-append'><code>
append(self, x: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Appends an element to the end of the vector.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, x: Any, i: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Inserts an element at the specified index in the vector.
<br></li>
<li> <a href='#function-pop'><code>
pop(self) -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Pops the last element from the vector.
<br></li>
<li> <a href='#function-extend'><code>
extend(self, elements: Sized and Iterable) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Appends to the vector all elements provided in `elements`.
<br></li>
<li> <a href='#function-__iter__'><code>
__iter__(self) -> Generator
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Iterates over all elements in the vector.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of vector.


<h2>Parameters</h2>
<ul>
<li> <strong>elements</strong>: <em>list or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An optional list of initial elements for the vector, by default None. <br></li>
<li> <strong>size</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial size of the vector, by default 0. <br></li>
<li> <strong>capacity</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the vector, by default 1. <br></li>
</ul>
<h2>Raises</h2>
<strong>NotImplementedError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the specified `capacity` is less than `size` or if invalid `capacity` or `size` values are provided. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__len__">
<strong>Function</strong>
<code>__len__</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- int The number of elements in the vector. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__contains__">
<strong>Function</strong>
<code>__contains__</code></h1>
Checks if a given element is present in the vector.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to check for in the vector. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the element is found, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__setitem__">
<strong>Function</strong>
<code>__setitem__</code></h1>
Sets the element at the specified index in the vector.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to set the element. <br></li>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to set. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the index is out of range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__getitem__">
<strong>Function</strong>
<code>__getitem__</code></h1>
Retrieves the element at the specified index from the vector.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to retrieve. <br></li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element at the specified index.   <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the index is out of range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__delitem__">
<strong>Function</strong>
<code>__delitem__</code></h1>
Deletes the element at the specified index from the vector.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to delete. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-copy_to_new_vector">
<strong>Function</strong>
<code>copy_to_new_vector</code></h1>
Change the size of the vector and copies elements from the current
vector to the new one.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-increase_capacity">
<strong>Function</strong>
<code>increase_capacity</code></h1>
Increases the capacity of the vector and copies elements
to the new vector.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-decrease_capacity">
<strong>Function</strong>
<code>decrease_capacity</code></h1>
Decreases the capacity of the vector and copies elements
to the new vector.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-erase">
<strong>Function</strong>
<code>erase</code></h1>
Removes the element at the specified index from the vector.

If the size of the vector becomes less than or equal to one-fourth
of its capacity after removal, the capacity is decreased.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to remove. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the index is out of range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-append">
<strong>Function</strong>
<code>append</code></h1>
Appends an element to the end of the vector.

If the size of the vector becomes equal to its capacity
after appending, the capacity is increased.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to append to the vector. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Inserts an element at the specified index in the vector.

If the size of the vector becomes equal to its capacity
after insertion, the capacity is increased.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to insert into the vector. <br></li>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to insert the element. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if the index is out of range. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pop">
<strong>Function</strong>
<code>pop</code></h1>
Pops the last element in the vector.


<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The popped element. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-extend">
<strong>Function</strong>
<code>extend</code></h1>
Appends all provided elements.


<h2>Parameters</h2>
<ul>
<li> <strong>elements</strong>: <em>Sized and Iterable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data structure supporting slices and containing elements to be appended <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__iter__">
<strong>Function</strong>
<code>__iter__</code></h1>
Iterates over all vector's elements.


<h2>Returns</h2>
<em>Generator</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---