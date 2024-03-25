class DisjointSet:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0] * n

  def find(self, u):
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

  def union(self, u, v):
    pu, pv = self.find(u), self.find(v)
    if pu == pv:
      return False
    if self.rank[pu] < self.rank[pv]:
      self.parent[pu] = pv
    elif self.rank[pu] > self.rank[pv]:
      self.parent[pv] = pu
    else:
      self.parent[pv] = pu
      self.rank[pu] += 1
    return True

def kruskalMST(n, edges):
  edges.sort(key = lambda x: x[2])    # sort based on weight
  s = DisjointSet(n)
  mst = 0
  for u, v, w in edges:
      if s.union(u-1, v-1):
          mst += w
  return mst

def testcases():
  tc = {
    "1": {
      'n': 5, 'm': 6,
      'edges': [[1, 2, 6], [2, 3, 5], [3, 4, 4], [1, 4, 1], [1, 3, 2], [3, 5, 3]]
    }
  }
  # inp = input("Choose Testcase[1/2]: ")
  inp = "1"
  print(f"Testcase #{inp}:\nVertices: {tc[inp]['n']}\tEdges: {tc[inp]['m']}\nEdge List: {tc[inp]['edges']}")
  print(kruskalMST(tc[inp]["n"], tc[inp]["edges"]))

if __name__ == '__main__':
  testcases()
  # n = int(input())
  # m = int(input())
  # edges = []
  # for i in range(m):
  #   u, v, w = map(int, input().split())
  #   edges.append([u, v, w])
  # print(kruskalMST(n, edges))
