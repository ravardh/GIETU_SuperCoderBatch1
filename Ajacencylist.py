class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self):
        self.graph = {}

    # Add edges
    def add_edge(self, s, d):
        if s not in self.graph:
            self.graph[s] = AdjNode(d)
        else:
            node = AdjNode(d)
            node.next = self.graph[s]
            self.graph[s] = node

    # Print the graph
    def print_agraph(self):
        for vertex in self.graph:
            print("Vertex " + str(vertex) + ":", end="")
            temp = self.graph[vertex]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (1, 9), (2, 1), (2, 4), (3, 1), (3, 4), (3, 5), (3, 7), (4, 2), (4, 6), (5, 3), (5, 6), (6, 4), (6, 5), (6, 7), (8, 7), (8, 9), (9, 8), (9, 1)]

    # Create graph and add edges
    graph = Graph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.print_agraph()