<h1>Two-Way Linked List Node</h1>
  This module provides a DoubleNode class representing a node in a two-way linked list, and a helper function `prev()` to access the previous node similar to the built-in `next()` function.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-prev'><code>
prev(obj: object with defined prev() method) -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieve the previous object connected to the given DoubleNode object or
    return None if there is no previous object.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-DoubleNode'><code>
DoubleNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a node in a two-way linked list with access to both    the next and previous nodes.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prev">
<strong>Function</strong>
<code>prev</code></h1>
Function-helper for easier calling for previous DoubleNode.

Works as analog for built-in function next().
This function retrieves the previous node connected
to the given DoubleNode object or None if there is no previous node.


<h2>Parameters</h2>
<ul>
<li> <strong>obj</strong>: <em>object with defined prev() method</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Object for which to retrieve the previous object. <br></li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The previous object or None if no previous object exists. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-DoubleNode">
<strong>Class</strong>
<code>DoubleNode</code></h1>
Two-Way Linked List Node Class

The DoubleNode class represents a node in a two-way linked list.
It has the same functionality as a regular Node, but it can also
access the previous node stored into the added attribute
using the prev() method.


<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, data=None, prev_node=None, next_node=None)
    Initialize a DoubleNode object.
</code></a> <br> </li>
<li> <a href='#function-prev'><code>
prev(self)
    Get the previous node of the DoubleNode.
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a DoubleNode object with optional data,
previous node, and next node.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>any, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be stored in the DoubleNode. Default is None.
prev_node: DoubleNode or None, optional The previous node in the linked list. Default is None.
next_node: DoubleNode or None, optional The next node in the linked list. Default is None. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the provided prev_node or next_node is of the wrong type. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prev_node">
<strong>Function</strong>
<code>prev_node</code></h1>
Get the previous node of the DoubleNode.


<h2>Returns</h2>
<em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The previous DoubleNode object or None if no previous node exists. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prev_node">
<strong>Function</strong>
<code>prev_node</code></h1>
Set the previous node of the DoubleNode.


<h2>Parameters</h2>
<ul>
<li> <strong>prev_node</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The previous node to be set for the DoubleNode. <br></li>
</ul>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the provided prev_node is of the wrong type. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prev">
<strong>Function</strong>
<code>prev</code></h1>
This method is defined for providing the same access option
for the previous node as for the next node
(to make possible the same call as for built-in function)


<h2>Parameters</h2>
<ul>
<li> <strong>prev_node</strong>: <em>DoubleNode or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The previous node to be set for the DoubleNode. <br></li>
</ul>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the provided prev_node is of the wrong type. <br>

---