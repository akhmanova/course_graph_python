# copy obj (not references)
from copy import deepcopy


class Graph:
    # count of vertexes
    __n = 0
    # count of edges
    __m = 0
    # list of adjacency (idx)
    __adj = []
    # list of edges (idx)
    __edges = []
    # dict from v.name to v.index
    __v_name_to_idx = {}
    # dict from v.index to v.name
    __v_idx_to_name = {}
    # oriented flag
    __oriented = False
    # weight flag
    __weight = False

    # GRAPH CONSTRUCTOR
    #
    # Types:
    # 1. Empty graph
    #      g = Graph()
    #
    # 2. Copy graph
    #      g = Graph(original_graph=old_g)
    #
    # 3. Fill graph (all parameters are optional
    #      g = Graph(
    #           n=<number of vertices>,
    #           m=<number of edges>,
    #           adj=<adjacency list [(1, 2, -1), (3, 4, 0)]>,
    #           edges=<edges list [(1, 2, -1), (3, 4, 0)]>,
    #           v_name_to_idx=<{'apple'=1, 'pear'=2}>
    #           v_idx_to_name=<{1='apple', 2='pear'}>
    #           oriented=<False or True>
    def __init__(self, **kwargs):

        # Copy from original graph
        if 'original_graph' in kwargs:
            self.__n = deepcopy(kwargs.original_graph.n)
            self.__m = deepcopy(kwargs.original_graph.m)
            self.__adj = deepcopy(kwargs.original_graph.adj)
            self.__edges = deepcopy(kwargs.original_graph.edges)
            self.__v_name_to_idx = deepcopy(kwargs.original_graph.v_name_to_idx)
            self.__v_idx_to_name = deepcopy(kwargs.original_graph.v_idx_to_name)
            print ("A class was created from the sample!")
            return 
        
        if 'n' in kwargs:
            self.__n = deepcopy(kwargs.get('n'))
        if 'm' in kwargs:
            self.__m = deepcopy(kwargs.get('m'))
        if 'adj' in kwargs:
            self.__adj = deepcopy(kwargs.get('adj'))
        if 'edges' in kwargs:
            self.__edges = deepcopy(kwargs.get('edges'))
        if 'v_name_to_idx' in kwargs:
            self.__v_name_to_idx = deepcopy(kwargs.get('v_name_to_idx'))
        if 'v_idx_to_name' in kwargs:
            self.__v_idx_to_name = deepcopy(kwargs.get('v_idx_to_name'))
        if 'oriented' in kwargs:
            self.__oriented = deepcopy(kwargs.get('oriented'))

        print("New class was created!")

    def get_n(self):
        return self.__n

    def get_m(self):
        return self.__m

    def get_adj(self):
        return self.__adj

    def get_edges(self):
        return self.__edges

    def get_v_name_to_idx(self):
        return self.__v_name_to_idx

    def get_v_idx_to_name(self):
        return self.__v_idx_to_name

    def get_oriented(self):
        return self.__oriented

    def set_n(self, n):
        try:
            n = int(n)
        except Exception:
            return False
        if n < 0:
            return False
        for (i, j) in self.__adj:
            if i >= n or j >= n:
                return False
        self.__n = deepcopy(n)
        return True

    def set_m(self, m):
        try:
            m = int(m)
        except Exception:
            return False
        if m < 0 or len(self.__adj) != m:
            return False
        self.__m = deepcopy(m)
        return True

    def set_edges(self, adj):
        try:
            adj = list(adj)
            if len(adj) > 0 and len(adj[0]) == 3 or self.__weight:
                for (i, j, v) in adj:
                    if i < 0 or j < 0 or type(i) != int or type(j) != int or type(v) != int:
                        raise Exception
            elif len(adj) > 0 and len(adj[0]) == 2:
                for (i, j) in adj:
                    if i < 0 or j < 0 or type(i) != int or type(j) != int:
                        raise Exception
        except Exception:
            return False
        self.__m = 0
        self.__n = 0
        self.__adj = []
        self.__edges = []

        for i in adj:
            result = self.add_edge(i)
            if not result:
                return False
        return True

    def set_v_name_to_idx(self, v_name_to_idx):
        temp_dict = {}
        if type(v_name_to_idx) is not dict:
            return False
        try:
            for name, idx in v_name_to_idx.items():
                temp_dict[name] = idx
            for name, idx in temp_dict.items():
                self.__v_name_to_idx[name] = idx
                self.__v_idx_to_name[idx] = name
            self.__n = max(self.__n, len(self.__v_name_to_idx), len(self.__v_idx_to_name))
            return True
        except:
            return False
        return True

    def set_v_idx_to_name(self, v_idx_to_name):
        temp_dict = {}
        if type(v_idx_to_name) is not dict:
            return False
        try:
            for idx, name in v_idx_to_name.items():
                temp_dict[idx] = name
            for idx in temp_dict.items():
                self.__v_idx_to_name[idx] = name
                self.__v_name_to_idx[name] = idx
            self.__n = max(self.__n, len(self.__v_name_to_idx), len(self.__v_idx_to_name))
            return True
        except:
            return False

    def set_oriented(self, oriented):
        self.__oriented = oriented
    
    def set_weight(self, weight):
        old_weight = self.__weight
        if type(weight) != bool:
            return False
        try:
            if old_weight != weight:
                temp_adj = []
                self.__weight = weight
                if self.__weight:
                    for (i, j) in self.__adj:
                        temp_adj.append(i, j, 0)
                else:
                    for (i, j, v) in self.__adj:
                        temp_adj.append(i, j)
                self.__adj = deepcopy(temp_adj)
            return True
        except:
            return False
    
    def add_edge(self, edge):
        if type(edge) != tuple:
            return False
        try:
            if len(edge) == 3 and not self.__weight:
                self.set_weight(True)

            if type(edge[0]) == int:
                i = edge[0]
            else:
                if not edge[0] in self.__v_name_to_idx:
                    self.__v_name_to_idx[edge[0]] = self.__n
                    self.__v_idx_to_name[self.__n] = edge[0]
                    self.__n += 1
                i = self.__v_name_to_idx[edge[0]]
            if type(edge[1]) == int:
                j = edge[1]
            else:
                if not edge[1] in self.__v_name_to_idx:
                    self.__v_name_to_idx[edge[1]] = self.__n
                    self.__v_idx_to_name[self.__n] = edge[1]
                    self.__n += 1
                j = self.__v_name_to_idx[edge[1]]
            if len(edge) == 2:
                idx_edge = (i, j)
            else:
                idx_edge = (i, j, edge[2])

            self.__n = max(self.__n, idx_edge[0] + 1, idx_edge[1] + 1)
            self.__adj.append(idx_edge)
            self.__edges.append(idx_edge)
            self.__m += 1
            if not self.__oriented:
                if len(idx_edge) == 3:
                    revert_edge = (idx_edge[1], idx_edge[0], idx_edge[2])
                else:
                    revert_edge = (idx_edge[1], idx_edge[0])
                self.__adj.append(revert_edge)
            self.add_vertex(idx_edge[0])
            self.add_vertex(idx_edge[1])
            return True
        except:
            return False

    def add_vertex(self, v):
        if type(v) != int or type(v) != str:
            return False
        if type(v) == int:
            self.__n = max(v, self.__n)
        if type(v) == str:
            if not v in self.__v_name_to_idx:
                self.__v_idx_to_name[self.__n] = v
                self.__v_name_to_idx[v] = self.__n
                self.__n += 1
        return True

    def delete_edge(self, edge):
        if type(edge) != tuple:
            return False
        try:
            if type(edge[0]) == int:
                i = edge[0]
            else:
                if not edge[0] in self.__v_name_to_idx:
                    self.__v_name_to_idx[edge[0]] = self.__n
                    self.__v_idx_to_name[self.__n] = edge[0]
                    self.__n += 1
                i = self.__v_name_to_idx[edge[0]]
            if type(edge[1]) == int:
                j = edge[1]
            else:
                if not edge[1] in self.__v_name_to_idx:
                    self.__v_name_to_idx[edge[1]] = self.__n
                    self.__v_idx_to_name[self.__n] = edge[1]
                    self.__n += 1
                j = self.__v_name_to_idx[edge[1]]
            if len(edge) == 2:
                idx_edge = (i, j)
            else:
                idx_edge = (i, j, edge[2])
            if idx_edge in self.__adj:
                self.__adj.remove(idx_edge)
            if idx_edge in self.__edges:
                self.__edges.remove(idx_edge)
            if len(idx_edge) == 3:
                revert_edge = (idx_edge[1], idx_edge[0], idx_edge[2])
            else:
                revert_edge = (idx_edge[1], idx_edge[0])
            if revert_edge in self.__adj:
                self.__adj.remove(revert_edge)
            self.__m = len(self.__edges)
            return True
        except:
            return False

    def get_idx(self, name):
        if type(name) is str and name in self.__v_name_to_idx:
            return self.__v_name_to_idx[name]
        else:
            return -1

    def get_name(self, idx):
        if type(idx) is int and idx in self.__v_idx_to_name:
            return self.__v_idx_to_name[idx]
        else:
            return ''

    def get_matrix_adj(self):
        result = []
        for _ in range(self.__n):
            result.append([])
        for edge in self.__adj:
            result[edge[0]].append(edge[1])
        return result


