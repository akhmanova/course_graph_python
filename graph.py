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
    def __init__(self, kwargs={}):

        # Copy from original graph
        if 'original_graph' in kwargs:
            self.__n = deepcopy(kwargs.get('original_graph').get_n())
            self.__m = deepcopy(kwargs.get('original_graph').get_m())
            self.__adj = deepcopy(kwargs.get('original_graph').get_adj())
            self.__edges = deepcopy(kwargs.get('original_graph').get_edges())
            self.__v_name_to_idx = deepcopy(kwargs.get('original_graph').get_v_name_to_idx())
            self.__v_idx_to_name = deepcopy(kwargs.get('original_graph').get_v_idx_to_name())
            print ("A class was created from the sample!")
            return 
        
        if 'n' in kwargs:
            self.set_n(deepcopy(kwargs.get('n')))
        if 'm' in kwargs:
            self.set_m(deepcopy(kwargs.get('m')))
        if 'edges' in kwargs:
            self.set_edges(deepcopy(kwargs.get('edges')))
        if 'v_name_to_idx' in kwargs:
            self.set_v_name_to_idx(deepcopy(kwargs.get('v_name_to_idx')))
        if 'v_idx_to_name' in kwargs:
            self.set_v_idx_to_name(deepcopy(kwargs.get('v_idx_to_name')))
        if 'oriented' in kwargs:
            self.set_oriented(deepcopy(kwargs.get('oriented')))

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
        self.__n = n
        return True

    def set_m(self, m):
        try:
            m = int(m)
        except Exception:
            return False
        if m < 0 or len(self.__adj) != m:
            return False
        self.__m = m
        return True

    def set_edges(self, adj):
        self.__m = 0
        self.__n = 0
        self.__adj = []
        self.__edges = []

        for i in adj:
            self.add_edge(i)
        self.__m = len(self.__edges)
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
        if type(edge) is not tuple:
            return False
        if type(edge[0]) is int:
            self.__n = max(self.__n, edge[0] + 1, edge[1] + 1)
            return self.add_edge_idx(edge)
        return self.add_edge_str(edge)

    def add_edge_str(self, edge):
        if edge[0] not in self.__v_name_to_idx:
            while self.__n in self.__v_idx_to_name:
                self.__n += 1
            idx0 = self.__n
            self.__v_name_to_idx[edge[0]] = idx0
            self.__v_idx_to_name[idx0] = edge[0]
            self.__n += 1
        else:
            idx0 = self.__v_name_to_idx[edge[0]]
        if edge[1] not in self.__v_name_to_idx:
            while self.__n in self.__v_idx_to_name:
                self.__n += 1
            idx1 = self.__n
            self.__v_name_to_idx[edge[1]] = idx1
            self.__v_idx_to_name[idx1] = edge[1]
            self.__n += 1
        else:
            idx1 = self.__v_name_to_idx[edge[1]]
        if len(edge) is 3:
            result = (idx0, idx1, edge[2])
        else:
            result = (idx0, idx1)
        return self.add_edge_idx(result)

    def add_edge_idx(self, edge):
        try:
            while self.__n in self.__v_idx_to_name:
                self.__n += 1
            self.__n = max(self.__n, edge[0] + 1, edge[1] + 1)
            idx = [min(edge[0], edge[1]), max(edge[0], edge[1])]
            if len(edge) == 2:
                res = (idx[0], idx[1])
            else:
                res = (idx[0], idx[1], edge[2])
            if not self.__oriented and  res not in self.__edges:
                self.__edges.append(res)
                self.__m = len(self.__edges)
            if self.__oriented and edge not in self.__edges:
                self.__edges.append(edge)
                self.__m = len(self.__edges)
            return True
        except:
            return False

    def add_vertex(self, v):

        if not v in self.__v_name_to_idx:
            self.__v_idx_to_name[self.__n] = v
            self.__v_name_to_idx[v] = self.__n
            self.set_n(self.__n + 1)
            return True
        else:
            return False

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

    def delete_vertex(self, v):
        if type(v) is str:
            if v not in self.__v_name_to_idx:
                return False
            v = self.__v_name_to_idx[v]
        if v >= self.__n:
            return False

        for i in self.__edges:
            if i[0] is v or i[1] is v:
                self.delete_edge(i)
        if v in self.__v_idx_to_name:
            self.__v_name_to_idx.pop(self.__v_idx_to_name[v])
            self.__v_idx_to_name.pop(v)
        return True

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
        for edge in self.__edges:
            result[edge[0]].append(edge[1])
            if not self.__oriented:
                result[edge[1]].append(edge[0])
        return result

    def find_path(self, v):
        if type(v) is str:
            v = self.__v_name_to_idx[v]

        temp_path = []
        cur = v
        flag = True
        temp_path.append(self.__v_idx_to_name[cur])

        while flag:
            flag = False
            for i in self.__edges:
                if i[1] == cur:
                    flag = True
                    cur = i[0]
                    temp_path.append(self.__v_idx_to_name[cur])

        temp_path.reverse()
        return temp_path



