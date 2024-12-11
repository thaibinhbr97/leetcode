from collections import defaultdict


def minReorder(n, connections):
    directedEdges = defaultdict(list)
    edges = defaultdict(list)
    visited = [False for i in range(n)]

    # set up to run DFS on node 0
    for u, v in connections:
        directedEdges[u].append(v)
        edges[u].append(v)
        edges[v].append(u)

    def dfs(city):
        nonlocal reversals
        visited[city] = True
        for neighbor in edges[city]:
            if not visited[neighbor]:
                # if the node has not been visited and in the directedEges dict, we will have to reverse the direction (by adding 1 to reversals count)
                if neighbor in directedEdges[city]:
                    reversals += 1
                dfs(neighbor)

    reversals = 0
    dfs(0)
    return reversals


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(minReorder(n, connections))  # 3

n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print(minReorder(n, connections))  # 2

n = 3
connections = [[1, 0], [2, 0]]
print(minReorder(n, connections))  # 0
