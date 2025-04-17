# python_solutions

______________________________________________________________________

This module contains python implementations of various sorting algorithms,
basic and advanced data structures and tests providing not only coverage
for the code, but also examples of usage.

## Contents

- Sorting Algorithms

  - insertion_sorts:
    [docs](./insert_sort.md),
    [source code](../insert_sort.py),
    [import tests](../tests/test_insert_sort.py),
    [case tests](../tests/test_sorts_and_searches.py),
    [performance](../speed_tuning/sorts_for_floats.md)

  - merge_sort:
    [docs](./merge_sort.md),
    [source code](../merge_sort.py),
    [import tests](../tests/test_merge_sort.py),
    [case tests](../tests/test_sorts_and_searches.py),
    [performance for floats](../speed_tuning/sorts_for_floats.md),
    [performance for integers](../speed_tuning/sorts_for_integers.md),
    [performance tuning](../speed_tuning/merge_sort_tuning.md),
    [animation](../speed_tuning/README.md)

  - quick_sort:
    [docs](./quick_sort.md),
    [source code](../quick_sort.py),
    [tests](../tests/test_sorts_and_searches.py),
    [performance](../speed_tuning/sorts_for_floats.md)

  - heap_sort:
    [docs](./heap.md),
    [source code](../heap.py),
    [tests](../tests/test_sorts_and_searches.py),
    [performance](../speed_tuning/sorts_for_floats.md)

  - sort by counting:
    [docs](./count_sort.md),
    [source code](../count_sort.py),
    [tests](../tests/test_sorts_and_searches.py),
    [performance](../speed_tuning/sorts_for_integers.md),
    [performance tuning](../speed_tuning/count_sort_tuning.md),
    [animation](../speed_tuning/README.md)

  - sort by key inside array:
    [docs](./array_count_sort.md),
    [source code](../array_count_sort.py),
    [tests](../tests/test_sorts_and_searches.py)

  - sort by key inside 2-dim array:
    [docs](./two_dim_array_count_sort.md),
    [source code](../two_dim_array_count_sort.py),
    [tests](../tests/test_sorts_and_searches.py)

  - sort by digits:
    [docs](./digit_sort.md),
    [source code](../digit_sort.py),
    [speed tests](../tests/test_sorts_and_searches.py),
    [additional functions tests](../tests/test_digit_sort.py),
    [performance](../speed_tuning/sorts_for_integers.md)

- Data Structures

  - Array-like

    - Vector:
      [docs](./vector.md),
      [source code](../vector.py),
      [tests](../tests/test_vector.py)

    - Heap:
      [docs](./heap.md),
      [source code](../heap.py),
      [tests](../tests/test_heap.py)

  - Nodes and Linked Lists

    - OneWayNode:
      [docs](./Node.md),
      [source code](../Node.py),
      [tests](../tests/test_Node.py)

    - TwoWayNode:
      [docs](./DoubleNode.md),
      [source code](../DoubleNode.py),
      [tests](../tests/test_DoubleNode.py)

    - LinkedList:
      [docs](./LinkedList.md),
      [source code](../LinkedList.py),
      [tests](../tests/test_LinkedList.py)

    - Queue:
      [docs](./Queue.md),
      [source code](../Queue.py),
      [tests](../tests/test_Queue.py)

    - Stack:
      [docs](./Stack.md),
      [source code](../Stack.py),
      [tests](../tests/test_Stack.py)

    - Deque:
      [docs](./Deque.md),
      [source code](../Deque.py),
      [tests](../tests/test_Deque.py)

    - CyclicLinkedList:
      [docs](./CyclicLinkedList.md),
      [source code](../CyclicLinkedList.py),
      [tests](../tests/test_CyclicLinkedList.py)

  - Probabilistic

    - HashTables with different collision handling approaches:
      [docs](./hashtable.md),
      [source code](../hashtable.py),
      [tests](../tests/test_hashtable.py)

    - BloomFilter:
      [docs](./bloom_filter.md),
      [source code](../bloom_filter.py),
      [tests](../tests/test_bloom_filter.py)

    - HyperLogLog:
      [docs](./hyperloglog.md),
      [source code](../hyperloglog.py),
      [tests](../tests/test_hyperloglog.py)

  - Trees

    - BinarySearchTree:
      [docs](./bst.md),
      [source code](../bst.py),
      [tests](../tests/test_bst.py)

    - AVLTree:
      [docs](./avl_tree.md),
      [source code](../avl_tree.py),
      [tests](../tests/test_avl_tree.py)

    - RedBlackTree:
      [docs](./red_black_tree.md),
      [source code](../red_black_tree.py),
      [tests](../tests/test_red_black_tree.py),

    - SegmentTree:
      [docs](./segment_tree.md),
      [source code](../segment_tree.py),
      [tests](../tests/test_segment_tree.py),

    - SparseTable:
      [docs](./sparse_table.md),
      [source code](../sparse_table.py),
      [tests](../tests/test_sparse_table.py)

  - Graphs and Graph Nodes

    - GraphNodes and Edges:
      [docs](./graph_nodes.md),
      [source code](../graph_nodes.py),
      [tests](../tests/test_graph.py)

    - Graph:
      [docs](./graph.md),
      [source code](../graph.py),
      [tests](../tests/test_graph.py)

    - WeightedGraph:
      [docs](./weighted_graph.md),
      [source code](../weighted_graph.py),
      [tests](../tests/test_graph.py)

- Searching Algorithms

  - Binary Search:
    [docs](./bin_search.md),
    [source code](../bin_search.py),
    [tests](../tests/test_sorts_and_searches.py)

  - Binary Search for upper and lower bounds:
    [docs](./bounds.md),
    [source code](../bounds.py),
    [tests](../tests/test_sorts_and_searches.py)

  - Binary Search for functions on the real domain:
    [docs](./real_bin_search.md),
    [source code](../real_bin_search.py),
    [tests](../tests/test_sorts_and_searches.py)

  - Search for k-th ascending element in the array without sorting:
    [docs](./split_find.md),
    [source code](../split_find.py),
    [tests](../tests/test_sorts_and_searches.py)

  - Ternary Search for real function extrema:
    [docs](./ternary_search_extremum.md),
    [source code](../ternary_search_extremum.py),
    [tests](../tests/test_sorts_and_searches.py)

- Some other tools and algorithms

  - Dynamic programming solutions to different problems:
    [docs](./dynamic_programming.md),
    [source code](../dynamic_programming.py),
    [tests](../tests/test_dynamic_programming.py),
    [animation for lcs](../animations/dp_lcs.py),
    [animation for tsp](../animations/dp_tsp.py)

  - Visualization tool for matrices:
    [docs](./matrix_view.md),
    [source code](../matrix_view.py),
    [tests](../tests/test_sorts_and_searches.py)

  - Edit distances:
    [docs](./edit_distance.md),
    [source code](../edit_distance.py),
    [tests](../tests/test_edit_distance.py)

______________________________________________________________________

Docs were made using [this](./docs.py) parser, sources for this table are
[here](../__init__.py) and [here](../tests/__init__.py).
