<h1>Weighted Graph</h1>
  This module implements all necessary for the Weighted Graph structure.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-WeightedGraph'><code>
WeightedGraph
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Advanced graph structure with ability to hold weights for all edges.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-WeightedGraph">
<strong>Class</strong>
<code>WeightedGraph</code></h1>
Weighted Graph Class

Represents a weighted graph structure with basic functionality, weights
assigning and managing, as well as advanced methods to manipulate
and analyze the graph properties.

Space complexity of all methods where time complexity specified is O(V)
because graph is stored as list of vertices.


<h2>Attributes</h2>
<ul>
<li> <strong>negative_edge_weight</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If any of edges in the graph have negative value. For now only Bellman-Ford algorithm depends on it and will not work if this value is True. Default is False. <br></li>
<li> <strong>node_type</strong>: <em>type</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Type of nodes which will be added to the graph. For WeightedGraph it is WeightedGraphNode. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes WeightedGraph.
<br></li>
<li> <a href='#function-add_vertex'><code>
add_vertex(self, *args, **kwargs) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds vertex to the graph.
<br></li>
<li> <a href='#function-add_edge'><code>
add_edge(self, u: int, v: int, *args, **kwargs) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds an edge to the graph from the vertex with an index u to the one
    with an index v. Additional edge properties to be passed straight to
    the edge have to be provided in kwargs with appropriate names. Look
    Edge class in `graph_nodes.py` for more information.
<br></li>
<li> <a href='#function-add_weight'><code>
add_weight(self, u: int, v: int, u_to_v_weight: float = 1) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds weight to the edge.
<br></li>
<li> <a href='#function-remove_edge'><code>
remove_edge(self, u: int, v: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes the edge from the vertex u to the vertex v.
<br></li>
<li> <a href='#function-calculate_element'><code>
calculate_element(self, vertex: int, neighbor: int) -> float
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates an element with coordinates (vertex, neighbor) of the
    adjacency matrix.
<br></li>
<li> <a href='#function-prims_algorithm_mst'><code>
prims_algorithm_mst(self) -> list[tuple[int, int, float]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Constructs a minimum spanning tree (MST) of a graph
    using Prim's algorithm.
<br></li>
<li> <a href='#function-find'><code>
find(self, parent: list[int], i: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds the representative or root of the set containing `i` using
    path compression.
<br></li>
<li> <a href='#function-union'><code>
union(self, parent: list[int], rank: list[int], x: int, y: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Performs the union of two subsets where elements `x` and `y` belong,
    using union by rank.
<br></li>
<li> <a href='#function-kruskals_mst'><code>
kruskals_mst(self) -> list[tuple[int, int, float]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Constructs a minimum spanning tree (MST) of a graph using
    Kruskal's algorithm.
<br></li>
<li> <a href='#function-bellman_ford'><code>
bellman_ford(self, start: int) -> tuple[list[float], dict[int, list[int]]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Error raiser for the main bellman_ford method.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes Weighted Graph.


<h2>Parameters</h2>
<ul>
<li> <strong>negative_edge_weight</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If any of edges in the graph have negative value. For now only Bellman-Ford algorithm depends on it and will not work if this value is True. Default is False. <br></li>
<li> <strong>node_type</strong>: <em>type</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Type of nodes which will be added to the graph. For WeightedGraph it is WeightedGraphNode. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add_vertex">
<strong>Function</strong>
<code>add_vertex</code></h1>
Adds vertex to the graph.


<h2>Parameters</h2>
<ul>
<li> <strong>kwargs['data'] or args[0]</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data to be placed into the vertex. <br></li>
<li> <strong>kwargs['edges'] of args[1]</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of indexes of vertices with which the vertex will be connected. <br></li>
<li> <strong>kwargs['weights'] or args[2]</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of weights. For each edge introduced by previous parameter weight has to be provided with the same index in this list as the appropriate vertex's index in the previous parameter. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add_edge">
<strong>Function</strong>
<code>add_edge</code></h1>
Adds an edge to the graph from the vertex with an index u to the one
with an index v.

Additional edge properties to be passed straight to
the edge have to be provided in kwargs with appropriate names. Look
Edge class in `graph_nodes.py` for more information.


<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge will go from. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge will go to. <br></li>
<li> <strong>kwargs['weights'] or args[0]</strong>: <em>list[float]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of the weights having the weight for this edge under the kwargs['nr'] index. Cannot be provided with kwargs['weight']. The kwargs['nr'] is passed from super() method. <br></li>
<li> <strong>kwargs['weight'] or args[0]</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Weight for the edge. Cannot be provided with kwargs['weights']. <br></li>
<li> <strong>kwargs[...]</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Additional property ... with appropriate value to be passed straight to the edge. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add_weight">
<strong>Function</strong>
<code>add_weight</code></h1>
Adds weight to the edge.


<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge to which weight is added goes from. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge to which weight is added goes to. <br></li>
<li> <strong>u_to_v_weight</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Weight of the edge. Default value is 1 which will be used if the weight is not provided. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-remove_edge">
<strong>Function</strong>
<code>remove_edge</code></h1>
Removes the edge from the vertex u to the vertex v.


<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge goes from. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex the edge goes to. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-calculate_element">
<strong>Function</strong>
<code>calculate_element</code></h1>
Calculates an element with coordinates (vertex, neighbor) of the
adjacency matrix.


<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The row of the element. <br></li>
<li> <strong>neighbor</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The column of the element. <br></li>
</ul>
<h2>Returns</h2>
<em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element of the adjacency matrix with coordinates (vertex, neighbor). <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-prims_algorithm_mst">
<strong>Function</strong>
<code>prims_algorithm_mst</code></h1>
Constructs a minimum spanning tree (MST) of a graph
using Prim's algorithm.
Starts from a randomly chosen vertex and explores edges with
the smallest weight, ensuring that no cycles are formed,
to expand the MST until all vertices are included.


<h2>Returns</h2>
<em>list[tuple[int, int, float]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Each tuple represents an edge in the MST, formatted as (index of the vertex starting the edge, index of the vertex ending the edge, weight of the edge).   <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the graph is empty and no vertices are available to start the algorithm. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-find">
<strong>Function</strong>
<code>find</code></h1>
Finds the representative or root of the set containing
`i` using path compression.


<h2>Parameters</h2>
<ul>
<li> <strong>parent</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Parent array of disjoint set.
i : int Element whose set representative is to be found. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The representative of the set containing `i`. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-union">
<strong>Function</strong>
<code>union</code></h1>
Performs the union of two subsets where elements `x` and `y` belong,
using union by rank.
Union by rank always attaches the tree with smaller height to the
root of the tree with larger height.


<h2>Parameters</h2>
<ul>
<li> <strong>parent</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Parent array of disjoint set. <br></li>
<li> <strong>rank</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Rank array used for union by rank. <br></li>
<li> <strong>x</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Element of the first subset. <br></li>
<li> <strong>y</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Element of the second subset. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-kruskals_mst">
<strong>Function</strong>
<code>kruskals_mst</code></h1>
Constructs a minimum spanning tree (MST) of a graph using
Kruskal's algorithm.
Sorts all edges in non-decreasing order of their weight and picks
the smallest edge, ensuring it does not form a cycle with the MST
formed so far. Repeats until there are V-1 edges in the MST,
where V is the number of vertices in the graph.
Kruskal's algorithm is suitable for graphs represented as
an edge list and works well for sparse graphs.
It relies heavily on a disjoint-set data structure.


<h2>Returns</h2>
<em>list[tuple[int, int, float]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Each tuple represents an edge in the MST, formatted as (from_vertex, to_vertex, weight). <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bellman_ford">
<strong>Function</strong>
<code>bellman_ford</code></h1>
Error raiser for the main bellman_ford method.


<h2>Parameters</h2>
<ul>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex to calculate distances from. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple[list[float], dict[int, list[int]]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Tuple with list and dict inside. In the list to each index, being vertex's index, corresponds the distance between it and start vertex. In the dict to vertices' indexes correspond the shortest paths between these vertices and the starting vertex, both included.   <br>
<h2>Raises</h2>
<strong>ValueError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;For graphs with negative edge weight. <br>

---