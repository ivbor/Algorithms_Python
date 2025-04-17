<h1>Graph Module</h1>
  This module contains the main Graph class with basic and some advanced methods.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-VerticesList'><code>
VerticesList
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Advanced dict to be used for storing vertices in the graph.
<br></li>
<li> <a href='#class-Graph'><code>
Graph
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    The main graph structure.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Graph">
<strong>Class</strong>
<code>Graph</code></h1>
Graph Class

Represents a graph structure with basic functionality, as well as advanced
methods to manipulate and analyze the graph properties.

Space complexity of all methods where time complexity specified is O(V)
because graph is stored as list of vertices.

<h2>Attributes</h2>
<ul>
<li> <strong>vertices</strong>: <em>VerticesList</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of vertices in the graph. <br></li>
<li> <strong>has_cycles</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Switcher to show if the graph contains cycles. Initially it is set to False, but updates after the addition of each edge. <br></li>
<li> <strong>node_type</strong>: <em>type</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A node class to be used by this graph type. For Graph it is GraphNode. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Initialize the graph.
```

<br></li>

<li> <a href='#function-all_vertices'><code>
all_vertices(self) -> list[str]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method showing all vertices by data they contain.
```

<br></li>

<li> <a href='#function-add_vertex'><code>
add_vertex(self, *args, **kwargs) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Adds vertex (node) to the graph.
```

<br></li>

<li> <a href='#function-remove_vertex'><code>
remove_vertex(self, **kwargs) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method removing vertex by data or index provided in kwargs.
```

<br></li>

<li> <a href='#function-add_edge'><code>
add_edge(self, u: int, v: int, *args, **kwargs) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Add edge between from the vertex with index u to the vertex with
index v.
```

<br></li>

<li> <a href='#function-remove_edge'><code>
remove_edge(self, u: int, v: int) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Remove edge from the vertex with index u to the vertex with index v.
```

<br></li>

<li> <a href='#function-bfs'><code>
bfs(self, start: int, target: int) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Breadth-first search implementation.
Returns the path from the start to the target.
```

<br></li>

<li> <a href='#function-to_adjacency_matrix'><code>
to_adjacency_matrix(self) -> list[list[int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Returns an adjacency matrix of the graph.
```

<br></li>

<li> <a href='#function-calculate_element'><code>
calculate_element(self, vertex: int, neighbor: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Calculates an element with coordinates (vertex, neighbor) of
adjacency matrix.
```

<br></li>

<li> <a href='#function-is_cyclic'><code>
is_cyclic(self) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method discovering whether the graph contains cycles.
```

<br></li>

<li> <a href='#function-topological_sort'><code>
topological_sort(self) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Perform a topological sort of the graph
and return a list of vertices in topologically sorted order.
```

<br></li>

<li> <a href='#function-tarjan_scc'><code>
tarjan_scc(self) -> list[list[int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Find and return all strongly connected components in the graph
using Tarjan's algorithm.
```

<br></li>

<li> <a href='#function-reverse_graph'><code>
reverse_graph(self) -> 'Graph'
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Reverses the direction of all edges in the graph.
```

<br></li>

<li> <a href='#function-dfs_util'><code>
dfs_util(self, reversed_graph: 'Graph', vertex: int,
   visited: set[int], scc: list[list[int]]) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A utility function for DFS traversal that tracks the strongly
connected component.
```

<br></li>

<li> <a href='#function-kosaraju_scc'><code>
kosaraju_scc(self) -> list[list[int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Find and return all strongly connected components in the graph
using Kosaraju's algorithm.
```

<br></li>

<li> <a href='#function-dijkstra'><code>
dijkstra(self, start: int) -> tuple[list[float], dict[int, int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A method to calculate distances from the vertex with index start to
all other vertices and shortest paths using provided dictionary
using Dijkstra's algorithm.
```

<br></li>

<li> <a href='#function-bellman_ford'><code>
bellman_ford(self, start: int) -> tuple[list[float], dict[int, list[int]]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A method to calculate distances from the vertex with index start to
all other vertices and shortest paths using provided dictionary
using Bellman-Ford algorithm.
```

<br></li>

<li> <a href='#function-dinics_algorithm'><code>
dinics_algorithm(self, source: int, sink: int) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Dinic's algorithm to find the maximum flow
from a source to a sink in the graph.
```

<br></li>

<li> <a href='#function-goldberg_tarjan'><code>
goldberg_tarjan(self, source: int, sink: int) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method implementing the Goldberg-Tarjan's algorithm
to find the maximum flow from a source to a sink in a flow network.
```

<br></li>

<li> <a href='#function-color_vertices'><code>
color_vertices(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Color the vertices of the graph using a greedy coloring algorithm.
```

<br></li>

<li> <a href='#function-all_edges'><code>
all_edges(self) -> list[dict[str, Any]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Return a list of all edges (in dict form) in the graph.
```

<br></li>

<li> <a href='#function-color_edges'><code>
color_edges(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Assign colors to edges ensuring no two adjacent edges have
the same color.
```

<br></li>

</ul>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a new Graph object.

<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-all_vertices">
<strong>Function</strong>
<code>all_vertices</code></h1>

<h2>Returns</h2>
<em></em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Returns ------- list[str] A list containing string representations of each vertex in the graph. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add_vertex">
<strong>Function</strong>
<code>add_vertex</code></h1>
Adds a vertex to the graph,
automatically handling the indexing and connections
based on provided arguments.

<h2>Parameters</h2>
<ul>
<li> <strong>kwargs['data'] or args[0]</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Data to be placed into the vertex. <br></li>
<li> <strong>kwargs['edges'] of args[1]</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of indexes of vertices with which the vertex will be connected. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-remove_vertex">
<strong>Function</strong>
<code>remove_vertex</code></h1>
Removes a vertex from the graph based on provided index or data.

<h2>Parameters</h2>
<ul>
<li> <strong>kwargs['index']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index of the vertex to remove.
or
kwargs['data']: Any Data inside the vertex to remove. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add_edge">
<strong>Function</strong>
<code>add_edge</code></h1>
Adds an edge between two vertices, identified by their indices,
optionally including properties listed below.

DO NOT USE args FOR PASSING THESE PROPERTIES!
Args are passed just to make potential future changes
(additional functionality) easier.

<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the destination vertex. <br></li>
<li> <strong>kwargs['capacity']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The capacity of the edge, used in flow algorithms. <br></li>
<li> <strong>kwargs['flow']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Current flow through the edge, used in flow algorithms. <br></li>
<li> <strong>kwargs['color']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number depicting color of the edge. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-remove_edge">
<strong>Function</strong>
<code>remove_edge</code></h1>
Removes an edge from the graph.

<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the destination vertex. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bfs">
<strong>Function</strong>
<code>bfs</code></h1>
Performs a Breadth-First Search (BFS)
starting from a specified vertex to a target vertex,
returning the path.

This function utilizes BFS.
Time complexity: O(V + E)
Space complexity: O(V)

<h2>Parameters</h2>
<ul>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the start vertex. <br></li>
<li> <strong>target</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the target vertex. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of vertex indices representing the path from start to target.   <br>
<h2>Raises</h2>
<strong>IndexError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If no path exists between the start and target vertices. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_adjacency_matrix">
<strong>Function</strong>
<code>to_adjacency_matrix</code></h1>
Finds an adjacency matrix of the graph.

<h2>Returns</h2>
<em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The adjacency matrix. <br>

______________________________________________________________________

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
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element of the adjacency matrix with coordinates (vertex, neighbor). <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-is_cyclic">
<strong>Function</strong>
<code>is_cyclic</code></h1>
Method discovering whether the graph contains cycles.

This function utilizes DFS.
Time complexity: O(V + E)

<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the graph contains cycles. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-topological_sort">
<strong>Function</strong>
<code>topological_sort</code></h1>
Performs a topological sort of the graph if it is acyclic,
returning an ordered list of vertex indices.

This function utilizes DFS.
Time complexity: O(V + E)

<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of vertex indices in topologically sorted order.   <br>
<h2>Raises</h2>
<strong>RecursionError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If the graph contains cycles, making topological sort impossible. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tarjan_scc">
<strong>Function</strong>
<code>tarjan_scc</code></h1>
Finds all strongly connected components in the graph
using Tarjan's algorithm.

This function utilizes DFS.
Time complexity: O(V + E)

<h2>Returns</h2>
<em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of lists, where each sublist represents a strongly connected component. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-reverse_graph">
<strong>Function</strong>
<code>reverse_graph</code></h1>
Reverses the direction of all edges in the graph.

Time complexity: O(V + E)

<h2>Returns</h2>
<em>Graph</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A new graph with reversed edges. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-dfs_util">
<strong>Function</strong>
<code>dfs_util</code></h1>
A utility function for DFS traversal that tracks
the strongly connected component.

This function utilizes DFS.
Time complexity: O(V + E)

<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The starting vertex index for DFS. <br></li>
<li> <strong>visited</strong>: <em>set</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Set of visited vertices. <br></li>
<li> <strong>scc</strong>: <em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List to accumulate vertices in the current SCC. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-kosaraju_scc">
<strong>Function</strong>
<code>kosaraju_scc</code></h1>
Finds strongly connected components in the given directed graph
using Kosaraju's algorithm.

Time complexity: O(V + E)

<h2>Returns</h2>
<em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of lists, where each inner list contains the indices of nodes that form a strongly connected component. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-dijkstra">
<strong>Function</strong>
<code>dijkstra</code></h1>
A method to calculate distances from the vertex with index start to
all other vertices and shortest paths using provided dictionary
using Dijkstra's algorithm.

Time complexity: O((V + E) * log V)

Time complexity comes from the following facts:
\- while acts as for cycle going through all vertices making
while-for section O(V + E);
\- additional heappush operation within while-for performs in
log V time.

<h2>Parameters</h2>
<ul>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex to calculate distances from. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple[list[float], dict[int, int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Tuple with list and dict inside. In the list to each index, being vertex's index, corresponds the distance between it and start vertex. In the dict to vertices' indexes correspond the closest vertices. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bellman_ford">
<strong>Function</strong>
<code>bellman_ford</code></h1>
A method to calculate distances from the vertex with index start to
all other vertices and shortest paths using provided dictionary
using Bellman-Ford algorithm.

Time complexity: O(V * E)

<h2>Parameters</h2>
<ul>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex to calculate distances from. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple[list[float], dict[int, list[int]]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Tuple with list and dict inside. In the list to each index, being vertex's index, corresponds the distance between it and start vertex. In the dict to vertices' indexes correspond the shortest paths between these vertices and the starting vertex, both included. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-dinics_algorithm">
<strong>Function</strong>
<code>dinics_algorithm</code></h1>
Dinic's algorithm to find the maximum flow
from a source to a sink in the graph.

This function uses two major processes in a loop:
first, it constructs a level graph using BFS to determine
the shortest paths from the source in terms of the number of edges.
Then, it attempts to find blocking flows in this level graph
using DFS until no more augmenting paths are found
in the level graph.

Time complexity: O(V * E \*\* 2)

<h2>Parameters</h2>
<ul>
<li> <strong>source</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex in the graph. <br></li>
<li> <strong>sink</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the sink vertex in the graph. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum flow from the source to the sink. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-goldberg_tarjan">
<strong>Function</strong>
<code>goldberg_tarjan</code></h1>
Method implementing the Goldberg-Tarjan's algorithm
to find the maximum flow from a source to a sink in a flow network.

This method uses the preflow-push (or push-relabel) approach,
which initializes a preflow that exceeds the flow demands
and then adjusts to find the max flow by moving excess flow
from the source towards the sink via allowable paths,
modifying vertex heights and relabeling vertices as necessary
to maintain feasibility.
The function repeatedly processes active vertices
(those with excess flow and not equal to the source or sink)
by trying to push this excess flow towards the sink.
If no flow can be pushed, the function relabels the vertex
(increases its height) to create new allowable paths
in future iterations.

Time complexity: O(E * V \*\* 2)

<h2>Parameters</h2>
<ul>
<li> <strong>source</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex. <br></li>
<li> <strong>sink</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the sink vertex. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum flow value from the source to the sink in the network. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-color_vertices">
<strong>Function</strong>
<code>color_vertices</code></h1>
Color the vertices of the graph using a greedy coloring algorithm.

<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Chromatic number of the graph. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-all_edges">
<strong>Function</strong>
<code>all_edges</code></h1>
Return a list of all edges in the graph.

<h2>Returns</h2>
<em>list[dict[str, Any]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List containing edges in the form of the dict where key is edge's attribute and the value is the value of that attribute. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-color_edges">
<strong>Function</strong>
<code>color_edges</code></h1>
Assign colors to edges ensuring no two adjacent edges have
the same color.

<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Chromatic number of the graph but for edges. <br>

______________________________________________________________________
