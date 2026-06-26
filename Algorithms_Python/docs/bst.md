<h1>Binary Search Tree Module</h1>
  This module defines a Binary Search Tree (BST) class that allows the insertion, deletion, and search of elements. It also provides methods for traversing the tree in-order, finding the minimum and maximum values, and determining the successor and predecessor of a given element.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-TreeNode'><code>
TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a node in the Binary Search Tree.
<br></li>
<li> <a href='#class-BinarySearchTree'><code>
BinarySearchTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing a Binary Search Tree.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-TreeNode">
<strong>Class</strong>
<code>TreeNode</code></h1>
A class representing a node in the Binary Search Tree.
Also a basic class to inherit from for more complicated tree nodes.


<h2>Attributes</h2>
<ul>
<li> <strong>left</strong>: <em>TreeNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The left child of the node if present, else - None. Default is None. <br></li>
<li> <strong>right</strong>: <em>TreeNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The right child of the node if present, else - None. Default is None. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a new instance of the TreeNode class with the specified
data.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data to be put into the TreeNode. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-BinarySearchTree">
<strong>Class</strong>
<code>BinarySearchTree</code></h1>
A class representing a Binary Search Tree.


<h2>Attributes</h2>
<ul>
<li> <strong>root</strong>: <em>TreeNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The root node of the tree if exists, else None. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the tree. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a new instance of the BinarySearchTree class.
<br></li>
<li> <a href='#function-insert'><code>
insert(self, data: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Inserts a new element with the specified data into the Binary Search
    Tree.
<br></li>
<li> <a href='#function-_insert'><code>
_insert(self, root: TreeNode, new_node: TreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively inserts a new node into the Binary Search Tree.
<br></li>
<li> <a href='#function-delete'><code>
delete(self, data: int | float) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Deletes the node with the specified data from the Binary Search Tree.
<br></li>
<li> <a href='#function-_delete'><code>
_delete(self, node: TreeNode) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively deletes the specified node from the Binary Search Tree.
<br></li>
<li> <a href='#function-search'><code>
search(self, data: int | float) -> TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Searches for a node with the specified data in the Binary Search Tree.
<br></li>
<li> <a href='#function-_search'><code>
_search(self, root: TreeNode, data: int | float) -> TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively searches for a node with the specified data in the
    Binary Search Tree.
<br></li>
<li> <a href='#function-in_order_traversal'><code>
in_order_traversal(self) -> list[int | float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs an in-order traversal of the Binary Search Tree and returns
    a list of elements.
<br></li>
<li> <a href='#function-_in_order_traversal_rec'><code>
_in_order_traversal_rec(self, root: TreeNode, result: list) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recursively performs an in-order traversal of the Binary Search Tree.
<br></li>
<li> <a href='#function-find_min'><code>
find_min(self) -> int | float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the minimum value in the Binary Search Tree.
<br></li>
<li> <a href='#function-_min_value_node'><code>
_min_value_node(self, node: TreeNode) -> TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the node with the minimum value in the Binary Search Tree.
<br></li>
<li> <a href='#function-find_max'><code>
find_max(self) -> int | float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the maximum value in the Binary Search Tree.
<br></li>
<li> <a href='#function-_max_value_node'><code>
_max_value_node(self, node: TreeNode) -> TreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the node with the maximum value in the Binary Search Tree.
<br></li>
<li> <a href='#function-find_successor'><code>
find_successor(self, data: int | float) -> int | float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the successor of the node with the specified data in the
    Binary Search Tree.
<br></li>
<li> <a href='#function-find_predecessor'><code>
find_predecessor(self, data: int | float) -> int | float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the predecessor of the node with the specified data in the
    Binary Search Tree.
<br></li>
<li> <a href='#function-is_empty'><code>
is_empty(self) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks if the Binary Search Tree is empty.
<br></li>
<li> <a href='#function-max_height'><code>
max_height(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the maximum height of the tree.
<br></li>
<li> <a href='#function-local_tree'><code>
local_tree(self, node: TreeNode, b: int = 2, deepness: int = 1)
 -> list[int | float]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns the local tree with the node being root and the required
    deepness. Nodes' data is loaded into the list down from root from
    the left to the right. Deepness 1 equals root and its children.
    b is the order of the tree, for the binary it is 2.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a new instance of the BinarySearchTree class.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Inserts a new element with the specified data into the Binary
Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data to be inserted. <br></li>
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
Recursively inserts a new node into the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>root</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Current TreeNode. <br></li>
<li> <strong>new_node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node with the data to be inserted. <br></li>
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
Deletes the node with the specified data from the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data which contains the node to be deleted. <br></li>
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
Recursively deletes the specified node from the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node to be deleted. <br></li>
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
Searches for a node with the specified data in the Binary Search Tree.
In case of value duplicate returns only one node at random.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data which contains inside the node to be searched. <br></li>
</ul>
<h2>Returns</h2>
<em>TreeNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;TreeNode containing the data required or None if such TreeNode was not found. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_search">
<strong>Function</strong>
<code>_search</code></h1>
Recursively searches for a node with the specified data in the
Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>root</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Current TreeNode. <br></li>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data which contains inside the node to be searched. <br></li>
</ul>
<h2>Returns</h2>
<em>TreeNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;TreeNode containing the data required or None if such TreeNode was not found. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-node_height">
<strong>Function</strong>
<code>node_height</code></h1>
Finds the height of the node with value.


<h2>Parameters</h2>
<ul>
<li> <strong>value</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Node data. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Node height. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-in_order_traversal">
<strong>Function</strong>
<code>in_order_traversal</code></h1>
Performs an in-order traversal of the Binary Search Tree and returns
a list of elements.


<h2>Returns</h2>
<em>list[int | float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list of elements in increasing order. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_in_order_traversal_rec">
<strong>Function</strong>
<code>_in_order_traversal_rec</code></h1>
Recursively performs an in-order traversal of the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>root</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Current TreeNode. <br></li>
<li> <strong>result</strong>: <em>list[int | float | None]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list to store result from traversal. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find_min">
<strong>Function</strong>
<code>find_min</code></h1>
Finds the minimum value in the Binary Search Tree.


<h2>Returns</h2>
<em>int | float | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The min if it was found, None otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_min_value_node">
<strong>Function</strong>
<code>_min_value_node</code></h1>
Finds the node with the minimum value in the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The root if the BST. <br></li>
</ul>
<h2>Returns</h2>
<em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;TreeNode containing the minimum value. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find_max">
<strong>Function</strong>
<code>find_max</code></h1>
Finds the maximum value in the Binary Search Tree.


<h2>Returns</h2>
<em>int | float | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum value if it was found, None otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_max_value_node">
<strong>Function</strong>
<code>_max_value_node</code></h1>
Finds the node with the maximum value in the Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The root of the BST. <br></li>
</ul>
<h2>Returns</h2>
<em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The node containing the maximum value. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find_successor">
<strong>Function</strong>
<code>find_successor</code></h1>
Finds the successor of the node with the specified data in the
Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data, successor to which is to be found. <br></li>
</ul>
<h2>Returns</h2>
<em>int | float | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The successor to the data. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find_predecessor">
<strong>Function</strong>
<code>find_predecessor</code></h1>
Finds the predecessor of the node with the specified data in the
Binary Search Tree.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>int | float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The data, predecessor to which is to be found. <br></li>
</ul>
<h2>Returns</h2>
<em>int | float | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The predecessor to the data. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-is_empty">
<strong>Function</strong>
<code>is_empty</code></h1>
Checks if the Binary Search Tree is empty.


<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the BST is empty, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-max_height">
<strong>Function</strong>
<code>max_height</code></h1>
The maximum height of the tree.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The height of the tree. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-local_tree">
<strong>Function</strong>
<code>local_tree</code></h1>
Makes the local tree with the node being root and the required
deepness. Nodes' data is loaded into the list down from root from
the left to the right. Deepness 1 equals root and its children.
b is the order of the tree, for binary it is 2.


<h2>Parameters</h2>
<ul>
<li> <strong>node</strong>: <em>TreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Node to be considered the root one. <br></li>
<li> <strong>b</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The order of the tree. Default is 2. <br></li>
<li> <strong>deepness</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The deepness of the local tree. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int | float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List containing the tree nodes' data. <br>

---