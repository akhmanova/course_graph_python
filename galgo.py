from graph import Graph
from collections import deque


# helpful functions
def is_connected(g):
    n = g.get_n()
    if n is 0:
        return True
    matrix = g.get_matrix_adj()
    q = deque()
    used = []
    for _ in range(n):
        used.append(False)
    s = 0
    q.append(s)
    used[s] = True
    while len(q) is not 0:
        v = q.popleft()
        for i in matrix[v]:
            to = i
            if not used[to]:
                used[to] = True
                q.append(to)
    for i in used:
        if not i:
            return False
    return True


def get_components(g):
    colors = []
    n = g.get_n()
    for _ in range(n):
        colors.append(0)
    matrix = g.get_matrix_adj()
    for vertex in range(n):
        q = deque()
        s = vertex
        if colors[s] is not 0:
            continue
        color = vertex + 1
        q.append(s)
        colors[s] = color
        while len(q) is not 0:
            v = q.popleft()
            for i in matrix[v]:
                to = i
                if colors[to] is 0:
                    colors[to] = color
                    q.append(to)
    return colors


def is_tree(g):
    return is_connected(g) and g.get_m() == g.get_n() - 1


def is_forest(g):
    components = get_components(g)
    n = g.get_n()
    orig_adj = g.get_edges()
    for cur_color in range(1, n + 1):
        vertices = []
        for idx, v_color in enumerate(components):
            if cur_color is v_color:
                vertices.append(idx)
        if len(vertices) is 0:
            continue
        temp_g = Graph()
        for edge in orig_adj:
            if edge[0] in vertices and edge[1] in vertices:
                temp_g.add_edge((str(edge[0]), str(edge[1])))
                temp_g.add_edge((str(edge[1]), str(edge[0])))
        if not is_tree(temp_g):
            return False
    return True


###################################################
###############    TASKS    #######################
###################################################

# Ia
# 1) Get a list of vertex degrees
# list_of_degrees = get_degrees(graph: Graph)
# [1, 2, 3, 0, 1, 1]
def get_degrees(g):
    degrees = []
    n = g.get_n()
    for i in range(n):
        degrees.append(0)
    edges = g.get_edges()
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    return degrees


# Ib
# 1) Adjacency list of complement graph
def get_adj_complement_graph(g):
    result_adj = []
    n = g.get_n()
    for i in range(n):
        for j in range(n):
            if not (i, j) in result_adj:
                result_adj.append((i, j))
            if not (j, i) in result_adj:
                result_adj.append((j, i))
    orig_adj = g.get_adj()
    for edge in orig_adj:
        i = edge[0]
        j = edge[1]
        if (i, j) in result_adj:
            result_adj.remove((i, j))
    return result_adj


###################################################


# II a
# Check is tree or/and is forest
def is_tree_or_and_is_forest(g):
    if is_tree(g) and is_forest(g):
        return 'Both'
    elif is_forest(g):
        return 'Forest'
    else:
        return 'Neither'


# II b
# is it possible to delete any vertex and get a tree?
def can_get_tree(g):
    n = g.get_n()
    edges = g.get_edges()
    if n == 0:
        return False
    if is_tree(g):
        return True
    for v in range(n):
        list_e = []
        for edge in edges:
            if edge[0] == v or edge[1] == v:
                continue
            idx0 = edge[0]
            if edge[0] > v:
                idx0 -= 1
            idx1 = edge[1]
            if edge[1] > v:
                idx1 -= 1
            list_e.append((min(idx0, idx1), max(idx0, idx1)))
        if len(list_e) is n - 1:
            return True
    return False


###################################################
# III Prima
def prim(graph):
    res = []
    edges = graph.get_edges()
    n = graph.get_n()
    g = []
    INF = 1000000000
    min_edge = []
    sel_edge = [] # end of edge
    for i in range(n):
        g.append([])
        min_edge.append(INF)
        sel_edge.append(-1)
    for i in edges:
        g[i[0]].append([i[1], i[2]])
        g[i[1]].append([i[0], i[2]])
    min_edge[0] = 0
    queue_weight = []
    queue_weight.append([0, 0])
    for i in range(n):
        if len(queue_weight) is 0:
            return None
        v = queue_weight[0][1]
        queue_weight.remove(queue_weight[0])
        if sel_edge[v] is not -1:
            res.append([v, sel_edge[v]])

        for (to, w) in g[v]:
            if w < min_edge[to]:
                if [min_edge[to], to] in queue_weight:
                    queue_weight.remove([min_edge[to], to])
                min_edge[to] = w
                sel_edge[to] = v
                queue_weight.append([min_edge[to], to])
                queue_weight.sort()
    return res


###################################################
# IVa Dijkstra
# 17 list of all shortest ways
def deijksta(graph):
    res = []
    n = graph.get_n()
    g = []
    INF = 1000000000
    edges = graph.get_edges()
    for i in range(n):
        g.append([])
    for i in edges:
        g[i[0]].append([i[1], i[2]])
        g[i[1]].append([i[0], i[2]])
    d = []
    for ver in range(n):
        d.append([])
        used = []
        for i in range(n):
            d[ver].append(INF)
            used.append(False)
        d[ver][ver] = 0
        for i in range(n):
            v = -1
            for j in range(n):
                if not used[j] and (v is -1 or d[ver][j] < d[ver][v]):
                    v = j
            if d[ver][v] is INF:
                break
            used[v] = True
            for [to, len] in g[v]:
                if d[ver][v] + len < d[ver][to]:
                    d[ver][to] = d[ver][v] + len
    for i in d:
        for j in i:
            if j is INF:
                return None
    return d


# IV ford_bellman
# get k-shortest ways from v to u
def ford_bellman(g, k, v, u):

