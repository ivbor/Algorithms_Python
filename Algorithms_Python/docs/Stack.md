<h1>Stack Module</h1>
  This module provides a Python implementation of a stack data structure. The stack follows the Last-In-First-Out (LIFO) principle, where the last element added is the first one to be removed. This class provides methods to manipulate and query the stack.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-Stack'><code>
Stack
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A stack data structure implemented using a doubly-linked list.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Stack">
<strong>Class</strong>
<code>Stack</code></h1>
A Python implementation of a stack data structure using
a doubly-linked list.

The stack follows the Last-In-First-Out (LIFO) principle,
where the last element added is the first one to be removed.
This class provides methods to manipulate and query the stack.


<h2>Attributes</h2>
<ul>
<li> <strong>head</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The top (front) of the stack. Default is None. <br></li>
<li> <strong>tail</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The bottom (back) of the stack. Default is None. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of elements in the stack. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes an empty stack.
<br></li>
<li> <a href='#function-push'><code>
push(self, value) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds a new element to the back of the stack.
<br></li>
<li> <a href='#function-pop'><code>
pop(self) -> Any | None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes and returns the back element from the stack.
<br></li>
<li> <a href='#function-back'><code>
back(self) -> Any | None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieves the element at the back of the stack
    without removing it.
<br></li>
<li> <a href='#function-front'><code>
front(self) -> Any | None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieves the element at the top of the stack.
<br></li>
<li> <a href='#function-__len__'><code>
__len__(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns the number of elements currently in the stack.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes an empty stack.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-push">
<strong>Function</strong>
<code>push</code></h1>
Adds a new element to the back of the stack.


<h2>Parameters</h2>
<ul>
<li> <strong>value</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value to be added to the stack. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pop">
<strong>Function</strong>
<code>pop</code></h1>
Removes and returns the back element from the stack.


<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The removed element from the back of the stack. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-back">
<strong>Function</strong>
<code>back</code></h1>
Retrieves the element at the back of the stack
without removing it.


<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element at the back of the stack. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-front">
<strong>Function</strong>
<code>front</code></h1>
Retrieves the element at the top of the stack.


<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element at the top of the stack. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__len__">
<strong>Function</strong>
<code>__len__</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- int The number of elements in the stack. <br>

---