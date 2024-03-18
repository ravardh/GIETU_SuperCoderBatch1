import heapq

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj_list = [[] for _ in range(v)]
        self.visited = set()

    def add_edge(self, s, d, w):
        self.adj_list[s - 1].append((s, d, w))
        self.adj_list[d - 1].append((d, s, w))

    def prim_mst(self):
        mst = []
        total_weight = 0
        start_vertex = 1
        self.visited.add(start_vertex)
        pq = [(weight, start_vertex, dest) for start, dest, weight in self.adj_list[start_vertex - 1]]
        heapq.heapify(pq)

        while pq:
            weight, src, dest = heapq.heappop(pq)
            if dest not in self.visited:
                mst.append((src, dest, weight))
                total_weight += weight
                self.visited.add(dest)
                for neighbor in self.adj_list[dest - 1]:
                    if neighbor[1] not in self.visited:
                        heapq.heappush(pq, (neighbor[2], neighbor[0], neighbor[1]))

        return mst, total_weight

g = Graph(4)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 20)
g.add_edge(2, 3, 30)
g.add_edge(2, 4, 5)

mst, total_weight = g.prim_mst()
for edge in mst:
    print(edge)
print(total_weight)