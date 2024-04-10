import heapq
import logging

from collections import deque

from Algorithms.python_solutions.graph_nodes import GraphNode, Edge


class VerticesList(dict):

    def __init__(self):
        super().__init__()

    def append(self, __object) -> None:
        self[len(self)] = __object

    def __getitem__(self, index):
        if index not in self.keys():
            raise IndexError(f'there is no index {index} in the list')
        return dict.get(self, index)

    def __iter__(self):
        for elt in self.values():
            yield elt

    def __delitem__(self, index):
        dict.__delitem__(self, index)


class Graph:

    def __init__(self):
        self.vertices = VerticesList()
        self.has_cycles = False
        self.node_type = GraphNode

    def all_vertices(self):
        return [str(vertex) for vertex in self.vertices]

    def add_vertex(self, *args, **kwargs):

        # figure out the index
        if len(self.vertices) == 0:
            index = len(self.vertices)
        else:
            present_indexes = \
                [i for i in self.vertices.keys()]
            missing_vals = set(present_indexes).difference(
                            set([i for i in range(max(present_indexes) + 1)]))
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
            kwargs['nr'] = nr
            if 'data' in kwargs and 'edges' in kwargs:
                self.add_edge(index, edge, *args, **kwargs)
            else:
                args = args[2:]
                self.add_edge(index, edge, *args, **kwargs)

    def _find_arg(self, default, arg_dict: dict[int, str], *args, **kwargs):

        pos = [i for i in arg_dict.keys()][0]
        string = [i for i in arg_dict.values()][0]

        try:
            if len(args) > pos:
                arg = args[pos]
            else:
                arg = kwargs[string]
        except KeyError:
            return default

        return arg

    def _find_index(self, **kwargs):
        if 'data' in kwargs.keys():
            index = \
                [vertex.index for vertex in self.vertices
                 if vertex.data == kwargs['data']][0]
        elif 'index' in kwargs.keys():
            index = kwargs['index']
        else:
            raise TypeError('no index or data specified to remove')
        return index

    def remove_vertex(self, **kwargs):
        index = self._find_index(**kwargs)
        for vertex in self.vertices:
            if index in vertex.edges.keys():
                self.remove_edge(vertex.index, index)
        del self.vertices[index]

    def add_edge(self, u: int, v: int, *args, **kwargs):
        if v not in self.vertices[u].edges.keys():
            self.vertices[u].edges[v] = Edge(u, v, *args, **kwargs)
            capacity = self._find_arg(0, {10: 'capacity'}, *args, **kwargs)
            self.vertices[u].edges[v].capacity = capacity

    def remove_edge(self, u: int, v: int):
        if v in self.vertices[u].edges.keys():
            del self.vertices[u].edges[v]

    def bfs(self, start, target=None):

        to_return = []
        visited = [False] * (
            max([vertex.index for vertex in self.vertices]) + 1)
        predecessor = [None] * (
            max([vertex.index for vertex in self.vertices]) + 1)
        current_row = [start]
        visited[start] = True

        while len(current_row) != 0:
            vertex = current_row[0]
            current_row = current_row[1:]
            if target is not None:
                if vertex == target:
                    current = target
                    while current is not None:
                        to_return.append(current)
                        current = predecessor[current]
                    return to_return[::-1]
            for neighbor in self.vertices[vertex].edges.keys():
                if not visited[neighbor]:
                    current_row.append(neighbor)
                    visited[neighbor] = True
                    predecessor[neighbor] = vertex
        if target is not None:
            raise IndexError(
                f'there is no path between {start} and {target}')

    def to_adjacency_matrix(self):

        matrix_size = len(self.vertices)
        adjacency_matrix = \
            [[0] * matrix_size for _ in range(matrix_size)]

        for vertex in self.vertices:
            for neighbor in vertex.edges.keys():
                adjacency_matrix[vertex.index][neighbor] = \
                    self.calculate_element(vertex.index, neighbor)

        return adjacency_matrix

    def calculate_element(self, vertex, neighbor):
        return 1

    def topological_sort_util(self, vertex, visited, stack):

        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.vertices[vertex].edges.keys():
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        # Push current vertex to stack which stores the result
        stack.insert(0, vertex)

    def topological_sort(self):

        # Step 1: Check for cycles
        if self.is_cyclic():
            raise RecursionError(
                "The graph has a cycle. Topological sort not possible.")

        # Step 2: Perform Topological Sort
        visited = [False] * len(self.vertices)
        stack = []

        for index in [vertex.index for vertex in self.vertices]:
            if not visited[index]:
                self.topological_sort_util(index, visited, stack)

        return stack

    def tarjan_dfs(self, vertex, index, stack, low_link, on_stack, scc):

        # when approach new vertex - assign it the index
        index[vertex] = self.counter
        # and the low-link value (the same one)
        # which will further show node with the lowest index
        # from which it can be accessible
        low_link[vertex] = self.counter
        self.counter += 1

        # add the current node to the current stack
        # which limits segment currently studied for connectivity
        stack.append(vertex)
        # mark the node to be in the current dfs queue
        on_stack[vertex] = True

        for neighbor in self.vertices[vertex].edges.keys():

            # if the neighbor has not been visited yet
            if index[neighbor] == -1:
                # Recursively call DFS on the neighbor
                self.tarjan_dfs(
                    neighbor, index, stack, low_link, on_stack, scc)
                # after calling dfs to calculate low_link value
                # for neighbor update low_link value of the current node
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])
            # if node is on the stack -
            # means that it has been visited earlier in the current dfs
            # but may not be updated as changes may have occurred
            # to the low_link of its neighbors on the deeper dfs iteration
            elif on_stack[neighbor]:
                low_link[vertex] = min(low_link[vertex], low_link[neighbor])

        # now that all nodes which could possibly be visited
        # on the current dfs have their indexes
        # and we can start to search for nodes in the current scc segment

        # if for vertex inside current dfs its low_link value equals to
        # its index - it is the root of the scc segment
        if low_link[vertex] == index[vertex]:
            scc_component = []
            # now - to remove vertices from current stack
            # until the root vertex is reached
            # and save them as scc segment
            while True:
                last_vertex = stack.pop()
                on_stack[last_vertex] = False
                scc_component.append(last_vertex)
                if last_vertex == vertex:
                    break
            scc.append(scc_component)

    def scc(self):

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
                self.tarjan_dfs(vertex, index, stack, low_link, on_stack, scc)

        return scc

    def kosaraju_scc(self):
        """
        Finds strongly connected components in the given directed graph
        using Kosaraju's algorithm.

        Args:
        - graph (DirectedGraph): The directed graph for which to find SCCs.

        Returns:
        - List[List[int]]: A list of lists, where each inner list contains
        the indices of nodes that form a strongly connected component.
        """
        stack = []
        visited = set()

        # Step 1: Fill vertices in stack according to their finishing times
        for vertex in self.vertices:
            if vertex.index not in visited:
                self.fill_order(vertex.index, visited, stack)

        # Step 2: Reverse graph
        reversed_graph = self.reverse_graph()

        # Step 3: Process all vertices in order defined by Stack
        visited.clear()
        sccs = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                scc = []
                self.dfs_util(reversed_graph, vertex, visited, scc)
                sccs.append(scc)

        return sccs

    def fill_order(self, vertex, visited, stack):
        """
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times (meaning the time when all not visited
        vertices accessible from this vertex by transitions with direction 1
        become visited).

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - vertex (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - stack (list): Stack to push vertices according to their
        finishing times.
        """

        visited.add(vertex)

        for neighbor in self.vertices[vertex].edges.keys():
            if neighbor not in visited:
                self.fill_order(neighbor, visited, stack)
        stack.append(vertex)

    def reverse_graph(self):
        """
        Reverses the direction of all edges in the graph.

        Args:
        - graph (DirectedGraph): The graph to reverse.

        Returns:
        - DirectedGraph: A new graph with reversed edges.
        """
        reversed_graph = Graph()
        for vertex in [vertex.index for vertex in self.vertices]:
            reversed_graph.add_vertex(data=self.vertices[vertex].data)

        for vertex in self.vertices:
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

    def dfs_util(self, reversed_graph, vertex, visited, scc):
        """
        A utility function for DFS traversal that tracks
        the strongly connected component.

        Args:
        - graph (DirectedGraph): The graph to perform DFS on.
        - vertex (int): The starting vertex index for DFS.
        - visited (set): Set of visited vertices.
        - scc (list): List to accumulate vertices in the current SCC.
        """
        visited.add(vertex)
        scc.append(vertex)

        for neighbor in reversed_graph.vertices[vertex].edges.keys():
            if neighbor not in visited:
                self.dfs_util(reversed_graph, neighbor, visited, scc)

    def dijkstra(self, start: int):

        # Initialize distances to all nodes as infinity
        distances = \
            [float('inf') for _ in self.vertices]
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

    def is_cyclic_util(self, vertex, visited, rec_stack):

        # Mark the current node as visited
        visited[vertex] = True
        rec_stack[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.vertices[vertex].edges.keys():

            # If the node is not visited then recurse on it
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True

            # If an adjacent vertex is visited and
            # not parent of current vertex, then there is a cycle
            elif rec_stack[neighbor]:
                return True

        rec_stack[vertex] = False
        return False

    def is_cyclic(self):

        # Mark all the vertices as not visited
        visited = [False] * len(self.vertices)
        rec_stack = [False] * len(self.vertices)

        # Call the recursive helper function
        # to detect cycle in different DFS trees
        for index in [vertex.index for vertex in self.vertices]:
            if not visited[index]:
                if self.is_cyclic_util(index, visited, rec_stack):
                    return True

        return False

    def bellman_ford(self, start):

        # Step 1: Initialize distances from start
        # to all other vertices as INFINITE and target to itself as 0.
        # Also, create a parent array to store the shortest path tree

        dist = [float("Inf")] * len(self.vertices)
        dist[start] = 0
        # Parent array to store the path
        parent = [-1] * len(self.vertices)

        # Step 2: Relax all edges |V| - 1 times
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

        # Step 3: Check for negative-weight cycles
        for vertex in self.vertices:
            for neighbor in vertex.edges.keys():
                if dist[vertex.index] != float("Inf") and \
                        dist[vertex.index] + \
                        self.calculate_element(vertex.index, neighbor) < \
                        dist[neighbor]:
                    print("Graph contains negative weight cycle")
                    return None, None

        # Function to reconstruct path from source to j using parent array
        def reconstruct_path(src, j, parent):
            path = []
            while j != -1:
                path.append(j)
                j = parent[j]
            path.reverse()
            return path if path[0] == src else []

        # Reconstruct paths from target to all other vertices
        paths = \
            {vertex.index: reconstruct_path(start, vertex.index, parent)
             for vertex in self.vertices}

        return dist, paths

    def bfs_level_graph(self, source):
        levels = [-1] * len(self.vertices)  # Level of nodes
        levels[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for _, edge in self.vertices[vertex].edges.items():
                # Check capacity and if the level is set
                if edge.capacity - edge.flow > 0 and \
                        levels[edge.second_node] < 0:
                    levels[edge.second_node] = levels[vertex] + 1
                    queue.append(edge.second_node)
        return levels

    def dfs_blocking_flow(self, source, sink, flow, levels):
        if source == sink:
            return flow
        for _, edge in self.vertices[source].edges.items():
            remaining_capacity = edge.capacity - edge.flow
            if remaining_capacity > 0 \
                    and levels[edge.second_node] == levels[source] + 1:
                # Min flow in path
                path_flow = min(flow, remaining_capacity)
                result_flow = \
                    self.dfs_blocking_flow(edge.second_node, sink,
                                           path_flow, levels)
                if result_flow > 0:
                    # Update capacities in the direction TO the sink
                    edge.flow += result_flow
                    # and FROM the sink
                    if source in [i for i in self.vertices[edge.second_node]
                                                 .edges.keys()]:
                        self.vertices[edge.second_node].edges[source]\
                            .flow -= result_flow
                    else:
                        raise KeyError(
                            f'no reverse edge from {edge.second_node} to \
                            {source}')
                    return result_flow
        return 0

    def dinics_algorithm(self, source, sink):
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

    def initialize_preflow(self, source):
        # Height initialization
        for vertex in self.vertices.keys():
            self.vertices[vertex].height = 0
            self.vertices[vertex].excess_flow = 0
        self.vertices[source].height = len(self.vertices)

        # Preflow initialization
        for edge in self.vertices[source].edges.keys():
            # Send max flow
            self.vertices[source].edges[edge].flow = \
                self.vertices[source].edges[edge].capacity
            self.vertices[edge].excess_flow += \
                self.vertices[source].edges[edge].flow
            self.vertices[source].excess_flow -= \
                self.vertices[source].edges[edge].flow

    def push_flow(self, u, v):

        edge = self.vertices[u].edges[v]
        flow = min(self.vertices[u].excess_flow,
                   edge.capacity - edge.flow)
        if flow > 0 and \
                self.vertices[u].height == self.vertices[v].height + 1:
            self.vertices[u].edges[v].flow += flow
            self.vertices[u].excess_flow -= flow
            self.vertices[v].excess_flow += flow
            return True
        return False

    def lift_vertex(self, u):
        min_height = float('inf')
        for edge in self.vertices[u].edges.keys():
            if self.vertices[u].edges[edge].capacity > \
                    self.vertices[u].edges[edge].flow:
                min_height = \
                    min(min_height, self.vertices[edge].height)
        if min_height < float('inf'):
            self.vertices[u].height = min_height + 1

    def discharge_excess_flow(self, u):
        while self.vertices[u].excess_flow > 0:
            for neighbor in self.vertices[u].edges.keys():
                if self.push_flow(u, neighbor):
                    break
            else:
                # No push occurred, lift the vertex
                self.lift_vertex(u)
                # Necessary to prevent infinite loop if no push is possible
                break

    def goldberg_tarjan(self, source, sink):
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
            excess_vertices = \
                [u for u in self.vertices.keys() if u != source and u != sink
                    and self.vertices[u].excess_flow != 0]

        return self.vertices[sink].excess_flow

    def color_vertices(self):
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

    def all_edges(self):
        all_edges = []
        for vertex in self.vertices:
            for _, edge in vertex.edges.items():
                all_edges.append(edge.__dict__)
        return all_edges

    def color_edges(self):
        # Initial implementation based on provided descriptions
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
