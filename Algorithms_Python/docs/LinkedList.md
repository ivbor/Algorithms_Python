<h1>Linked List Module</h1>
  A module for implementing a one-way linked list data structure. This module contains the LinkedList class, which represents a one-way linked list data structure. The LinkedList class allows for the creation and manipulation of a linked list, including appending, inserting, erasing, and searching for elements.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-LinkedList'><code>
LinkedList
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A one-way linked list data structure.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-LinkedList">
<strong>Class</strong>
<code>LinkedList</code></h1>
Linked List Implementation.

The LinkedList class represents a one-way linked list data structure.
It allows for the creation and manipulation of a linked list, including
appending, inserting, erasing, and searching for elements.


<h2>Attributes</h2>
<ul>
<li> <strong>head</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first node of the linked list. <br></li>
<li> <strong>tail</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The last node of the linked list. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of elements in the linked list. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, head=None, tail=None) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Creates an instance of the LinkedList class.
    It is important to note, that if there already is some
    connection between head and tail nodes - this method will
    effectively parse it.
<br></li>
<li> <a href='#function-append'><code>
append(self, x) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Add an element to the end of the linked list.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, i, x) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Insert an element at a specific index.
<br></li>
<li> <a href='#function-erase'><code>
erase(self, i) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Remove the element at a specific index.
<br></li>
<li> <a href='#function-__contains__'><code>
__contains__(self, x) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check if an element exists in the linked list.
<br></li>
<li> <a href='#function-__iter__'><code>
__iter__(self) -> Generator
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Iterate through the elements of the linked list.
<br></li>
<li> <a href='#function-list_all'><code>
list_all(self) -> List[]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return a list of all elements in the linked list.
<br></li>
<li> <a href='#function-__str__'><code>
__str__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return a string representation of the linked list.
<br></li>
<li> <a href='#function-__repr__'><code>
__repr__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Print method for the linked list.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a Linked List.


<h2>Parameters</h2>
<ul>
<li> <strong>head</strong>: <em>Node or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The first node of the linked list. Default is None. <br></li>
<li> <strong>tail</strong>: <em>Node or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The last node of the linked list. Default is None. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-head">
<strong>Function</strong>
<code>head</code></h1>
Get the head of the linked list.


<h2>Returns</h2>
<em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The head of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-head">
<strong>Function</strong>
<code>head</code></h1>
Set the head of the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>head</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new head of the linked list. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tail">
<strong>Function</strong>
<code>tail</code></h1>
Get the tail of the linked list.


<h2>Returns</h2>
<em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The tail of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tail">
<strong>Function</strong>
<code>tail</code></h1>
Raise NotImplementedError when trying to set the tail.
The tail should be set through insert or initialization methods.


<h2>Parameters</h2>
<ul>
<li> <strong>tail</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new tail of the linked list. <br></li>
</ul>
<h2>Raises</h2>
<strong>NotImplementedError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;When trying to set the tail directly. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-size">
<strong>Function</strong>
<code>size</code></h1>
Get the size of the linked list.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-size">
<strong>Function</strong>
<code>size</code></h1>
Raise NotImplementedError when trying to set the size.
The size is calculated automatically.


<h2>Parameters</h2>
<ul>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new size of the linked list. <br></li>
</ul>
<h2>Raises</h2>
<strong>NotImplementedError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;When trying to set the size directly. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__contains__">
<strong>Function</strong>
<code>__contains__</code></h1>
Check if a given element is present in the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to check for in the linked list. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the element is found, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__iter__">
<strong>Function</strong>
<code>__iter__</code></h1>
Iterate through the elements of the linked list.


<h2>Returns</h2>
<em>generator</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A generator to iterate through the elements. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-list_all">
<strong>Function</strong>
<code>list_all</code></h1>
Return a list of all elements in the linked list.


<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list containing all elements of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__str__">
<strong>Function</strong>
<code>__str__</code></h1>
Return a string representation of the linked list.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A string representation of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__repr__">
<strong>Function</strong>
<code>__repr__</code></h1>
Return a string representation of the linked list.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A string representation of the linked list. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-append">
<strong>Function</strong>
<code>append</code></h1>
Append an element to the end of the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to append to the linked list. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Search for nodes at a given index in the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to search for nodes. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing the previous and current nodes. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert an element at a given index in the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to insert the element. <br></li>
<li> <strong>x</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to insert into the linked list. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;When trying to insert with negative indexing. Negative indexing is an undefined operation.   <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-erase">
<strong>Function</strong>
<code>erase</code></h1>
Remove an element at the specified index in the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to remove the element. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the index is out of bounds or negative.   <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-update">
<strong>Function</strong>
<code>update</code></h1>
Update the element at the specified index in the linked list.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index at which to update the element.
x: any The new value to assign to the element. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the index is negative.   <br>

---