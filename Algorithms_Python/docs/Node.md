<h1>Node Module</h1>
 This module defines a simple one-way node class that can store data and have a reference to the next node in a linked list.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-Node'><code>
Node
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a one-way node with basic operations.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Node">
<strong>Class</strong>
<code>Node</code></h1>
Simple One-Way Node Class

The Node class represents a simple one-way node that can store data and
have a reference to the next node in a linked list. It supports basic
operations like getting the next node and printing the data.


<h2>Attributes</h2>
<ul>
<li> <strong>_next_node</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Reference to the next node if it exists. <br></li>
<li> <strong>_data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data stored inside the node. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, data=None, next_node=None)
    Initialize a Node object with optional data and next node.
</code></a> <br> </li>
<li> <a href='#function-__str__'><code>
__str__(self)
    Return a string representation of the data stored in the node.
</code></a> <br> </li>
<li> <a href='#function-__next__'><code>
__next__(self)
    Get the reference to the next node.
</code></a> <br> </li>
<li> <a href='#function-__repr__'><code>
__repr__(self)
    Return a string representation of the node.
</code></a> <br> </li>
<li> <a href='#function-__eq__'><code>
__eq__(self, other)
    Compare if two nodes are the same (reference equality).
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a Node object with optional data and next node.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>any, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be stored in the node. Default is None. <br></li>
<li> <strong>next_node</strong>: <em>Node or None, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The next node in the linked list. Default is None. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the provided next_node is of the wrong type. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__str__">
<strong>Function</strong>
<code>__str__</code></h1>
Return a string representation of the data stored in the node.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The string representation of the data. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__next__">
<strong>Function</strong>
<code>__next__</code></h1>
Get the reference to the next node.


<h2>Returns</h2>
<em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The reference to the next node or None if it doesn't exist. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__repr__">
<strong>Function</strong>
<code>__repr__</code></h1>
Return a string representation of the node.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The string representation of the node. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__eq__">
<strong>Function</strong>
<code>__eq__</code></h1>
Compare if two nodes are the same (reference equality).


<h2>Parameters</h2>
<ul>
<li> <strong>other</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The other object to compare with. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if both nodes are the same, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-next_node">
<strong>Function</strong>
<code>next_node</code></h1>
Get the reference to the next node.


<h2>Returns</h2>
<em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The reference to the next node or None if it doesn't exist. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-next_node">
<strong>Function</strong>
<code>next_node</code></h1>
Set the reference to the next node.


<h2>Parameters</h2>
<ul>
<li> <strong>next_node</strong>: <em>Node or None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The next node to be set for the current node. <br></li>
</ul>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the provided next_node is of the wrong type. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-data">
<strong>Function</strong>
<code>data</code></h1>
Get or set the data stored in the node.


<h2>Returns</h2>
<em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data stored in the node. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-data">
<strong>Function</strong>
<code>data</code></h1>
Set the data stored in the node.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be stored in the node. <br></li>
</ul>

---