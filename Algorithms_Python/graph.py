"""
Graph Module
============

This module contains the main Graph class with basic and some advanced
methods.

Classes
-------
VerticesList
    Advanced dict to be used for storing vertices in the graph.

Graph
    The main graph structure.

"""


import heapq

from typing import Any, Generator

from Algorithms_Python.graph_nodes import GraphNode, Edge
from Algorithms_Python.graph_util \
    import Graph_util, reconstruct_path


class VerticesList(dict):

    def __init__(self) -> None:
        super().__init__()

    def append(self, __object) -> None:
        self[len(self)] = __object

    def __getitem__(self, index) -> Any | None:
        if index not in self.keys():
            raise IndexError(f'there is no index {index} in the list')
        return dict.get(self, index)

    def __iter__(self) -> Generator[Any, Any, None]:
        for elt in self.values():
            yield elt

    def __delitem__(self, index) -> None:
        dict.__delitem__(self, index)


class Graph(Graph_util):
    """
    Graph Class

    Represents a graph structure with basic functionality, as well as advanced
    methods to manipulate and analyze the graph properties.

    Space complexity of all methods where time complexity specified is O(V)
    because graph is stored as list of vertices.

    Attributes
    ----------
    vertices : VerticesList
        A list of vertices in the graph.

    has_cycles : bool
        Switcher to show if the graph contains cycles.
        Initially it is set to False, but updates after the addition of each
        edge.

    node_type : type
        A node class to be used by this graph type.
        For Graph it is GraphNode.

    Methods
    -------
    __init__(self) -> None
        Initialize the graph.

    all_vertices(self) -> list[str]
        Method showing all vertices by data they contain.

    add_vertex(self, *args, **kwargs) -> None
        Adds vertex (node) to the graph.

    remove_vertex(self, **kwargs) -> None
        Method removing vertex by data or index provided in kwargs.

    add_edge(self, u: int, v: int, *args, **kwargs) -> None
        Add edge between from the vertex with index u to the vertex with
        index v.

    remove_edge(self, u: int, v: int) -> None
        Remove edge from the vertex with index u to the vertex with index v.

    bfs(self, start: int, target: int) -> list[int]
        Breadth-first search implementation.
        Returns the path from the start to the target.

    to_adjacency_matrix(self) -> list[list[int]]
        Returns an adjacency matrix of the graph.

    calculate_element(self, vertex: int, neighbor: int) -> int
        Calculates an element with coordinates (vertex, neighbor) of
        adjacency matrix.

    is_cyclic(self) -> bool
        Method discovering whether the graph contains cycles.

    topological_sort(self) -> list[int]
        Perform a topological sort of the graph
        and return a list of vertices in topologically sorted order.

    tarjan_scc(self) -> list[list[int]]
        Find and return all strongly connected components in the graph
        using Tarjan's algorithm.

    reverse_graph(self) -> 'Graph'
        Reverses the direction of all edges in the graph.

    dfs_util(self, reversed_graph: 'Graph', vertex: int,
             visited: set[int], scc: list[list[int]]) -> None
        A utility function for DFS traversal that tracks the strongly
        connected component.

    kosaraju_scc(self) -> list[list[int]]
        Find and return all strongly connected components in the graph
        using Kosaraju's algorithm.

    dijkstra(self, start: int) -> tuple[list[float], dict[int, int]]
        A method to calculate distances from the vertex with index start to
        all other vertices and shortest paths using provided dictionary
        using Dijkstra's algorithm.

    bellman_ford(self, start: int) -> tuple[list[float], dict[int, list[int]]]
        A method to calculate distances from the vertex with index start to
        all other vertices and shortest paths using provided dictionary
        using Bellman-Ford algorithm.

    dinics_algorithm(self, source: int, sink: int) -> int:
        Dinic's algorithm to find the maximum flow
        from a source to a sink in the graph.

    goldberg_tarjan(self, source: int, sink: int) -> int:
        Method implementing the Goldberg-Tarjan's algorithm
        to find the maximum flow from a source to a sink in a flow network.

    color_vertices(self) -> int
        Color the vertices of the graph using a greedy coloring algorithm.

    all_edges(self) -> list[dict[str, Any]]
        Return a list of all edges (in dict form) in the graph.

    color_edges(self) -> int
        Assign colors to edges ensuring no two adjacent edges have
        the same color.

    """

    def __init__(self) -> None:
        """
        Initialize a new Graph object.

        Returns
        -------
        None
        """
        self.vertices = VerticesList()
        self.has_cycles = False
        self.node_type = GraphNode

    def all_vertices(self) -> list[str]:
        """
        Returns a list of all vertices in the graph
        as string representations.

        Returns
        -------
        list[str]
            A list containing string representations of each vertex
            in the graph.
        """
        return [str(vertex) for vertex in self.vertices]

    def add_vertex(self, *args, **kwargs) -> None:
        """
        Adds a vertex to the graph,
        automatically handling the indexing and connections
        based on provided arguments.

        Parameters
        ----------
        kwargs['data'] or args[0]: Any
            Data to be placed into the vertex.

        kwargs['edges'] of args[1]: list[int]
            List of indexes of vertices
            with which the vertex will be connected.

        Returns
        -------
        None
        """
        # figure out and assign the index
        if len(self.vertices) == 0:
            index = len(self.vertices)
        # something is in the graph already
        else:
            # find out which indexes are already assigned
            present_indexes = \
                [i for i in self.vertices.keys()]
            # find out which ones are missing due to possible deletion
            missing_vals = set(present_indexes).difference(
                            set([i for i in range(max(present_indexes) + 1)]))
            # if something is missing - reuse missing index
            # if all filled - use more memory
            if len(missing_vals) != 0:
                index = min(missing_vals)
            else:
                index = max(present_indexes) + 1

        # create the vertex
        new_node = self.node_type(index, *args, **kwargs)
        # add the vertex to the vertices list
        self.vertices[index] = new_node

        # find and connect its edges
        edges = \
            self._find_arg([], {1: 'edges'}, *args, **kwargs)
        for nr, edge in enumerate(edges):
            # pass to kwargs current edge number
            kwargs['nr'] = nr
            # and sort out the available args and kwargs for
            # add_edge method
            if 'data' in kwargs and 'edges' in kwargs:
                self.add_edge(index, edge, *args, **kwargs)
            else:
                args = args[2:]
                self.add_edge(index, edge, *args, **kwargs)

    def remove_vertex(self, **kwargs) -> None:
        """
        Removes a vertex from the graph based on provided index or data.

        Parameters
        ----------
        kwargs['index']: int
            Index of the vertex to remove.
        or
        kwargs['data']: Any
            Data inside the vertex to remove.

        Returns
        -------
        None
        """

        index = self._find_index(**kwargs)
        # first, remove edges from other vertices to this vertex
        for vertex in self.vertices:
            if index in vertex.edges.keys():
                self.remove_edge(vertex.index, index)
        del self.vertices[index]

    def add_edge(self, u: int, v: int, *args, **kwargs) -> None:
        """
        Adds an edge between two vertices, identified by their indices,
        optionally including properties listed below.

        DO NOT USE args FOR PASSING THESE PROPERTIES!
        Args are passed just to make potential future changes
        (additional functionality) easier.

        Parameters
        ----------
        u : int
            The index of the source vertex.

        v : int
            The index of the destination vertex.

        kwargs['capacity']: int
            The capacity of the edge, used in flow algorithms.

        kwargs['flow']: int
            Current flow through the edge, used in flow algorithms.

        kwargs['color']: int
            The number depicting color of the edge.

        Returns
        -------
        None
        """
        if v not in self.vertices[u].edges.keys():
            self.vertices[u].edges[v] = Edge(u, v, *args, **kwargs)
            capacity = self._find_arg(0, {10: 'capacity'}, *args, **kwargs)
            self.vertices[u].edges[v].capacity = capacity

    def remove_edge(self, u: int, v: int) -> None:
        """
        Removes an edge from the graph.

        Parameters
        ----------
        u : int
            The index of the source vertex.

        v : int
            The index of the destination vertex.

        Returns
        -------
        None
        """
        if v in self.vertices[u].edges.keys():
            del self.vertices[u].edges[v]

    def bfs(self, start: int, target: int) -> list[int]:
        """
        Performs a Breadth-First Search (BFS)
        starting from a specified vertex to a target vertex,
        returning the path.

        This function utilizes the shared BFS traversal helper.
        It records each vertex parent in the `after_enter` callback
        and reconstructs the path after traversal.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Parameters
        ----------
        start : int
            The index of the start vertex.

        target : int
            The index of the target vertex.

        Returns
        -------
        list[int]
            A list of vertex indices representing the path
            from start to target.

        Raises
        ------
        IndexError
            If no path exists between the start and target vertices.
        """

        predecessor = [None] * self._vertex_state_size()

        def after_enter(vertex: int, parent: int | None) -> None:
            predecessor[vertex] = parent

        visited = [False] * self._vertex_state_size()
        self._bfs_traverse(start, visited, after_enter=after_enter)

        if target is not None and visited[target]:
            path = []
            current = target
            while current is not None:
                path.append(current)
                current = predecessor[current]
            return path[::-1]

        if target is not None:
            raise IndexError(
                f'there is no path between {start} and {target}')

    def to_adjacency_matrix(self) -> list[list[int]]:
        """
        Finds an adjacency matrix of the graph.

        Returns
        -------
        list[list[int]]
            The adjacency matrix.
        """
        matrix_size = len(self.vertices)
        adjacency_matrix = \
            [[0] * matrix_size for _ in range(matrix_size)]

        for vertex in self.vertices:
            for neighbor in vertex.edges.keys():
                adjacency_matrix[vertex.index][neighbor] = \
                    self.calculate_element(vertex.index, neighbor)

        return adjacency_matrix

    def calculate_element(self, vertex: int, neighbor: int) -> int:
        """
        Calculates an element with coordinates (vertex, neighbor) of the
        adjacency matrix.

        Parameters
        ----------
        vertex: int
            The row of the element.

        neighbor: int
            The column of the element.

        Returns
        -------
        int
            The element of the adjacency matrix with coordinates
            (vertex, neighbor).
        """
        return 1

    def is_cyclic(self) -> bool:
        """
        Method discovering whether the graph contains cycles.

        This function utilizes the shared DFS traversal helper.
        The recursion-stack state is updated with enter and exit callbacks.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Returns
        -------
        bool
            Whether the graph contains cycles.
        """

        # Mark all the vertices as not visited
        visited = [False] * self._vertex_state_size()
        rec_stack = [False] * self._vertex_state_size()

        # Call the recursive helper function
        # to detect cycle in different DFS trees
        for index in [vertex.index for vertex in self.vertices]:
            if not visited[index]:
                if self.is_cyclic_util(index, visited, rec_stack):
                    return True

        return False

    def topological_sort(self) -> list[int]:
        """
        Performs a topological sort of the graph if it is acyclic,
        returning an ordered list of vertex indices.

        This function utilizes the shared DFS traversal helper.
        Each vertex is placed into the output order in the exit callback.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Returns
        -------
        list[int]
            A list of vertex indices in topologically sorted order.

        Raises
        ------
        RecursionError
            If the graph contains cycles, making topological sort impossible.
        """
        # Check for cycles
        if self.is_cyclic():
            raise RecursionError(
                "The graph has a cycle. Topological sort is not possible.")

        # Perform Topological Sort
        visited = [False] * self._vertex_state_size()
        stack = []

        for index in [vertex.index for vertex in self.vertices]:
            if not visited[index]:
                self.topological_sort_util(index, visited, stack)

        return stack

    def tarjan_scc(self) -> list[list[int]]:
        """
        Finds all strongly connected components in the graph
        using Tarjan's algorithm.

        This function utilizes DFS with low-link updates. It is not routed
        through the shared traversal helper because Tarjan's algorithm needs
        edge-specific state updates after recursive child calls return.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Returns
        -------
        list[list[int]]
            A list of lists, where each sublist represents
            a strongly connected component.
        """

        # counter for indexes
        self.counter = 0
        # arrays of indexes and low_link values
        index = [-1] * len(self.vertices)
        low_link = [-1] * len(self.vertices)
        # array showing which of vertices are in the current dfs queue
        on_stack = [False] * len(self.vertices)
        # stack limiting segment of the graph being studied for scc
        stack = []
        # array with all found scc segments
        scc = []

        for vertex in [vertex.index for vertex in self.vertices]:
            if index[vertex] == -1:
                self.tarjan_dfs(vertex, index, stack,
                                low_link, on_stack, scc)

        return scc

    def reverse_graph(self) -> 'Graph':
        """
        Reverses the direction of all edges in the graph.

        Time complexity: O(V + E)

        Returns
        -------
        Graph
            A new graph with reversed edges.
        """
        reversed_graph = Graph()
        for vertex in [vertex.index for vertex in self.vertices]:
            reversed_graph.add_vertex(data=self.vertices[vertex].data)

        for vertex in [vertex for vertex in self.vertices]:
            for neighbor in vertex.edges.keys():
                # copy params
                edge_params = vertex.edges[neighbor].__dict__
                # flip start and finish
                # by deleting them
                del edge_params['first_node']
                del edge_params['second_node']
                # and reassigning again
                reversed_graph.add_edge(neighbor, vertex.index, **edge_params)
                # Reversing the edge direction

        return reversed_graph

    def dfs_util(self, reversed_graph: 'Graph', vertex: int,
                 visited: set[int], scc: list[list[int]]) -> None:
        """
        A utility function for DFS traversal that tracks
        the strongly connected component.

        This function utilizes the shared DFS traversal helper on the
        reversed graph. It collects the current strongly connected component
        in the `after_enter` callback.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Parameters
        ----------
        vertex: int
            The starting vertex index for DFS.

        visited: set
            Set of visited vertices.

        scc: list[list[int]]
            List to accumulate vertices in the current SCC.

        Returns
        -------
        None
        """
        visited_list = [False] * reversed_graph._vertex_state_size()
        for node in visited:
            visited_list[node] = True

        def after_enter(node: int, parent: int | None) -> None:
            visited.add(node)
            scc.append(node)

        reversed_graph._dfs_traverse(
            vertex, visited_list, after_enter=after_enter)

    def kosaraju_scc(self) -> list[list[int]]:
        """
        Finds strongly connected components in the given directed graph
        using Kosaraju's algorithm.

        The two DFS passes are routed through the shared DFS traversal
        helper: the first pass records finish order and the second pass
        collects components in the reversed graph.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Returns
        -------
        list[list[int]]
            A list of lists, where each inner list contains
            the indices of nodes that form a strongly connected component.
        """

        stack = []
        visited = set()

        # Fill vertices in stack according to their finishing times
        for vertex in self.vertices:
            if vertex.index not in visited:
                self.fill_order(vertex.index, visited, stack)

        # Reverse graph
        reversed_graph = self.reverse_graph()

        # Process all vertices in order defined by Stack
        visited.clear()
        sccs = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                scc = []
                self.dfs_util(reversed_graph, vertex, visited, scc)
                sccs.append(scc)

        return sccs

    def dijkstra(self, start: int) -> tuple[list[float], dict[int, int]]:
        """
        A method to calculate distances from the vertex with index start to
        all other vertices and shortest paths using provided dictionary
        using Dijkstra's algorithm.

        Time complexity: O((V + E) * log V)

        Time complexity comes from the following facts:
            - while acts as for cycle going through all vertices making
            while-for section O(V + E);
            - additional heappush operation within while-for performs in
            log V time.

        Parameters
        ----------
        start: int
            Vertex to calculate distances from.

        Returns
        -------
        tuple[list[float], dict[int, int]]
            Tuple with list and dict inside. In the list to each index, being
            vertex's index, corresponds the distance between it and start
            vertex. In the dict to vertices' indexes correspond the closest
            vertices.
        """

        # Initialize distances to all nodes as infinity
        distances = \
            [float('inf') for _ in range(len(self.vertices))]
        # Set distance to start node as 0
        distances[start] = 0
        # Priority queue to store nodes to visit
        priority_queue = [(0, start)]
        current_distances = {start: 0}

        while priority_queue:
            # Pop the node with the smallest distance from the priority queue
            current_distance, current_node = heapq.heappop(priority_queue)
            # If the current distance is greater than the recorded distance,
            # skip
            if current_distance > distances[current_node]:
                continue

            # Visit each neighbor of the current node
            for neighbor in self.vertices[current_node].edges.keys():
                distance = current_distance + \
                    self.calculate_element(current_node, neighbor)
                # If the new distance is shorter,
                # update it and add to the priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    current_distances[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, current_distances

    def bellman_ford(self, start: int) \
            -> tuple[list[float], dict[int, list[int]]]:
        """
        A method to calculate distances from the vertex with index start to
        all other vertices and shortest paths using provided dictionary
        using Bellman-Ford algorithm.

        Time complexity: O(V * E)

        Parameters
        ----------
        start: int
            Vertex to calculate distances from.

        Returns
        -------
        tuple[list[float], dict[int, list[int]]]
            Tuple with list and dict inside. In the list to each index, being
            vertex's index, corresponds the distance between it and start
            vertex. In the dict to vertices' indexes correspond the shortest
            paths between these vertices and the starting vertex,
            both included.
        """

        # Initialize distances from start
        # to all other vertices as INFINITE and target to itself as 0.
        # Also, create a parent array to store the shortest path tree
        dist = [float("Inf")] * len(self.vertices)
        dist[start] = 0
        parent = [-1] * len(self.vertices)

        # Relax all edges |V| - 1 times
        for _ in range(len(self.vertices) - 1):
            for vertex in self.vertices:
                for neighbor in vertex.edges.keys():
                    if dist[vertex.index] != float("Inf") and \
                            dist[vertex.index] + \
                            self.calculate_element(vertex.index, neighbor) < \
                            dist[neighbor]:
                        dist[neighbor] = dist[vertex.index] + \
                            self.calculate_element(vertex.index, neighbor)
                        parent[neighbor] = vertex.index

        # Reconstruct paths from target to all other vertices
        paths = \
            {vertex.index: reconstruct_path(start, vertex.index, parent)
                for vertex in self.vertices}

        return dist, paths

    def dinics_algorithm(self, source: int, sink: int) -> int:
        """
        Dinic's algorithm to find the maximum flow
        from a source to a sink in the graph.

        This function uses two major processes in a loop:
        first, it constructs a level graph using BFS to determine
        the shortest paths from the source in terms of the number of edges.
        Then, it attempts to find blocking flows in this level graph
        using DFS until no more augmenting paths are found
        in the level graph.

        Time complexity: O(V * E ** 2)

        Parameters
        ----------
        source : int
            The index of the source vertex in the graph.

        sink : int
            The index of the sink vertex in the graph.

        Returns
        -------
        int
            The maximum flow from the source to the sink.
        """

        max_flow = 0
        while True:
            levels = self.bfs_level_graph(source)
            if levels[sink] == -1:
                break  # No path
            while True:
                flow = \
                    self.dfs_blocking_flow(source, sink, float('inf'), levels)
                if flow == 0:
                    break
                max_flow += flow
        return max_flow

    def goldberg_tarjan(self, source: int, sink: int) -> int:
        """
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

        Time complexity: O(E * V ** 2)

        Parameters
        ----------
        source: int
            The index of the source vertex.

        sink: int
            The index of the sink vertex.

        Returns
        -------
        int
            The maximum flow value from the source to the sink in the network.
        """
        self.initialize_preflow(source)

        active_vertices = \
            [u for u in self.vertices.keys() if u != source and u != sink]
        excess_vertices = \
            [u for u in self.vertices.keys() if u != source and u != sink
             and self.vertices[u].excess_flow != 0]
        while active_vertices or excess_vertices:
            if len(active_vertices) == 0:
                u = excess_vertices.pop(0)
            else:
                u = active_vertices.pop(0)
            old_height = self.vertices[u].height
            self.discharge_excess_flow(u)
            if self.vertices[u].height > old_height:
                # Re-add to the list if the height was increased
                active_vertices = [u] + active_vertices
            # check for vertices left with an excess flow
            excess_vertices = \
                [u for u in self.vertices.keys() if u != source and u != sink
                    and self.vertices[u].excess_flow != 0]

        return self.vertices[sink].excess_flow

    def color_vertices(self) -> int:
        """
        Color the vertices of the graph using a greedy coloring algorithm.

        Returns
        -------
        int
            Chromatic number of the graph.
        """
        # Initialize all vertices as unassigned
        vertex_colors = \
            {vertex.index: -1 for vertex in self.vertices}
        available_colors = [False] * len(self.vertices)

        # Assign colors to the remaining vertices
        for vertex in self.vertices:
            # Process all adjacent vertices
            # and flag their colors as unavailable
            for adj in vertex.edges.keys():
                if vertex_colors[adj] != -1:
                    available_colors[vertex_colors[adj]] = True

            # Find the first available color
            color = 0
            while color < len(self.vertices):
                if not available_colors[color]:
                    break
                color += 1

            # Assign the found color
            vertex_colors[vertex.index] = color

            # Reset the availability for the next iteration
            for adj in vertex.edges.keys():
                if vertex_colors[adj] != -1:
                    available_colors[vertex_colors[adj]] = False

        # Apply assigned colors
        for vertex in self.vertices:
            vertex.color = vertex_colors[vertex.index]

        return max([i for i in vertex_colors.values()]) + 1

    def all_edges(self) -> list[dict[str, Any]]:
        """
        Return a list of all edges in the graph.

        Returns
        -------
        list[dict[str, Any]]
            List containing edges in the form of the dict where key is
            edge's attribute and the value is the value of that attribute.
        """
        all_edges = []
        for vertex in self.vertices:
            for _, edge in vertex.edges.items():
                all_edges.append(edge.__dict__)
        return all_edges

    def color_edges(self) -> int:
        """
        Assign colors to edges ensuring no two adjacent edges have
        the same color.

        Returns
        -------
        int
            Chromatic number of the graph but for edges.
        """

        all_edges = self.all_edges()
        available_colors = [True] * len(all_edges)

        for vertex in self.vertices:
            for edge in vertex.edges.values():
                # Reset availability for each edge
                available_colors = \
                    [True] * len(available_colors)
                # Check colors of adjacent edges
                for adj_vertex in self.vertices:
                    # first_node is vertex
                    if adj_vertex.index == edge.second_node:
                        for adj_edge in adj_vertex.edges.values():
                            if adj_edge.color != 0:
                                available_colors[adj_edge.color - 1] = False
                # Find the first available color
                for color, available in enumerate(available_colors, start=1):
                    if available:
                        edge.color = color
                        break

        return max([edge.color for vertex in self.vertices
                    for edge in vertex.edges.values()])
