from graph import Graph
from galgo import *

###################################################
# Ia
# Get a list of vertex degrees
# list_of_degrees = get_degrees(graph: Graph)
g = Graph()
g.set_oriented(False)
g.set_edges([
    (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5),
    (4, 5), (4, 6), (5, 6), (5, 7), (6, 7), (6, 8),
    (7, 8), (7, 9), (8, 9)
])
assert [0, 2, 3, 4, 4, 4, 4, 4, 3, 2], get_degrees(g)

###################################################

# Ib
# 1) Adjacency list of complement graph
g = Graph()
g.set_oriented(False)
g.set_edges([])
g.set_n(3)
assert [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0)], get_adj_complement_graph(g)
print(get_adj_complement_graph(g))

g = Graph()
g.set_oriented(False)
g.set_edges([(0, 1), (1, 2), (2, 0)])
assert [(0, 0), (1, 1), (2, 2)], get_adj_complement_graph(g)
print(get_adj_complement_graph(g))

###################################################
# II a
# Check is tree or/and is forest
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 2), (0, 1), (2, 3), (2, 4), (3, 5)
])
assert 'Both', is_tree_or_and_is_forest(g)

g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 2), (0, 1), (2, 3), (2, 4), (3, 5), (3, 4)
])
assert 'Neither', is_tree_or_and_is_forest(g)

g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 1), (2, 3), (2, 4), (3, 5)
])
assert 'Forest', is_tree_or_and_is_forest(g)


# II b
# is it possible to delete any vertex and get a tree?
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 2), (0, 1), (2, 3), (2, 4), (3, 5), (3, 4)
])
assert True, can_get_tree(g)

# False
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 2), (0, 1), (2, 3), (2, 4), (3, 9), (3, 4)
])
print(can_get_tree(g))


###################################################
# III
# Prima
# None
g = Graph()
g.set_oriented(False)
g.set_n(6)
print(prim(g))

# None
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 1, 1), (0, 5, 1), (1, 2, 1), (1, 5, 5), (1, 5, 3),
    (2, 3, 1), (2, 5, 5), (3, 5, 5), (3, 4, 1), (4, 5, 1)
])
g.set_n(6)
assert [[1, 0], [2, 1], [3, 2], [4, 3], [5, 0]], prim(g)


###################################################
# IVa Dijkstra
# 17 list of all shortest ways
# None
g = Graph()
g.set_oriented(False)
g.set_n(6)
print(deijksta(g))

g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 1, 1), (0, 5, 1), (1, 2, 1), (1, 5, 5), (1, 5, 3),
    (2, 3, 1), (2, 5, 5), (3, 5, 5), (3, 4, 1), (4, 5, 1)
])
g.set_n(6)
assert \
    [
    [0, 1, 2, 3, 2, 1],
    [1, 0, 1, 2, 3, 2],
    [2, 1, 0, 1, 2, 3],
    [3, 2, 1, 0, 1, 2],
    [2, 3, 2, 1, 0, 1],
    [1, 2, 3, 2, 1, 0]
    ],\
    deijksta(g)

# IV ford_bellman
# 22) get k-shortest ways from v to u
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 1, 100), (0, 5, 100), (1, 2, 100), (1, 5, 5), (1, 5, 3),
    (2, 3, 100), (2, 5, 5), (3, 5, 5), (3, 4, 100), (4, 5, 100)
])
g.set_n(6)
g.set_m(10)
assert [100, 103], ford_bellman(g, 2, 0, 5)

# IV ford_bellman
# 8 get set of u, where ro(v, u) <= n
g = Graph()
g.set_oriented(False)
g.set_edges([
    (0, 1, 100), (0, 5, 100), (1, 2, 100), (1, 5, 5), (1, 5, 3),
    (2, 3, 100), (2, 5, 5), (3, 5, 5), (3, 4, 100), (4, 5, 100)
])
g.set_n(6)
g.set_m(10)
assert [0, 1, 2, 5], ford_bellman_find_set(g, 0, 200)


###################################################
# V Ford Fulkerson
# Find the maximum possible flow
g = Graph()
g.set_oriented(True)
g.set_edges([
    (0, 1, 16), (0, 2, 13),
    (1, 2, 10), (1, 3, 12),
    (2, 1, 4), (2, 4, 14),
    (3, 2, 9), (3, 5, 20),
    (4, 3, 7), (4, 5, 4)
])
g.set_n(6)
g.set_m(10)
assert 23, ford_fulkerson(graph=g, source=0, sink=5)