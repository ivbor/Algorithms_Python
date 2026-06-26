<h1>AVL Tree Module</h1>
  This module implements an AVL tree, a self-balancing binary search tree. This tree has very fixed height, which is smaller than that of RedBlackTree, and is between log2(size) and 2*log2(size).  
<h2>Classes</h2>
<ul>
<li> <a href='#class-AVLNode'><code>
AVLNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a node in an AVL tree, extending TreeNode.
<br></li>
<li> <a href='#class-AVLTree'><code>
AVLTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing an AVL tree,    extending RedBlackTree and BinarySearchTree.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-AVLNode">
<strong>Class</strong>
<code>AVLNode</code></h1>
Node for AVL Tree

Represents a node in an AVL tree. Inherits from TreeNode and provides
methods to calculate height and balance factor.


<h2>Attributes</h2>
<ul>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data stored in the node. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, data: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize an AVLNode.
<br></li>
<li> <a href='#function-height'><code>
height(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate the height of the node.
<br></li>
<li> <a href='#function-balance_factor'><code>
balance_factor(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate the balance factor of the node.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize an AVLNode object with data.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be stored in the node. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-height">
<strong>Function</strong>
<code>height</code></h1>
Calculate the height of the node.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The height of the node. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-balance_factor">
<strong>Function</strong>
<code>balance_factor</code></h1>
Calculate the balance factor of the node.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The balance factor of the node. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-AVLTree">
<strong>Class</strong>
<code>AVLTree</code></h1>
AVL Tree Implementation

Represents an AVL tree, a self-balancing binary search tree.


<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize an AVLTree object.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, key: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Insert a key into the AVL tree.
<br></li>
<li> <a href='#function-_insert'><code>
_insert(root: AVLNode, new_node: AVLNode)
    Helper method to insert a new node into the AVL tree.
</code></a> <br> </li>
<li> <a href='#function-delete'><code>
delete(self, key: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Delete a key from the AVL tree.
<br></li>
<li> <a href='#function-_delete'><code>
_delete(node: AVLNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Helper method to delete a node from the AVL tree.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize an AVLTree object.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert a key into the AVL tree.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be inserted into the AVL tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_insert">
<strong>Function</strong>
<code>_insert</code></h1>
Helper method to insert a new node into the AVL tree.


<h2>Parameters</h2>
<ul>
<li> <strong>root</strong>: <em>AVLNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The root node of the AVL tree. <br></li>
<li> <strong>new_node</strong>: <em>AVLNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new node to be inserted into the AVL tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-delete">
<strong>Function</strong>
<code>delete</code></h1>
Delete a key from the AVL tree.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be deleted from the AVL tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_delete">
<strong>Function</strong>
<code>_delete</code></h1>
Helper method to delete a node from the AVL tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>AVLNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node to be deleted from the AVL tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---