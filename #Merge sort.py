#Merge sort
def mergeSort(A):
    if len(A) < 2:
        return A
    mid = int(len(A)/2)
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])
    r,l = 0,0
    B = []
    while len(B) < len(A):
        if r >= len(right) or (l < mid and left[l] < right[r]):
            B.append(left[l])
            l += 1
        elif r < len(right):
            B.append(right[r])
            r += 1

    return B
A=eval(input("Enter a list of elements for sorting: "))
print(mergeSort(A))class Graph:
     
    adj = []
 
    # Function to fill empty adjacency matrix
    def __init__(self, v, e):
         
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)] 
                        for j in range(v)]
 
    # Function to add an edge to the graph
    def addEdge(self, start, e):
         
        # Considering a bidirectional edge
        Graph.adj[start][e] = 1