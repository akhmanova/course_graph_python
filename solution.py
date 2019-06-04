# copy obj (not references)
from copy import deepcopy


class Graph:
    # count of vertexes
    __n = 0
    # count of edges
    __m = 0
    # list of adjacency (idx)
    __adj = []
    # list of adjacency (names)
    __names_adj = []
    # dict from v.name to v.index
    __v_name_to_idx = {}
    # dict from v.index to v.name
    __v_idx_to_name = {}
    # oriented flag
    __oriented = False

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
    #           adj=<adjacency list [(1, 2), (3, 4)]>,
    #           names_adj=<adjacency list of names [('apple', 'pear')]>,
    #           v_name_to_idx=<{'apple'=1, 'pear'=2}>
    #           v_idx_to_name=<{1='apple', 2='pear'}>
    #           oriented=<False or True>
    def __init__(self, **kwargs):

        # Copy from original graph
        if 'original_graph' in kwargs:
            self.__n = deepcopy(kwargs.original_graph.n)
            self.__m = deepcopy(kwargs.original_graph.m)
            self.__adj = deepcopy(kwargs.original_graph.adj)
            self.__names_adj = deepcopy(kwargs.original_graph.names_adj)
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
        if 'names_adj' in kwargs:
            self.__names_adj = deepcopy(kwargs.get('names_adj'))
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

    def get_names_adj(self):
        return self.__names_adj

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

    def set_adj(self, adj):
        try:
            adj = list(adj)
            for (i, j) in adj:
                if i < 0 or j < 0 or type(i) != int or type(j) != int:
                    raise Exception
        except Exception:
            return False
        self.__m = len(adj)
        self.__n = 0
        self.__adj = []
        for (i, j) in adj:
            self.__adj.append((i, j))
            if not self.__oriented:
                self.__adj.append((j, i))
        return True

    def set_names_adj(self, names_adj):
        try:
            names_adj = list(names_adj)
            for i in names_adj:
                if type(i) != tuple or len(i) != 2:
                    raise Exception
        except Exception:
            return False
        self.__m = len(names_adj)
        self.__n = 0
        self.__names_adj = []
        self.__adj = []
        for (i, j) in names_adj:
            if i in self.__v_name_to_idx:
                idx_i = self.__v_name_to_idx[i]
            else:
                idx_i = self.__n
                self.__n += 1
                self.__v_name_to_idx[i] = idx_i
                self.__v_idx_to_name[idx_i] = i
            if j in self.__v_name_to_idx:
                idx_j = self.__v_name_to_idx[j]
            else:
                idx_j = self.__n
                self.__n += 1
                self.__v_name_to_idx[j] = idx_j
                self.__v_idx_to_name[idx_j] = j
            self.__names_adj.append((i, j))
            self.__adj.append((idx_i, idx_j))
            if not self.__oriented:
                self.__names_adj.append((j, i))
                self.__adj.append((idx_j, idx_i))
        return True

    def set_v_name_to_idx(self):
        return self.__v_name_to_idx

    def set_v_idx_to_name(self):
        return self.__v_idx_to_name

    def set_oriented(self):
        return self.__oriented


g = Graph(n=2, m=2, adj=[(0, 1), (1,0)])
print(g.get_n())
g.set_n(3)
print( g.get_n())
print (g.set_n(3))
print (g.set_m(2))
print (g.set_adj([(0, 1), (1,0), (2, 3)]))
print( g.get_n())
print( g.get_m())
print (len((0, 1)))
print (g.set_names_adj([(0, 1), (1,0), (2, 3)]))
print( g.get_n())
print( g.get_m())
print (g.get_v_idx_to_name())


