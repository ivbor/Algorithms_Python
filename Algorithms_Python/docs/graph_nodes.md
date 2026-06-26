<h1>Graph Nodes and Edges</h1>
  This module defines a base node class for the graph nodes to inherit from and graph nodes themselves. Also it contains a class where the graph edge is outlined.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-BaseGraphNode'><code>
BaseGraphNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class for graph nodes to inherit from.
<br></li>
<li> <a href='#class-Edge'><code>
Edge
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing the graph edge.
<br></li>
<li> <a href='#class-GraphNode'><code>
GraphNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing the usual graph node.
<br></li>
<li> <a href='#class-WeightedGraphNode'><code>
WeightedGraphNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class representing the graph node with additional support for weights.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-BaseGraphNode">
<strong>Class</strong>
<code>BaseGraphNode</code></h1>
Base Graph Node Class

Represents a base graph node with basic attributes and methods.
This class is intended to be extended by other specific types of
graph nodes.


<h2>Attributes</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index identifier of the node. <br></li>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data associated with the node. <br></li>
<li> <strong>color</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;An integer representing the node color, useful in algorithms like graph coloring. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, index: int, data: Any, color: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize Base Graph Node
<br></li>
<li> <a href='#function-__str__'><code>
__str__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return a string representation of the node's data.
<br></li>
<li> <a href='#function-__repr__'><code>
__repr__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return a string representation of the node.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a BaseGraphNode object.


<h2>Parameters</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index identifier of the node. <br></li>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data associated with the node. <br></li>
<li> <strong>color</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the node. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__str__">
<strong>Function</strong>
<code>__str__</code></h1>
Return a string representation of the node's data.


<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The string representation of the data. <br>

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
<h1 id="class-Edge">
<strong>Class</strong>
<code>Edge</code></h1>
Edge Class

Represents an edge in a graph with attributes to manage weights,
capacities, and flow.


<h2>Attributes</h2>
<ul>
<li> <strong>first_node</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the first node in the edge. <br></li>
<li> <strong>second_node</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the second node in the edge. <br></li>
<li> <strong>weight</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The weight of the edge. <br></li>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The capacity of the edge, used in flow algorithms. <br></li>
<li> <strong>flow</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Current flow through the edge, used in flow algorithms. <br></li>
<li> <strong>color</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Color of the edge, used in certain algorithms for marking. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, first_node: int, second_node: int, weight: float = 1,
capacity: int = 0, flow: int = 0, color: int = 0) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize an Edge object.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize an Edge object.


<h2>Parameters</h2>
<ul>
<li> <strong>first_node</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the first node in the edge. <br></li>
<li> <strong>second_node</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the second node in the edge. <br></li>
<li> <strong>weight</strong>: <em>float, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The weight of the edge. Defaults to 1. <br></li>
<li> <strong>capacity</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The capacity of the edge. Defaults to 0. <br></li>
<li> <strong>flow</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The current flow through the edge. Defaults to 0. <br></li>
<li> <strong>color</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the edge. Defaults to 0. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-GraphNode">
<strong>Class</strong>
<code>GraphNode</code></h1>
Graph Node Class

Represents a graph node with additional functionality to manage edges
and capacities.
Extends BaseGraphNode with edge handling capabilities.


<h2>Attributes</h2>
<ul>
<li> <strong>edges</strong>: <em>dict</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A dictionary of edges where keys are node indices and values are Edge objects. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, index: int, data: Any, edges: list[Edge] = [],
   capacities: list[int] = [], color: int = 0) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize a GraphNode object with edges and capacities.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a GraphNode object with optional edges and capacities.


<h2>Parameters</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index identifier of the node. <br></li>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data associated with the node. <br></li>
<li> <strong>edges</strong>: <em>list[Edge], optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of indices of connected nodes. Defaults to empty list. <br></li>
<li> <strong>capacities</strong>: <em>list[int], optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of capacities corresponding to edges. Defaults to empty list. <br></li>
<li> <strong>color</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the node. Defaults to 0. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the lengths of edges and capacities do not match, indicating an error in input. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-WeightedGraphNode">
<strong>Class</strong>
<code>WeightedGraphNode</code></h1>
Weighted Graph Node Class

Represents a graph node that manages both weights and capacities of edges.
Extends GraphNode to include weights along with the existing attributes.


<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, index: int, data: Any, edges: list[Edge] = [],
   weights: list[float] = [], capacities: list[int] = [],
   color: int = 0) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize a WeightedGraphNode object with weights for the edges.
<br></li>
<li> <a href='#function-Raises
------
KeyError
    If the lengths of edges and weights do not match'><code>
Raises
------
KeyError
    If the lengths of edges and weights do not match.
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a WeightedGraphNode object with optional weights
for the edges.


<h2>Parameters</h2>
<ul>
<li> <strong>index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index identifier of the node. <br></li>
<li> <strong>data</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data associated with the node. <br></li>
<li> <strong>edges</strong>: <em>list[Edge], optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of indices of connected nodes. Defaults to empty list. <br></li>
<li> <strong>weights</strong>: <em>list[float], optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of weights corresponding to edges. Defaults to empty list. <br></li>
<li> <strong>capacities</strong>: <em>list[int], optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of capacities corresponding to edges. Defaults to empty list. <br></li>
<li> <strong>color</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The color of the node. Defaults to 0. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the lengths of edges and weights do not match, indicating an error in input. <br>

---