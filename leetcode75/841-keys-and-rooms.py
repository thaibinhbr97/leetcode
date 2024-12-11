def canVisitAllRooms(rooms):
    n = len(rooms)
    visited = [False for i in range(n)]

    def dfs(source, rooms, visited):
        s = []
        visited[source] = True
        s.append(source)
        while s:
            u = s.pop()
            for v in rooms[u]:
                if not visited[v]:
                    visited[v] = True
                    s.append(v)

    dfs(0, rooms, visited)
    for v in visited:
        if v == False:
            return False
    return True


def canVisitAllRooms(rooms):

    n = len(rooms)
    visited = [False for i in range(n)]

    def dfs(s):
        # mark the room as visited
        visited[s] = True
        # visit all rooms accessible with keys in the current room
        for v in rooms[s]:
            if not visited[v]:
                dfs(v)

    # dfs from room 0
    dfs(0)
    for v in visited:
        if v == False:
            return False
    return True


def canVisitAllRooms(rooms):

    n = len(rooms)
    visited = set()

    def dfs(room):
        # add the room to visited set
        visited.add(room)
        # visit all rooms accessible with keys in the current room
        for key in rooms[room]:
            if key not in visited:
                dfs(key)

    # dfs from room 0
    dfs(0)
    return len(visited) == len(rooms)


rooms = [[1], [2], [3], []]
print(canVisitAllRooms(rooms))  # true

rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))  # false
