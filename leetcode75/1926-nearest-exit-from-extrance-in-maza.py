"""
.: empty cell
+: wall

start from an entrance and use bfs to traverse through empty cell to find an exit which is an empty cell
on the edge of the maze
-> need a isValid function that consider if a cell is valid (on the edge of the maze) or not
"""

from queue import deque


def nearestExit(maze, entrace):
    # rows = len(maze)  # of rows
    # cols = len(maze[0])  # of cols
    # dr = [-1, 1, 0, 0]
    # dc = [0, 0, -1, 1]
    # sR, sC = entrance

    # def isValid(r, c):
    #     return r in range(rows) and c in range(cols)

    # def isExit(r, c):
    #     return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

    # def bfs(r, c, d):
    #     q = deque([(r, c, d)])
    #     maze[r][c] = "+"
    #     while q:
    #         ur, uc, distance = q.popleft()
    #         for i in range(4):
    #             r = ur + dr[i]
    #             c = uc + dc[i]
    #             if isValid(r, c):
    #                 if maze[r][c] == ".":
    #                     if isExit(r, c):
    #                         return distance + 1
    #                     maze[r][c] = "+"
    #                     q.append([r, c, distance + 1])
    #     return -1

    # return bfs(sR, sC, 0)

    rows = len(maze)
    cols = len(maze[0])
    sr, sc = entrance  # source row, source column
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def isValid(r, c):
        return r in range(rows) and c in range(cols)

    def onEdge(r, c):
        return r == 0 or c == 0 or r == rows - 1 or c == cols - 1

    def bfs(r, c, d):
        q = deque()
        q.append((r, c, d))
        maze[r][c] = "+"
        while q:
            ur, uc, distance = q.popleft()
            for i in range(4):
                r = ur + dr[i]
                c = uc + dc[i]
                if isValid(r, c) and maze[r][c] == ".":
                    if onEdge(r, c):
                        return distance + 1
                    maze[r][c] = "+"
                    q.append((r, c, distance + 1))
        return -1

    return bfs(sr, sc, 0)


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
# print(nearestExit(maze, entrance))  # 1

maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]
# print(nearestExit(maze, entrance))  # 2

maze = [[".", "+"]]
entrance = [0, 0]
print(nearestExit(maze, entrance))  # -1
