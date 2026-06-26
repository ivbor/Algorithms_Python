<h1>Red-Black Tree Module</h1>
  This module defines a Red-Black Tree class which represents balanced binary search tree. By coloring nodes it is possible to maintain the height of O(logn), here in particular it is 3*log2n.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-TreeNode'><code>
TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a node in the Red-Black Tree.
<br></li>
<li> <a href='#class-BinarySearchTree'><code>
BinarySearchTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a Red-Black Tree.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-RBTreeNode">
<strong>Class</strong>
<code>RBTreeNode</code></h1>
Red-Black Tree Node Class

This class represents a node in a red-black tree.
It extends the TreeNode class.


<h2>Attributes</h2>
<ul>
<li> <strong>color</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the node, either 'red' or 'black'. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a Red-Black Tree Node.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be stored in the node. <br></li>
<li> <strong>color</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the node, either 'red' or 'black'. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-RedBlackTree">
<strong>Class</strong>
<code>RedBlackTree</code></h1>
Red-Black Tree Class

This class represents a red-black tree,
which is a self-balancing binary search tree.


<h2>Attributes</h2>
<ul>
<li> <strong>node_class</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The class to use for creating nodes in the tree. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize a RedBlackTree object.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, key: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Insert key into RedBlackTree.
<br></li>
<li> <a href='#function-handle_rb'><code>
handle_rb(self, new_node: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function managing insertion into RedBlackTree.
<br></li>
<li> <a href='#function-recolor'><code>
recolor(self, node: RBTreeNode, uncle: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function handling the case when only recoloring is needed.
<br></li>
<li> <a href='#function-rotate_and_recolor'><code>
rotate_and_recolor(self, node: RBTreeNode, right: bool) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function handling the case when both rotation and recoloring
    have to be done.
<br></li>
<li> <a href='#function-_left_rotate'><code>
_left_rotate(self, node: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function performing left rotation with node being moved to its
    left child place and the right child of the node moved to the
    node's place.
<br></li>
<li> <a href='#function-_right_rotate'><code>
_right_rotate(self, node: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function performing right rotation with node being moved to its
    right child place and the left child of the node moved to the
    node's place.
<br></li>
<li> <a href='#function-_delete'><code>
_delete(self, node: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function performing deletion of the node.
<br></li>
<li> <a href='#function-_fix_double_black'><code>
_fix_double_black(self, node: RBTreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    The function handling the double black violation case
    (parent and child are black) when deleting node.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a Red-Black Tree.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert a key into the red-black tree.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to insert into the tree. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-handle_rb">
<strong>Function</strong>
<code>handle_rb</code></h1>
Handle red-black tree properties after inserting a node.


<h2>Parameters</h2>
<ul>
<li> <strong>new_node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The newly inserted node. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-recolor">
<strong>Function</strong>
<code>recolor</code></h1>
Recolor nodes in the red-black tree after insertion.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The newly inserted node. <br></li>
<li> <strong>uncle</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The uncle node of the newly inserted node. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-rotate_and_recolor">
<strong>Function</strong>
<code>rotate_and_recolor</code></h1>
Rotate and recolor nodes in the red-black tree after insertion.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The newly inserted node. <br></li>
<li> <strong>right</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Flag indicating if the uncle of the newly inserted node is on the right (in this case is True) or on the left (False). <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_left_rotate">
<strong>Function</strong>
<code>_left_rotate</code></h1>
Perform a left rotation on the red-black tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node around which the rotation is performed. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_right_rotate">
<strong>Function</strong>
<code>_right_rotate</code></h1>
Perform a right rotation on the red-black tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node around which the rotation is performed. <br></li>
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
Delete a node from the red-black tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>RBTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node to be deleted. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_fix_double_black">
<strong>Function</strong>
<code>_fix_double_black</code></h1>
Fix double black violation in the red-black tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node causing the double black violation. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---