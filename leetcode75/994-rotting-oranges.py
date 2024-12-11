"""
m x n grid
0; empty cell
1: fresh orange
2: rotten orange
4 directionally adjacent to rotten orange becomes rotten

return # of minutes until no cell has a fresh orange
if not possible, return -1

example 1:
2 1 1
1 1 0
0 1 1

2 2 2
2 2 0
0 2 2
-> 4

example 2:
2 2 2
0 2 2
1 0 2
-> -1 

example 3:
0 2
-> 0 
"""

from collections import deque


def orangeRotting(grid):
    # # Initial Solution
    # rows = len(grid)
    # cols = len(grid[0])
    # dr = [0, 0, 1, -1]
    # dc = [1, -1, 0, 0]
    # q = deque()

    # def isValid(r, c):
    #     return r in range(rows) and c in range(cols)

    # def bfs(minutes):
    #     # using multi-source bfs on rottenOranges
    #     nonlocal freshOranges
    #     while q:
    #         flag = False
    #         for i in range(len(q)):
    #             ur, uc = q.popleft()
    #             for i in range(4):
    #                 r = ur + dr[i]
    #                 c = uc + dc[i]
    #                 if isValid(r, c) and grid[r][c] == 1:
    #                     grid[r][c] = 2
    #                     freshOranges -= 1
    #                     q.append((r, c))
    #                     if not flag:
    #                         flag = True
    #         if flag:
    #             minutes += 1
    #     return minutes

    # def setUp(grid):
    #     # count freshOranges and append rottenOranges to the queue
    #     nonlocal freshOranges
    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == 1:
    #                 freshOranges += 1
    #             if grid[row][col] == 2:
    #                 q.append((row, col))

    # freshOranges = 0
    # setUp(grid)
    # minutes = bfs(0)

    # return -1 if freshOranges > 0 else minutes

    # Second Solution
    # rows = len(grid)
    # cols = len(grid[0])
    # dr = [0, 0, 1, -1]
    # dc = [1, -1, 0, 0]
    # q = deque()

    # def isValid(r, c):
    #     return r in range(rows) and c in range(cols)

    # def bfs(minutes):
    #     # using multi-source bfs on rottenOranges
    #     nonlocal freshOranges
    #     while q:
    #         for i in range(len(q)):
    #             ur, uc, time = q.popleft()
    #             for i in range(4):
    #                 r = ur + dr[i]
    #                 c = uc + dc[i]
    #                 if isValid(r, c) and grid[r][c] == 1:
    #                     grid[r][c] = 2
    #                     freshOranges -= 1
    #                     # add newly rottenOrange to the queue with incremented time
    #                     q.append((r, c, time + 1))
    #                     # update minutes to rot all oranges
    #                     minutes = time + 1
    #     return minutes

    # def setUp(grid):
    #     # count freshOranges and append rottenOranges to the queue
    #     nonlocal freshOranges
    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == 1:
    #                 freshOranges += 1
    #             if grid[row][col] == 2:
    #                 q.append((row, col, 0))

    # freshOranges = 0
    # setUp(grid)
    # minutes = bfs(0)

    # return -1 if freshOranges > 0 else minutes

    # Third Solution
    rows = len(grid)
    cols = len(grid[0])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = deque()

    def isValid(r, c):
        return r in range(rows) and c in range(cols)

    def bfs(minutes):
        # using multi-source bfs on rottenOranges
        nonlocal freshOranges
        while q and freshOranges > 0:
            for i in range(len(q)):
                ur, uc = q.popleft()
                for i in range(4):
                    r = ur + dr[i]
                    c = uc + dc[i]
                    if isValid(r, c) and grid[r][c] == 1:
                        grid[r][c] = 2
                        freshOranges -= 1
                        q.append((r, c))
            minutes += 1
        return minutes

    def setUp(grid):
        # count freshOranges and append rottenOranges to the queue
        nonlocal freshOranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshOranges += 1
                if grid[row][col] == 2:
                    q.append((row, col))

    freshOranges = 0
    setUp(grid)
    minutes = bfs(0)

    return -1 if freshOranges > 0 else minutes

    # ChatGPT solution
    # rows, cols = len(grid), len(grid[0])
    # queue = deque()
    # fresh_count = 0

    # # Initialize the queue with all rotten oranges and count fresh oranges
    # for r in range(rows):
    #     for c in range(cols):
    #         if grid[r][c] == 2:
    #             queue.append((r, c, 0))  # (row, column, time)
    #         elif grid[r][c] == 1:
    #             fresh_count += 1

    # # If there are no fresh oranges, return 0 immediately
    # if fresh_count == 0:
    #     return 0

    # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # minutes = 0

    # # BFS to spread the rot
    # while queue:
    #     x, y, time = queue.popleft()
    #     for dx, dy in directions:
    #         nx, ny = x + dx, y + dy

    #         # Check if the neighboring cell is a fresh orange
    #         if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
    #             # Rot the orange
    #             grid[nx][ny] = 2
    #             fresh_count -= 1
    #             # Add the newly rotten orange to the queue with incremented time
    #             queue.append((nx, ny, time + 1))
    #             # Update the minutes taken to rot all oranges
    #             minutes = time + 1

    # # If there are still fresh oranges left, return -1
    # return -1 if fresh_count > 0 else minutes


# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# print(orangeRotting(grid))  # 4
# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# print(orangeRotting(grid))  # -1
# grid = [[0, 2]]
# print(orangeRotting(grid))  # 0
"""
2 1 1
1 1 1
0 1 2
=>
2 2 2
2 2 2
0 2 2

"""
grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
print(orangeRotting(grid))  # 2
