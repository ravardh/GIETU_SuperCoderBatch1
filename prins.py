import sys

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None
        for v in key:
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = {v: None for v in self.graph}
        key = {v: sys.maxsize for v in self.graph}
        key[list(self.graph.keys())[0]] = 0
        mst_set = {v: False for v in self.graph}

        for _ in range(len(self.graph)):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v, weight in self.graph[u]:
                if not mst_set[v] and weight < key[v]:
                    parent[v] = u
                    key[v] = weight

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for v in parent:
            if parent[v] is not None:
                print(parent[v], "-", v, "\t", self.get_weight(parent[v], v))
    
    
