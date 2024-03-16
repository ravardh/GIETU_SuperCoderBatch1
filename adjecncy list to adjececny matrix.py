from typing import List

def convert_adjacency_list_to_matrix(adj_list: List[List[int]]) -> List[List[int]]:
    n = len(adj_list)
    matrix = [[0]*n for _ in range(n)]

    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            matrix[i][neighbor] = 1

    return matrix


T = int(input().strip())

for t in range(T):
    n = int(input().strip())

    adj_list = []

    for i in range(n):
        try:
            m, *neighbors = map(int, input().strip().split())
        except ValueError:
            print("Error: invalid input {}".format(i+1))
            continue

        adj_list.append(neighbors)

    if len(adj_list) < n:
        continue

    matrix = convert_adjacency_list_to_matrix(adj_list)

    for row in matrix:
        print(*row)

    print()