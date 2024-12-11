def findCircleNum(isConnected):
    # T: O(n^2)
    # S: O(n)
    # isConnected is adjacency matrix n x n
    n = len(isConnected)
    visited = [False for i in range(n)]
    provinces = 0

    def dfs(src, visited, isConnected):
        s = [src]
        visited[src] = True
        while s:
            u = s.pop()
            for v in range(len(isConnected[u])):
                if isConnected[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    s.append(v)

    for city in range(n):
        if not visited[city]:
            dfs(city, visited, isConnected)
            # after dfs from each city, it will group it as a province
            provinces += 1
    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))  # 2


isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))  # 3
