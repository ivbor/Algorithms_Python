"""
Graph Utility
=============

This module defines Graph_util class which has all utility methods for Graph
class methods.

Functions
---------
reconstruct_path(src: int, target: int, parent: list[int]) -> list[int]
    A function to reconstruct path from source to target using parent array.

Classes
-------
Graph_util
    A class storing utility methods for the main graph class, including
    callback-based BFS and DFS traversal helpers.

"""


from typing import Any, Callable
from collections import deque


TraversalCallback = Callable[[int, int | None], bool | None]


def reconstruct_path(src: int, target: int, parent: list[int]) -> list[int]:
    """
    Function to reconstruct path from source to target using parent array.

    Parameters
    ----------
    src: int
        Index of starting vertex.

    target: int
        Index of the target vertex.

    parent: list[int]
        List where each vertex's index, being the index of the list,
        has its parent, index of vertex from which it was visited first,
        being the value in the list.

    Returns
    -------
    list[int]
        Path from the start vertex to the target, including both.
    """
    path = []
    while target != -1:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path if path[0] == src else []


class Graph_util:
    """
    Class storing utility methods for the main graph class.

    The shared traversal invariant is:
    `before_enter(vertex, parent)` is called before a candidate vertex is
    accepted, `after_enter(vertex, parent)` is called after it is marked
    visited, `before_exit(vertex, parent)` is called after its outgoing
    neighbors are processed, and `after_exit(vertex, parent)` is called at
    the end of the vertex lifecycle. Returning False from a callback stops
    that branch or traversal step.

    The helpers fit algorithms whose state can be updated on vertex
    discovery or vertex finish, such as path reconstruction, cycle detection,
    topological sorting, and Kosaraju DFS passes.

    Methods
    -------
    _vertex_state_size(self) -> int
        Return one greater than the greatest present vertex index.

    _run_callback(self, callback: TraversalCallback | None,
                  vertex: int, parent: int | None) -> bool
        Run a traversal callback and convert its result to a continue flag.

    _dfs_traverse(self, start: int, visited: list[bool],
                  before_enter: TraversalCallback | None = None,
                  after_enter: TraversalCallback | None = None,
                  before_exit: TraversalCallback | None = None,
                  after_exit: TraversalCallback | None = None,
                  parent: int | None = None) -> None
        Depth-first traversal with uniform lifecycle callbacks.

    _bfs_traverse(self, start: int, visited: list[bool],
                  before_enter: TraversalCallback | None = None,
                  after_enter: TraversalCallback | None = None,
                  before_exit: TraversalCallback | None = None,
                  after_exit: TraversalCallback | None = None) -> None
        Breadth-first traversal with uniform lifecycle callbacks.

    _find_arg(self, default: Any, arg_dict: dict[int, str], *args, **kwargs)
        -> Any
        Method for finding arg among args and kwargs provided.

    _find_index(self, **kwargs) -> int | None
        Method finding index of the vertex to remove among kwargs by data or
        index.

    is_cyclic_util(self, vertex: int,
                   visited: list[bool], rec_stack: list[bool]) -> bool
        Utility method which is used by is cyclic method.

    topological_sort_util(self, vertex: int,
                          visited: list[bool], stack: list[int]) -> None
        Utility method which is used by topological sort method.

    tarjan_dfs(self, vertex: int, index: list[int],
               stack: list[int], low_link: list[int], on_stack: list[bool],
               scc: list[list[int]]) -> None
        Utility method which is used by tarjan_scc method.

    fill_order(self, vertex: int, visited: set[int],
               stack: list[int]) -> None
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times.

    bfs_level_graph(self, source: int) -> list[int]:
        A method to set up levels for vertices for Dinic's algorithms
        using BFS.

    dfs_blocking_flow(self, source: int, sink: int, flow: int,
                      levels: list[int]) -> int:
        Performs DFS to find a blocking flow in a level graph
        from source to sink.

    initialize_preflow(self, source: int) -> None:
        Initializes heights and preflows for all vertices
        for Goldberg-Tarjan's flow calculation algorithm.

    push_flow(self, u: int, v: int) -> bool:
        A method to push flow from vertex with index u
        to the vertex with index v if push is possible.

    lift_vertex(self, u: int) -> None:
        Increase vertex height by 1.

    discharge_excess_flow(self, u: int) -> None:
        Discharge excess flow down the path to the sink from the vertex.
    """

    def _vertex_state_size(self) -> int:
        """
        Return a size that can index every currently present vertex.

        Time complexity: O(V)
        Space complexity: O(1)

        Returns
        -------
        int
            One greater than the greatest present vertex index.
        """
        if len(self.vertices) == 0:
            return 0
        return max(vertex.index for vertex in self.vertices) + 1

    def _run_callback(self, callback: TraversalCallback | None,
                      vertex: int, parent: int | None) -> bool:
        """
        Run a traversal callback if one was provided.

        Time complexity: O(1) plus callback time.
        Space complexity: O(1) plus callback space.

        Parameters
        ----------
        callback: TraversalCallback | None
            Callback to run. If None, traversal continues.

        vertex: int
            Current vertex index.

        parent: int | None
            Parent vertex index or None for the root.

        Returns
        -------
        bool
            Whether traversal should continue for the current candidate.
        """
        if callback is None:
            return True
        result = callback(vertex, parent)
        return result is not False

    def _dfs_traverse(self, start: int, visited: list[bool],
                      before_enter: TraversalCallback | None = None,
                      after_enter: TraversalCallback | None = None,
                      before_exit: TraversalCallback | None = None,
                      after_exit: TraversalCallback | None = None,
                      parent: int | None = None) -> None:
        """
        Depth-first traversal with uniform lifecycle callbacks.

        `before_enter` is called for every candidate vertex before the
        visited check. The other callbacks run only for newly entered
        vertices.

        Time complexity: O(V + E) plus callback time.
        Space complexity: O(V) for recursion depth and the visited list.

        Parameters
        ----------
        start: int
            Vertex from which traversal starts.

        visited: list[bool]
            List where indexes are vertex indexes and values show whether
            the vertex has been entered.

        before_enter: TraversalCallback | None
            Callback run before a candidate vertex is entered.

        after_enter: TraversalCallback | None
            Callback run after a vertex is marked visited.

        before_exit: TraversalCallback | None
            Callback run after neighbors are processed and before exit.

        after_exit: TraversalCallback | None
            Callback run after the vertex exits.

        parent: int | None
            Parent vertex index or None for the root.

        Returns
        -------
        None
        """
        if not self._run_callback(before_enter, start, parent):
            return
        if visited[start]:
            return

        visited[start] = True
        if not self._run_callback(after_enter, start, parent):
            return

        for neighbor in self.vertices[start].edges.keys():
            self._dfs_traverse(
                neighbor, visited, before_enter, after_enter,
                before_exit, after_exit, start)

        if not self._run_callback(before_exit, start, parent):
            return
        self._run_callback(after_exit, start, parent)

    def _bfs_traverse(self, start: int, visited: list[bool],
                      before_enter: TraversalCallback | None = None,
                      after_enter: TraversalCallback | None = None,
                      before_exit: TraversalCallback | None = None,
                      after_exit: TraversalCallback | None = None) -> None:
        """
        Breadth-first traversal with uniform lifecycle callbacks.

        `before_enter` is called before a candidate is accepted into the
        queue. `after_enter` is called when it is marked visited.
        `before_exit` and `after_exit` are called after the vertex is popped
        and its outgoing neighbors have been processed.

        Time complexity: O(V + E) plus callback time.
        Space complexity: O(V) for the queue and the visited list.

        Parameters
        ----------
        start: int
            Vertex from which traversal starts.

        visited: list[bool]
            List where indexes are vertex indexes and values show whether
            the vertex has been entered.

        before_enter: TraversalCallback | None
            Callback run before a candidate vertex is entered.

        after_enter: TraversalCallback | None
            Callback run after a vertex is marked visited.

        before_exit: TraversalCallback | None
            Callback run after neighbors are processed and before exit.

        after_exit: TraversalCallback | None
            Callback run after the vertex exits.

        Returns
        -------
        None
        """
        if not self._run_callback(before_enter, start, None):
            return
        if visited[start]:
            return

        visited[start] = True
        self._run_callback(after_enter, start, None)
        queue = deque([(start, None)])

        while queue:
            vertex, parent = queue.popleft()

            for neighbor in self.vertices[vertex].edges.keys():
                if not self._run_callback(before_enter, neighbor, vertex):
                    continue
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if not self._run_callback(after_enter, neighbor, vertex):
                        return
                    queue.append((neighbor, vertex))

            if not self._run_callback(before_exit, vertex, parent):
                return
            if not self._run_callback(after_exit, vertex, parent):
                return

    def _find_arg(self, default: Any,
                  arg_dict: dict[int, str], *args, **kwargs) -> Any:
        """
        Find the required argument among args.

        Parameters
        ----------
        default: Any
            Value to be returned if the required argument was not provided.

        arg_dict: dict[int, str]
            Dictionary where index corresponds to the possible argument
            position in args, and value - in kwargs.

        Returns
        -------
        Any
            The required argument found within args or kwargs or the default
            value if the argument was not found.
        """

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

    def _find_index(self, **kwargs) -> int | None:
        """
        Find index of the vertex by data or index provided in kwargs
        for further removal.

        Parameters
        ----------
        kwargs['index']: int
            Index of the vertex to remove.
        or
        kwargs['data']: Any
            Data inside the vertex to remove.

        Returns
        -------
        int
            The index of the vertex to remove.

        Raises
        ------
        KeyError
            If data or index were not found among kwargs.
        """

        if 'data' in kwargs.keys():
            index = \
                [vertex.index for vertex in self.vertices
                 if vertex.data == kwargs['data']][0]
        elif 'index' in kwargs.keys():
            index = kwargs['index']
        else:
            raise KeyError('no index or data specified to remove')
        return index

    def is_cyclic_util(self, vertex: int,
                       visited: list[bool], rec_stack: list[bool]) -> bool:
        """
        Utility method which is used by is cyclic method.

        This utility uses the shared DFS traversal callbacks. It marks
        vertices in the active recursion stack on enter and removes them
        on exit. Encountering a candidate already in the recursion stack
        means a directed cycle exists.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Parameters
        ----------
        vertex: int
            Vertex being visited.

        visited: list[bool]
            List where vertices are marked as visited (True)
            or not visited (False).

        rec_stack: list[bool]
            List used as a stack showing which vertices were visited
            in the active iteration of the is_cyclic method.

        Returns
        -------
        bool
            Whether the cycle was discovered during current iteration.
        """

        has_cycle = [False]

        def before_enter(node: int, parent: int | None) -> bool:
            if rec_stack[node]:
                has_cycle[0] = True
                return False
            return not has_cycle[0]

        def after_enter(node: int, parent: int | None) -> None:
            rec_stack[node] = True

        def after_exit(node: int, parent: int | None) -> None:
            rec_stack[node] = False

        self._dfs_traverse(
            vertex, visited, before_enter=before_enter,
            after_enter=after_enter, after_exit=after_exit)
        return has_cycle[0]

    def topological_sort_util(self, vertex: int,
                              visited: list[bool], stack: list[int]) -> None:
        """
        Utility method which is used by topological sort method.

        This utility uses the shared DFS traversal callbacks and appends
        each vertex to the front of the result stack after the vertex exits.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Parameters
        ----------
        vertex: int
            Vertex for which the place is being searched.

        visited: list[bool]
            List where vertices are marked as visited (True)
            or not visited (False).

        stack: list[int]
            List which stores the result of the sort.

        Returns
        -------
        None
        """

        def after_exit(node: int, parent: int | None) -> None:
            stack.insert(0, node)

        self._dfs_traverse(vertex, visited, after_exit=after_exit)

    def tarjan_dfs(self, vertex: int, index: list[int], stack: list[int],
                   low_link: list[int], on_stack: list[bool],
                   scc: list[list[int]]) -> None:
        """
        Utility method which is used by tarjan_scc method.

        Parameters
        ----------
        vertex: int
            Vertex being visited.

        index: list[int]
            List where all vertices are assigned an index based on
            how early they were visited or -1 if they have not been visited.

        stack: list[int]
            List gathering current scc segment.

        low_link: list[int]
            List where all vertices are assigned a low-link value based on
            the smallest index of visited vertex from which the current
            one is accessible. Unvisited are assigned -1's.

        on_stack: list[bool]
            List showing which vertices are visited in the current dfs queue.

        scc: list[list[int]]
            List of sccs.

        Returns
        -------
        None
        """

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

    def fill_order(self, vertex: int,
                   visited: set[int], stack: list[int]) -> None:
        """
        Utility function for DFS and to fill the stack with vertices
        based on their finishing times.

        This utility uses the shared DFS traversal callbacks and appends
        each vertex to the stack after the vertex exits. Kosaraju's
        algorithm uses that stack as decreasing finish-time order.

        Time complexity: O(V + E)
        Space complexity: O(V)

        Parameters
        ----------
        vertex: int
            Currently visited vertex.

        visited: set
            Set of visited vertices.

        stack: list[int]
            Stack to push vertices according to their finishing times.

        Returns
        -------
        None
        """

        state_size = self._vertex_state_size()
        visited_list = [False] * state_size
        for node in visited:
            visited_list[node] = True

        def after_enter(node: int, parent: int | None) -> None:
            visited.add(node)

        def after_exit(node: int, parent: int | None) -> None:
            stack.append(node)

        self._dfs_traverse(
            vertex, visited_list, after_enter=after_enter,
            after_exit=after_exit)

    def bfs_level_graph(self, source: int) -> list[int]:
        """
        A method to set up levels for vertices for Dinic's algorithms
        using BFS.

        Parameters
        ----------
        source: int
            Vertex which is the source of the flow.

        Returns
        -------
        list[int]
            The list of levels of vertices where indexes are ones of vertices
            and values are levels.
        """

        levels = [-1] * len(self.vertices)
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

    def dfs_blocking_flow(self, source: int, sink: int, flow: int,
                          levels: list[int]) -> int:
        """
        Performs DFS to find a blocking flow in a level graph
        from source to sink.

        Parameters
        ----------
        source : int
            The index of the source vertex from where the flow starts.

        sink : int
            The index of the sink vertex where the flow ends.

        flow : int
            The amount of flow that can potentially be pushed through
            the path.

        levels : list[int]
            A list representing the level graph
            where levels[i] is the level of vertex i.

        Returns
        -------
        int or float
            The amount of flow that was actually pushed
            from the source to the sink.
            If no flow is possible, returns 0.

        Raises
        ------
        KeyError
            If a reverse edge necessary for updating flow does not exist,
            indicating an inconsistency in the graph's edge management.
        """

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

    def initialize_preflow(self, source: int) -> None:
        """
        Initializes heights and preflows for all vertices
        for Goldberg-Tarjan's flow calculation algorithm.

        Parameters
        ----------
        source : int
            The index of the source vertex in the graph.

        Returns
        -------
        None
        """
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

    def push_flow(self, u: int, v: int) -> bool:
        """
        A method to push flow from vertex with index u
        to the vertex with index v if push is possible.

        Parameters
        ----------
        u: int
            The index of the vertex to push from.

        v: int
            The index of the vertex to push to.

        Returns
        -------
        bool
            Whether it was possible to push flow.
        """
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

    def lift_vertex(self, u: int) -> None:
        """
        Increase vertex height by 1.

        Parameters
        ----------
        u: int
            The index of the vertex which height will be increased.

        Returns
        -------
        None
        """
        min_height = float('inf')
        for edge in self.vertices[u].edges.keys():
            if self.vertices[u].edges[edge].capacity > \
                    self.vertices[u].edges[edge].flow:
                min_height = \
                    min(min_height, self.vertices[edge].height)
        if min_height < float('inf'):
            self.vertices[u].height = min_height + 1

    def discharge_excess_flow(self, u: int) -> None:
        """
        Discharge excess flow down the path to the sink from the vertex.

        Parameters
        ----------
        u: int
            The vertex from which excess flow will be discharged.

        Returns
        -------
        None
        """
        while self.vertices[u].excess_flow > 0:
            for neighbor in self.vertices[u].edges.keys():
                if self.push_flow(u, neighbor):
                    break
            else:
                # No push occurred, lift the vertex
                self.lift_vertex(u)
                # Necessary to prevent infinite loop if no push is possible
                break
