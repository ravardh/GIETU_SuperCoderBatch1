# Graph Theory Notes

## Introduction to Graph Theory

Graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A graph consists of a set of vertices (also called nodes or points) and a set of edges (also called links or lines) connecting these vertices.

### Basic Definitions

- **Graph**: A graph G is an ordered pair (V, E) comprising a set V of vertices or nodes together with a set E of edges or arcs.
- **Vertex**: A vertex (plural: vertices) is a fundamental unit of a graph. It represents an entity or a point in a graph.
- **Edge**: An edge is a link connecting two vertices in a graph. It represents a relationship or connection between the entities represented by the vertices.
- **Directed Graph**: A graph in which edges have a direction associated with them.
- **Undirected Graph**: A graph in which edges have no direction associated with them.

## Data Structures for Graph Representation

### Adjacency Matrix

An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.

Example of an adjacency matrix for an undirected graph:

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 0 | 1 |
| B | 1 | 0 | 1 | 1 |
| C | 0 | 1 | 0 | 0 |
| D | 1 | 1 | 0 | 0 |

### Adjacency List

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a vertex in the graph.

Example of an adjacency list for an undirected graph:

```
A -> B, D
B -> A, C, D
C -> B
D -> A, B
```