<h1>Graph Utility</h1>
  This module defines Graph_util class which has all utility methods for Graph class methods.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-reconstruct_path'><code>
reconstruct_path(src: int, target: int, parent: list[int]) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A function to reconstruct path from source to target using parent array.
```

<br></li>

</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-Graph_util'><code>
Graph_util
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class storing utility methods for the main graph class.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-reconstruct_path">
<strong>Function</strong>
<code>reconstruct_path</code></h1>
Function to reconstruct path from source to target using parent array.

<h2>Parameters</h2>
<ul>
<li> <strong>src</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index of starting vertex. <br></li>
<li> <strong>target</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index of the target vertex. <br></li>
<li> <strong>parent</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where each vertex's index, being the index of the list, has its parent, index of vertex from which it was visited first, being the value in the list. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Path from the start vertex to the target, including both. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Graph_util">
<strong>Class</strong>
<code>Graph_util</code></h1>
Class storing utility methods for the main graph class.

<h2>Methods</h2>
<ul>
<li> <a href='#function-_find_arg'><code>
_find_arg(self, default: Any, arg_dict: dict[int, str], *args, **kwargs)
 -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method for finding arg among args and kwargs provided.
```

<br></li>

<li> <a href='#function-_find_index'><code>
_find_index(self, **kwargs) -> int | None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Method finding index of the vertex to remove among kwargs by data or
index.
```

<br></li>

<li> <a href='#function-is_cyclic_util'><code>
is_cyclic_util(self, vertex: int,
      visited: list[bool], rec_stack: list[bool]) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Utility method which is used by is cyclic method.
```

<br></li>

<li> <a href='#function-topological_sort_util'><code>
topological_sort_util(self, vertex: int,
       visited: list[bool], stack: list[int]) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Utility method which is used by topological sort method.
```

<br></li>

<li> <a href='#function-tarjan_dfs'><code>
tarjan_dfs(self, vertex: int, index: list[int],
     stack: list[int], low_link: list[int], on_stack: list[bool],
     scc: list[list[int]]) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Utility method which is used by tarjan_scc method.
```

<br></li>

<li> <a href='#function-fill_order'><code>
fill_order(self, vertex: int, visited: set[int],
     stack: list[int]) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Utility function for DFS and to fill the stack with vertices
based on their finishing times.
```

<br></li>

<li> <a href='#function-bfs_level_graph'><code>
bfs_level_graph(self, source: int) -> list[int]:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A method to set up levels for vertices for Dinic's algorithms
using BFS.
```

<br></li>

<li> <a href='#function-dfs_blocking_flow'><code>
dfs_blocking_flow(self, source: int, sink: int, flow: int,
       levels: list[int]) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Performs DFS to find a blocking flow in a level graph
from source to sink.
```

<br></li>

<li> <a href='#function-initialize_preflow'><code>
initialize_preflow(self, source: int) -> None:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Initializes heights and preflows for all vertices
for Goldberg-Tarjan's flow calculation algorithm.
```

<br></li>

<li> <a href='#function-push_flow'><code>
push_flow(self, u: int, v: int) -> bool:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
A method to push flow from vertex with index u
to the vertex with index v if push is possible.
```

<br></li>

<li> <a href='#function-lift_vertex'><code>
lift_vertex(self, u: int) -> None:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Increase vertex height by 1.
```

<br></li>

<li> <a href='#function-discharge_excess_flow'><code>
discharge_excess_flow(self, u: int) -> None:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

```
Discharge excess flow down the path to the sink from the vertex.
```

<br></li>

</ul>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_find_arg">
<strong>Function</strong>
<code>_find_arg</code></h1>
Find the required argument among args.

<h2>Parameters</h2>
<ul>
<li> <strong>default</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Value to be returned if the required argument was not provided. <br></li>
<li> <strong>arg_dict</strong>: <em>dict[int, str]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Dictionary where index corresponds to the possible argument position in args, and value - in kwargs. <br></li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The required argument found within args or kwargs or the default value if the argument was not found. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_find_index">
<strong>Function</strong>
<code>_find_index</code></h1>
Find index of the vertex by data or index provided in kwargs
for further removal.

<h2>Parameters</h2>
<ul>
<li> <strong>kwargs['index']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index of the vertex to remove.
or
kwargs['data']: Any Data inside the vertex to remove. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex to remove.   <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If data or index were not found among kwargs. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-is_cyclic_util">
<strong>Function</strong>
<code>is_cyclic_util</code></h1>
Utility method which is used by is cyclic method.

<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex being visited. <br></li>
<li> <strong>visited</strong>: <em>list[bool]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where vertices are marked as visited (True) or not visited (False). <br></li>
<li> <strong>rec_stack</strong>: <em>list[bool]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List used as a stack showing which vertices were visited in the active iteration of the is_cyclic method. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether the cycle was discovered during current iteration. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-topological_sort_util">
<strong>Function</strong>
<code>topological_sort_util</code></h1>
Utility method which is used by topological sort method.

<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex for which the place is being searched. <br></li>
<li> <strong>visited</strong>: <em>list[bool]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where vertices are marked as visited (True) or not visited (False). <br></li>
<li> <strong>stack</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List which stores the result of the sort. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-tarjan_dfs">
<strong>Function</strong>
<code>tarjan_dfs</code></h1>
Utility method which is used by tarjan_scc method.

<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex being visited. <br></li>
<li> <strong>index</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where all vertices are assigned an index based on how early they were visited or -1 if they have not been visited. <br></li>
<li> <strong>stack</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List gathering current scc segment. <br></li>
<li> <strong>low_link</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where all vertices are assigned a low-link value based on the smallest index of visited vertex from which the current one is accessible. Unvisited are assigned -1's. <br></li>
<li> <strong>on_stack</strong>: <em>list[bool]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List showing which vertices are visited in the current dfs queue. <br></li>
<li> <strong>scc</strong>: <em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List of sccs. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-fill_order">
<strong>Function</strong>
<code>fill_order</code></h1>
Utility function for DFS and to fill the stack with vertices
based on their finishing times.

<h2>Parameters</h2>
<ul>
<li> <strong>vertex</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Currently visited vertex. <br></li>
<li> <strong>visited</strong>: <em>set</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Set of visited vertices. <br></li>
<li> <strong>stack</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Stack to push vertices according to their finishing times. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bfs_level_graph">
<strong>Function</strong>
<code>bfs_level_graph</code></h1>
A method to set up levels for vertices for Dinic's algorithms
using BFS.

<h2>Parameters</h2>
<ul>
<li> <strong>source</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Vertex which is the source of the flow. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The list of levels of vertices where indexes are ones of vertices and values are levels. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-dfs_blocking_flow">
<strong>Function</strong>
<code>dfs_blocking_flow</code></h1>
Performs DFS to find a blocking flow in a level graph
from source to sink.

<h2>Parameters</h2>
<ul>
<li> <strong>source</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex from where the flow starts. <br></li>
<li> <strong>sink</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the sink vertex where the flow ends. <br></li>
<li> <strong>flow</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The amount of flow that can potentially be pushed through the path. <br></li>
<li> <strong>levels</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list representing the level graph where levels[i] is the level of vertex i. <br></li>
</ul>
<h2>Returns</h2>
<em>int or float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The amount of flow that was actually pushed from the source to the sink. If no flow is possible, returns 0.   <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If a reverse edge necessary for updating flow does not exist, indicating an inconsistency in the graph's edge management. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-initialize_preflow">
<strong>Function</strong>
<code>initialize_preflow</code></h1>
Initializes heights and preflows for all vertices
for Goldberg-Tarjan's flow calculation algorithm.

<h2>Parameters</h2>
<ul>
<li> <strong>source</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the source vertex in the graph. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-push_flow">
<strong>Function</strong>
<code>push_flow</code></h1>
A method to push flow from vertex with index u
to the vertex with index v if push is possible.

<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex to push from. <br></li>
<li> <strong>v</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex to push to. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether it was possible to push flow. <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-lift_vertex">
<strong>Function</strong>
<code>lift_vertex</code></h1>
Increase vertex height by 1.

<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex which height will be increased. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-discharge_excess_flow">
<strong>Function</strong>
<code>discharge_excess_flow</code></h1>
Discharge excess flow down the path to the sink from the vertex.

<h2>Parameters</h2>
<ul>
<li> <strong>u</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The vertex from which excess flow will be discharged. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

______________________________________________________________________
