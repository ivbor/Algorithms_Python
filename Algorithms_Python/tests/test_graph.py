import pytest
import copy
import random

from Algorithms_Python.graph_nodes \
    import GraphNode, WeightedGraphNode
from Algorithms_Python.graph import Edge, Graph
from Algorithms_Python.weighted_graph import WeightedGraph


def test_can_create_everything():
    structures = [(GraphNode, Graph),
                  (WeightedGraphNode, WeightedGraph)]
    for node, graph in structures:
        node_instance = node(0, None)
        graph_instance = graph()
        assert isinstance(node_instance, node)
        assert isinstance(graph_instance, graph)
        assert graph_instance.vertices == {}
        assert graph_instance.has_cycles is False
        assert node_instance.data is None


def test_undirected_graph_node_workes_well():
    structures = [GraphNode, WeightedGraphNode]
    for node_type in structures:
        node = node_type(index=0, data=3)
        assert node.index == 0
        assert node.data == 3
        assert node.edges == {}
        assert str(node) == '3'
        assert node.__repr__() == '3'
        if node_type == WeightedGraphNode:
            with pytest.raises(KeyError):
                node = node_type(index=0, data=3,
                                 edges=[], weights=[1, 2])


@pytest.fixture
def graphs():
    structures = [Graph, WeightedGraph]
    return structures


@pytest.fixture
def nodes():
    nodes = [(3, []), (3, [], [])]
    return nodes


def test_graphs_can_accept_vertex(graphs, nodes):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        assert graph_instance[nr].all_vertices() == ['3']


@pytest.fixture
def nodes2():
    nodes2 = [(4, []), (4, [], [])]
    return nodes2


def test_graphs_can_accept_two_unconnected_vertices(graphs, nodes, nodes2):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


def test_find_kwarg_data(graphs, nodes):
    graph_instance = []
    nodes2 = \
        [{'data': 4, 'edges': []},
         {'data': 4, 'edges': [], 'weights': []}]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(**nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']


def test_find_kwarg_with_edges(graphs, nodes):
    graph_instance = []
    nodes2 = \
        [{'data': 4, 'edges': [0]},
         {'data': 4, 'edges': [0], 'weights': [5]}]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(**nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']
        assert [i for i in graph_instance[nr].vertices[1].edges.keys()] == [0]
        if type(graph_instance[nr]) == WeightedGraph:  # noqa: E721
            assert graph_instance[nr].vertices[1].edges[0].weight == 5


@pytest.fixture
def uncon2(graphs, nodes, nodes2):
    graph_instance = []
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
    return graph_instance


@pytest.mark.parametrize('index_rem, all_vertices, first',
                         [(0, ['4'], '4'), (1, ['3'], '3')])
def test_can_remove_vertices_by_index(uncon2, index_rem, all_vertices, first):
    graph_instance = uncon2
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(index=index_rem)
        assert graph_instance[nr].all_vertices() == all_vertices
        assert str(graph_instance[nr].vertices[int(not index_rem)]) == first
        assert graph_instance[nr].vertices[int(not index_rem)].edges == {}
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index_rem]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(index=int(not index_rem))
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index_rem]


@pytest.mark.parametrize('data_rem, all_vertices, first, second, index',
                         [(3, ['4'], '4', 4, 1), (4, ['3'], '3', 3, 0)])
def test_can_remove_vertices_by_data(uncon2, data_rem, all_vertices,
                                     first, second, index):
    graph_instance = uncon2
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=data_rem)
        assert graph_instance[nr].all_vertices() == all_vertices
        assert str(graph_instance[nr].vertices[index]) == first
        assert graph_instance[nr].vertices[index].edges == {}
        with pytest.raises(Exception):
            graph_instance[nr].vertices[int(not index)]
    for nr in range(len(graph_instance)):
        graph_instance[nr].remove_vertex(data=second)
        assert graph_instance[nr].all_vertices() == []
        with pytest.raises(Exception):
            graph_instance[nr].vertices[index]


def test_raises_when_no_data_or_index_specified_in_remove(uncon2):
    with pytest.raises(KeyError):
        for nr in range(len(uncon2)):
            uncon2[nr].remove_vertex()


@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_add_edge_between_vertices_undir(uncon2, front, back):
    graph = uncon2[0]
    instances = [graph, copy.deepcopy(graph)]
    instances[0].add_edge(front, back)
    instances[1].add_edge(back, front)
    assert [i for i in instances[0].vertices[front].edges.keys()] == [back]
    assert [i for i in instances[1].vertices[back].edges.keys()] == [front]


@pytest.mark.parametrize('direction, weight', [(0, 3),
                                               (0, []),
                                               (1, 4),
                                               (1, [])])
def test_add_edge_between_vertices_wei(uncon2, direction, weight):
    graph = uncon2[1]
    instances = [graph, copy.deepcopy(graph)]
    instances[0].add_edge(direction, int(not direction), weight=weight)
    instances[1].add_edge(int(not direction), direction, weight=weight)
    if not isinstance(weight, int):
        weight = 1
    if not direction:
        assert instances[0].vertices[0].edges[1].weight == weight
        assert instances[1].vertices[1].edges[0].weight == weight
    else:
        assert instances[0].vertices[1].edges[0].weight == weight
        assert instances[1].vertices[0].edges[1].weight == weight


def test_graphs_can_accept_two_connected_vertices(graphs, nodes):
    graph_instance = []
    nodes2 = [(4, [0]), (4, [0], [3])]
    for nr, graph in enumerate(graphs):
        graph_instance.append(graph())
        graph_instance[nr].add_vertex(*nodes[nr])
        graph_instance[nr].add_vertex(*nodes2[nr])
        assert graph_instance[nr].all_vertices() == ['3', '4']
        assert [i for i in graph_instance[nr].vertices[1].edges.keys()] == [0]
        if graph == WeightedGraph:
            assert graph_instance[nr].vertices[1].edges[0].weight == 3


@pytest.fixture
def con2(graphs):
    con2 = []
    nodes = [(3, [1]), (3, [1], [5])]
    nodes2 = [(4, [0]), (4, [0], [3])]
    for nr, graph in enumerate(graphs):
        con2.append(graph())
        con2[nr].add_vertex(*nodes[nr])
        con2[nr].add_vertex(*nodes2[nr])
    return con2


@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_remove_edge(con2, front, back):
    for graph in con2:
        graph.remove_edge(front, back)
        graph.remove_edge(back, front)
        assert graph.vertices[0].edges == {}
        assert graph.vertices[1].edges == {}


@pytest.mark.parametrize('params', [({'index': 0}),
                                    ({'index': 1}),
                                    ({'data': 3}),
                                    ({'data': 4})])
def test_remove_vertex(con2, params):
    for graph in con2:
        graph.remove_vertex(**params)
        assert len(graph.vertices) == 1
        last_index = [vertex.index for vertex in graph.vertices][0]
        if 'index' in params.keys():
            if params['index'] == 0:
                assert last_index == 1
                assert graph.vertices[1].edges == {}
            else:
                assert last_index == 0
                assert graph.vertices[0].edges == {}
        else:
            if params['data'] == 3:
                assert last_index == 1
                assert graph.vertices[1].edges == {}
            else:
                assert last_index == 0
                assert graph.vertices[0].edges == {}
        graph.remove_vertex(index=last_index)
        assert len(graph.vertices) == 0


def test_add_vertices_manipulate_edges_remove_vertices():
    edges = [[4, 3, 2, 1], [0, 2, 4, 3], [3, 1, 4, 0],
             [2, 4, 1, 0], [2, 1, 3, 0]]
    weights = [[random.uniform(-100, 100) for _ in range(4)]
               for _ in range(5)]
    undir = Graph()
    weigh = WeightedGraph()
    graphs = [undir, weigh]
    for i in range(5):
        for graph in graphs:
            graph.add_vertex(data=10*i)
            assert len(graph.all_vertices()) == i + 1
            assert graph.vertices[i].data == 10*i
    for graph in graphs:
        for vertex_nr, vertex in enumerate(edges):
            for edge_nr, edge in enumerate(vertex):
                if type(graph) == WeightedGraph:  # noqa: E721
                    graph.add_edge(vertex_nr, edge,
                                   weight=weights[vertex_nr][edge_nr])
                    assert edge in graph.vertices[vertex_nr].edges
                    assert graph.vertices[vertex_nr].edges[edge]\
                        .weight == weights[vertex_nr][edge_nr]
                if type(graph) == Graph:  # noqa: E721
                    graph.add_edge(vertex_nr, edge)
                    assert edge in graph.vertices[vertex_nr].edges
    undir.remove_edge(0, 4)
    assert len(undir.vertices[0].edges) == 3
    assert [i for i in undir.vertices[0].edges.keys()] == [3, 2, 1]
    with pytest.raises(KeyError):
        undir.vertices[0].edges[4]
    weigh.remove_edge(2, 0)
    assert len(weigh.vertices[2].edges) == 3
    assert [i for i in weigh.vertices[2].edges.keys()] == [3, 1, 4]
    with pytest.raises(KeyError):
        weigh.vertices[2].edges[0]
    undir.add_edge(0, 4)
    assert len(undir.vertices[0].edges) == 4
    assert [i for i in undir.vertices[0].edges.keys()] == [3, 2, 1, 4]
    assert len(undir.vertices[4].edges) == 4
    assert [i for i in undir.vertices[4].edges.keys()] == [2, 1, 3, 0]
    assert isinstance(undir.vertices[0].edges[4], Edge)
    new_weight = [random.uniform(-100, 100)]
    weigh.add_edge(2, 0, weight=new_weight)
    assert len([i for i in weigh.vertices[0].edges.keys()]) == 4
    assert isinstance(weigh.vertices[2].edges[0], Edge)
    assert weigh.vertices[2].edges[0].weight == new_weight

    for graph in [undir, weigh]:
        indexes_changed = [0, 1, 2, 3, 4]
        for i in range(5):
            # the vertex to delete
            index = \
                random.choice(indexes_changed)

            # remove vertex from the graph
            assert len(graph.vertices) == (5 - i)
            graph.remove_vertex(index=index)
            assert len(graph.vertices) == (5 - i - 1)
            for i in range(5):
                if i != index and i in indexes_changed:
                    assert index not in \
                        [j for j in graph.vertices[i].edges.keys()]
                else:
                    assert index not in \
                        [vertex.index for vertex in graph.vertices]
            indexes_changed.remove(index)


global weights
weights = [[random.uniform(-100, 100) for _ in range(4)] for _ in range(5)]


@pytest.fixture
def con5():
    edges = [[4, 3, 2, 1], [0, 2, 4, 3], [3, 1, 4, 0],
             [2, 4, 1, 0], [2, 1, 3, 0]]
    undir = Graph()
    weigh = WeightedGraph()
    graphs = [undir, weigh]
    for i in range(5):
        for graph in graphs:
            graph.add_vertex(data=10*i)
    for graph in graphs:
        for vertex_nr, vertex in enumerate(edges):
            for edge_nr, edge in enumerate(vertex):
                if type(graph) == WeightedGraph:  # noqa: E721
                    graph.add_edge(vertex_nr, edge,
                                   weight=weights[vertex_nr][edge_nr])
                if type(graph) == Graph:  # noqa: E721
                    graph.add_edge(vertex_nr, edge)
    return graphs


@pytest.fixture
def bfs_graph():
    # 0 - 1-5
    # \\\ | |
    #    -2-6
    #  \\ | |
    #    -3-7
    #   \ | |
    #    -4-8
    graph = WeightedGraph()
    for i in range(9):
        graph.add_vertex(data=i)
    edges = [[1, 2, 3, 4],  # 0
             [0, 2, 5],     # 1
             [0, 1, 3, 6],  # 2
             [0, 2, 4, 7],  # 3
             [0, 3, 8],     # 4
             [1, 6],        # 5
             [2, 5, 7],     # 6
             [3, 6, 8],     # 7
             [4, 7]]        # 8
    for vertex, neighbors in enumerate(edges):
        for neighbor in neighbors:
            graph.add_edge(vertex, neighbor)
    return graph


def test_bfs(uncon2, con2, con5, bfs_graph):
    for i in range(2):
        uncon2[i].remove_edge(0, 1)
        assert uncon2[i].vertices[0].edges == {}
        assert uncon2[i].vertices[1].edges == {}
        assert uncon2[i].bfs(0, 0) == [0]
        with pytest.raises(IndexError):
            uncon2[i].bfs(0, 1)
        con2[i].add_edge(0, 1)
        assert [i for i in con2[i].vertices[0].edges.keys()] == [1]
        assert [i for i in con2[i].vertices[1].edges.keys()] == [0]
        assert con2[i].bfs(0, 0) == [0]
        assert con2[i].bfs(0, 1) == [0, 1]
        for j in range(5):
            target = random.choice([0, 1, 2, 3, 4])
            while target == j:
                target = random.choice([0, 1, 2, 3, 4])
            assert con5[i].bfs(j, target) == [j, target]
        edges = [[1, 2, 3, 4],  # 0
                 [2, 5],  # 1
                 [3],     # 2
                 [4],     # 3
                 [],      # 4
                 [6],     # 5
                 [2, 7],  # 6
                 [3, 8],  # 7
                 [4]]     # 8
        for vertex, neighbors in enumerate(edges):
            bfs_graph.vertices[vertex].edges = {}
            for neighbor in neighbors:
                bfs_graph.add_edge(vertex, neighbor)
        assert bfs_graph.bfs(0, 4) == [0, 4]
        edges = [[1],     # 0
                 [2, 5],  # 1
                 [3],     # 2
                 [4],     # 3
                 [],      # 4
                 [6],     # 5
                 [2, 7],  # 6
                 [3, 8],  # 7
                 [4]]     # 8
        for vertex, neighbors in enumerate(edges):
            bfs_graph.vertices[vertex].edges = {}
            for neighbor in neighbors:
                bfs_graph.add_edge(vertex, neighbor)
        assert bfs_graph.bfs(0, 4) == [0, 1, 2, 3, 4]


def test_adjancency_matrix(con5):
    for i in range(2):
        if type(con5[i]) == Graph:  # noqa: E721
            assert con5[i].to_adjacency_matrix() == [[0, 1, 1, 1, 1],
                                                     [1, 0, 1, 1, 1],
                                                     [1, 1, 0, 1, 1],
                                                     [1, 1, 1, 0, 1],
                                                     [1, 1, 1, 1, 0]]
        if type(con5[i]) == WeightedGraph:   # noqa: E721
            adj_mtx = con5[i].to_adjacency_matrix()
            for row_nr in range(len(adj_mtx)):
                for col_nr in range(len(con5[i].vertices)):
                    if row_nr != col_nr:
                        assert abs(adj_mtx[row_nr][col_nr] -
                                   con5[i].vertices[row_nr]
                                   .edges[col_nr].weight) <= 10**-6
                    else:
                        assert adj_mtx[row_nr][col_nr] == 0


def test_cycles_detector(uncon2, con5, bfs_graph):

    for i in range(2):
        assert uncon2[i].is_cyclic() is False
        assert con5[i].is_cyclic() is True

    assert bfs_graph.is_cyclic() is True

    edges = [[1],  # 0
             [5],  # 1
             [],   # 2
             [2],  # 3
             [3],  # 4
             [6],  # 5
             [7],  # 6
             [8],  # 7
             [4]]  # 8
    for vertex, neighbors in enumerate(edges):
        bfs_graph.vertices[vertex].edges = {}
        for neighbor in neighbors:
            bfs_graph.add_edge(vertex, neighbor)

    assert bfs_graph.is_cyclic() is False


def test_topo_sort(bfs_graph):

    # error for cycle
    # 0 > 1>5
    #     ^ |
    #     2 6
    #     ^ |
    #     3 7
    #     ^ |
    #     4<8

    edges = [[1],  # 0
             [5],  # 1
             [1],  # 2
             [2],  # 3
             [3],  # 4
             [6],  # 5
             [7],  # 6
             [8],  # 7
             [4]]  # 8

    for vertex, neighbors in enumerate(edges):
        bfs_graph.vertices[vertex].edges = {}
        for neighbor in neighbors:
            bfs_graph.add_edge(vertex, neighbor)

    with pytest.raises(RecursionError):
        bfs_graph.topological_sort()

    bfs_graph.vertices[2].edges = {}
    assert bfs_graph.topological_sort() == [0, 1, 5, 6, 7, 8, 4, 3, 2]


def test_single_node():
    graph = Graph()
    graph.add_vertex(data=0)
    assert graph.tarjan_scc() == [[0]]
    assert graph.kosaraju_scc() == [[0]]


def test_two_nodes_no_edge():
    graph = Graph()
    graph.add_vertex(data=0)
    graph.add_vertex(data=1)
    assert graph.tarjan_scc() == [[0], [1]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()]) == [[0], [1]]


def test_simple_cycle():
    graph = Graph()
    graph.add_vertex(data=0)
    graph.add_vertex(data=1)
    graph.add_vertex(data=2)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    assert sorted([sorted(scc) for scc in graph.tarjan_scc()]) == [[0, 1, 2]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()]) == [[0, 1, 2]]


@pytest.fixture
def graph():
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    return graph


def test_multiple_scc(graph):
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(3, 2)  # This creates two SCCs: {0,1,2} and {3}
    assert sorted([sorted(scc) for scc in graph.tarjan_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3]]


def test_complex_graph(graph):
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 3)
    # This creates two SCCs: {0,1,2} and {3,4},
    # assuming no connections between these groups
    assert sorted([sorted(scc) for scc in graph.tarjan_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3, 4, 5]]
    assert sorted([sorted(scc) for scc in graph.kosaraju_scc()],
                  key=lambda scc: scc[0]) == [[0, 1, 2], [3, 4, 5]]


def test_edge_cases():
    graph = Graph()
    # Test an edge case, such as a graph with no vertices
    assert graph.tarjan_scc() == []
    assert graph.kosaraju_scc() == []


@pytest.mark.parametrize('graph_type', [Graph,
                                        WeightedGraph])
def test_dijkstra_undir(graph_type):
    graph = graph_type()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    if graph_type == Graph:
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 5)
        assert graph.dijkstra(0) == ([0, 1, 2, 3, 4, 5],
                                     {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4})
    elif graph_type == WeightedGraph:
        graph.add_edge(0, 1, weight=2)
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 0, weight=4)
        graph.add_edge(2, 3, weight=5)
        graph.add_edge(3, 4, weight=6)
        graph.add_edge(4, 5, weight=7)
        assert graph.dijkstra(0) == ([0, 2, 5, 10, 16, 23],
                                     {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4})
        graph.add_edge(0, 2, weight=4)
        graph.add_edge(3, 5, weight=8)
        assert graph.dijkstra(0) == ([0, 2, 4, 9, 15, 17],
                                     {0: 0, 1: 0, 2: 0, 3: 2, 4: 3, 5: 3})


def test_bellman_ford():
    graph = WeightedGraph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1, weight=2)
    graph.add_edge(1, 2, weight=3)
    graph.add_edge(2, 0, weight=4)
    graph.add_edge(2, 3, weight=5)
    graph.add_edge(3, 4, weight=6)
    graph.add_edge(4, 5, weight=7)
    assert graph.bellman_ford(0) == ([0, 2, 5, 10, 16, 23],
                                     {0: [0],
                                      1: [0, 1],
                                      2: [0, 1, 2],
                                      3: [0, 1, 2, 3],
                                      4: [0, 1, 2, 3, 4],
                                      5: [0, 1, 2, 3, 4, 5]})
    graph.add_edge(0, 2, weight=-4)
    graph.add_edge(3, 5, weight=-8)

    with pytest.raises(ValueError):
        graph.bellman_ford(0)


@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_simple_flow(graph, algo):

    graph.add_edge(0, 1, capacity=1)
    graph.add_edge(1, 0, capacity=1)
    graph.add_edge(1, 2, capacity=1)
    graph.add_edge(2, 1, capacity=1)
    graph.add_edge(2, 3, capacity=1)
    graph.add_edge(3, 2, capacity=1)

    if algo == 'dinics':
        dinics_max_flow = graph.dinics_algorithm(0, 3)
        assert dinics_max_flow == 1
    else:
        gt_max_flow = graph.goldberg_tarjan(0, 3)
        assert gt_max_flow == 1


@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_multiple_flows(graph, algo):

    graph.add_edge(0, 1, capacity=1)
    graph.add_edge(1, 0, capacity=1)
    graph.add_edge(1, 3, capacity=1)
    graph.add_edge(3, 1, capacity=1)
    graph.add_edge(0, 2, capacity=2)
    graph.add_edge(2, 0, capacity=2)
    graph.add_edge(2, 3, capacity=2)
    graph.add_edge(3, 2, capacity=2)

    if algo == 'dinics':
        dinics_max_flow = graph.dinics_algorithm(0, 3)
        assert dinics_max_flow == 3
    else:
        gt_max_flow = graph.goldberg_tarjan(0, 3)
        assert gt_max_flow == 3


@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_no_flow(algo):

    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)

    if algo == 'dinics':
        dinics_max_flow = graph.dinics_algorithm(0, 1)
        assert dinics_max_flow == 0
    else:
        gt_max_flow = graph.goldberg_tarjan(0, 1)
        assert gt_max_flow == 0


@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_max_flow(graph, algo):

    graph.add_vertex(4)
    graph.add_vertex(5)

    graph.add_edge(0, 1, capacity=10)
    graph.add_edge(1, 0, capacity=10)

    graph.add_edge(1, 2, capacity=4)
    graph.add_edge(2, 1, capacity=4)

    graph.add_edge(2, 5, capacity=10)
    graph.add_edge(5, 2, capacity=10)

    graph.add_edge(0, 3, capacity=8)
    graph.add_edge(3, 0, capacity=8)

    graph.add_edge(3, 5, capacity=8)
    graph.add_edge(5, 3, capacity=8)

    graph.add_edge(1, 3, capacity=6)
    graph.add_edge(3, 1, capacity=6)

    graph.add_edge(1, 4, capacity=6)
    graph.add_edge(4, 1, capacity=6)

    graph.add_edge(4, 5, capacity=12)
    graph.add_edge(5, 4, capacity=12)

    if algo == 'dinics':
        dinics_max_flow = graph.dinics_algorithm(0, 5)
        assert dinics_max_flow == 18
    else:
        gt_max_flow = graph.goldberg_tarjan(0, 5)
        assert gt_max_flow == 18


@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_backflow(graph, algo):

    graph.add_vertex(4)

    graph.add_edge(0, 1, capacity=10)
    graph.add_edge(1, 0, capacity=10)

    graph.add_edge(1, 2, capacity=4)
    graph.add_edge(2, 1, capacity=4)

    graph.add_edge(2, 4, capacity=12)
    graph.add_edge(4, 2, capacity=12)

    graph.add_edge(0, 3, capacity=8)
    graph.add_edge(3, 0, capacity=8)

    graph.add_edge(3, 2, capacity=6)
    graph.add_edge(2, 3, capacity=6)

    if algo == 'dinics':
        dinics_max_flow = graph.dinics_algorithm(0, 4)
        assert dinics_max_flow == 10
    else:
        gt_max_flow = graph.goldberg_tarjan(0, 4)
        assert gt_max_flow == 10


@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_correctness(algo):
    graph = WeightedGraph()
    # Triangle graph with weights
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(0, 1, weight=1)
    graph.add_edge(1, 0, weight=1)
    graph.add_edge(1, 2, weight=2)
    graph.add_edge(2, 1, weight=2)
    graph.add_edge(0, 2, weight=3)
    graph.add_edge(2, 0, weight=3)
    if algo == 'prims':
        mst_edges = graph.prims_algorithm_mst()
    else:
        mst_edges = graph.kruskals_mst()
    assert len(mst_edges) == 2
    total_weight = sum(weight for _, _, weight in mst_edges)
    assert total_weight == 3


@pytest.mark.parametrize('algo', ['prims'])
def test_algorithm_mst_disconnected_graph(algo):
    graph = WeightedGraph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(0, 1, weight=1)
    graph.add_edge(1, 0, weight=1)
    graph.add_edge(2, 3, weight=2)
    graph.add_edge(3, 2, weight=2)
    if algo == 'prims':
        mst_edges = graph.prims_algorithm_mst()
    else:
        mst_edges = graph.kruskals_mst()
    assert len(mst_edges) == 1


@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_empty_graph(algo):
    graph = WeightedGraph()
    if algo == 'prims':
        mst_edges = graph.prims_algorithm_mst()
    else:
        mst_edges = graph.kruskals_mst()
    assert len(mst_edges) == 0, "MST of an empty graph should be an empty list"


@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_uniform_weights(algo):
    graph = WeightedGraph()
    # Creating a square graph where all edge weights are the same
    vertices = ['A', 'B', 'C', 'D']
    for v in vertices:
        graph.add_vertex(v)
    graph.add_edge(0, 1, weight=1)
    graph.add_edge(1, 0, weight=1)
    graph.add_edge(1, 2, weight=1)
    graph.add_edge(2, 1, weight=1)
    graph.add_edge(2, 3, weight=1)
    graph.add_edge(3, 2, weight=1)
    graph.add_edge(3, 0, weight=1)
    graph.add_edge(0, 3, weight=1)
    # Adding a diagonal with the same weight
    graph.add_edge(0, 2, weight=1)
    graph.add_edge(2, 0, weight=1)
    if algo == 'prims':
        mst_edges = graph.prims_algorithm_mst()
    else:
        mst_edges = graph.kruskals_mst()
    assert len(mst_edges) == 3


def test_mst_complex_graph():
    graph = WeightedGraph()
    vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for v in vertices:
        graph.add_vertex(v)
    for i in range(10):
        for _ in range(2):
            second = random.choice(vertices)
            while second == i:
                second = random.choice(vertices)
                continue
            weight = random.randint(1, 101)
            graph.add_edge(i, second, weight=weight)
            graph.add_edge(second, i, weight=weight)
    prims_mst = graph.prims_algorithm_mst()
    kruskals_mst = graph.kruskals_mst()
    prims_weights = sum([weight for _, _, weight in prims_mst])
    kruskals_weights = sum([weight for _, _, weight in kruskals_mst])
    assert prims_weights == kruskals_weights


def test_graph_vertices_and_edges_coloring():
    vertices = [0, 1, 2]
    edges = [(0, 1), (1, 2), (2, 0), (1, 0), (2, 1), (0, 2)]
    graph = Graph()
    for v in vertices:
        graph.add_vertex(v)
    for edge in edges:
        graph.add_edge(*edge)
    assert graph.color_vertices() == 3
    assert graph.color_edges() == 3

    # Verify vertex coloring
    vertex_colors = set(v.color for v in graph.vertices)
    assert len(vertex_colors) == 3

    # Verify edge coloring
    assert len(set(e.color for v in graph.vertices
                   for _, e in v.edges.items())) == 3


def test_complex_graph_coloring():
    # Initialize the complex graph
    vertices = [i for i in range(8)]  # 8 vertices
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (1, 0), (2, 1), (3, 2), (0, 3),  # Cycle
             (4, 5), (5, 6), (6, 4),
             (5, 4), (6, 5), (4, 6),  # Clique
             (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
             (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
             # Additional connections
             (0, 4), (4, 0)  # Additional edge for complexity
             ]

    g = Graph()
    for v in vertices:
        g.add_vertex(v)
    for u, v in edges:
        g.add_edge(u, v)

    assert g.color_vertices() >= 4
    assert g.color_edges() >= 3

    # Verify vertex coloring
    vertex_colors = set(v.color for v in g.vertices)
    assert len(vertex_colors) >= 4

    # Verify edge coloring
    assert len(set(e.color for v in g.vertices for _, e in v.edges.items())) \
        >= 3
