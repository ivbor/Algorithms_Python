<h1>Cyclic Linked List Module</h1>
  This module defines a cyclic linked list, which is a variation of a linked list where the tail node is connected to the head node, creating a closed loop.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-CyclicLinkedList'><code>
CyclicLinkedList
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Represents a cyclic linked list and provides additional    methods and behavior specific to cyclic linked lists.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-CyclicLinkedList">
<strong>Class</strong>
<code>CyclicLinkedList</code></h1>
Represents a cyclic linked list, which is a variation of a linked list
where the tail node is connected to the head node, creating a closed loop.

This class inherits from the LinkedList class and provides additional
methods and behavior specific to cyclic linked lists. This means that
operations like list traversal and iteration will continue
indefinitely in a loop.


<h2>Attributes</h2>
<ul>
<li> <strong>_head</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The head node of the cyclic linked list. Default is None. <br></li>
<li> <strong>_tail</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The tail node of the cyclic linked list. Default is None. <br></li>
<li> <strong>_size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of elements in the cyclic linked list. Default is None. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, head=None, tail=None) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes empty cyclic linked list.
<br></li>
<li> <a href='#function-list_all'><code>
list_all(self) -> List[Unknown]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns a list containing all the elements in the cyclic linked list.
<br></li>
<li> <a href='#function-search'><code>
search(self, i) -> tuple(DoubleNode | None, DoubleNode | None)
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Searches for the i-th element in the cyclic linked list and returns
    the previous and current nodes before the i-th element.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, i, x) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Inserts a new element x at the specified index i in
    the cyclic linked list.
<br></li>
<li> <a href='#function-erase'><code>
erase(self, i) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes the element at the specified index i from
    the cyclic linked list.
<br></li>
<li> <a href='#function-update'><code>
update(self, i, x) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Updates the element at the specified index i in
    the cyclic linked list with x.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes an empty cyclic linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>head</strong>: <em>DoubleNode or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The head node of the cyclic linked list. Default is None. <br></li>
<li> <strong>tail</strong>: <em>DoubleNode or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The tail node of the cyclic linked list. Default is None. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-list_all">
<strong>Function</strong>
<code>list_all</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- List[Unknown] A list containing all the elements in the cyclic linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Searches for the i-th element in the cyclic linked list and returns
the node before the i-th element (previous)
and the node with i-th element (current).


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to search for. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple(DoubleNode | None, DoubleNode | None)</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing the previous and current nodes if they exist. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Inserts a new element x at the specified index i
in the cyclic linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to insert the new element. <br></li>
<li> <strong>x</strong>: <em>Unknown</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to insert. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-erase">
<strong>Function</strong>
<code>erase</code></h1>
Removes the element at the specified index i
from the cyclic linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to remove. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-update">
<strong>Function</strong>
<code>update</code></h1>
Updates the element at the specified index i
in the cyclic linked list with x.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the element to update. <br></li>
<li> <strong>x</strong>: <em>Unknown</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new value to update the element with. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---