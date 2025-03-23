# def gameOfLife(board):
#     rows = len(board)
#     cols = len(board[0])

#     def isValid(r, c):
#         return 0 <= r < rows and 0 <= c < cols

#     directions = [
#         (-1, 0),  # up
#         (1, 0),  # down
#         (0, -1),  # left
#         (0, 1),  # right
#         (-1, -1),  # top left
#         (-1, 1),  # top right
#         (1, -1),  # bottom left
#         (1, 1),  # bottom right
#     ]
#     # 2->0 (alive->dead)
#     # 3->1 (dead->alive)
#     for r in range(rows):
#         for c in range(cols):
#             count = 0

#             for dr, dc in directions:
#                 ur = r + dr
#                 uc = c + dc
#                 # count live neighbors (both 1 and 2 representing originally alive cells)
#                 if isValid(ur, uc) and board[ur][uc] in [1, 2]:
#                     count += 1
#             if board[r][c] == 1:
#                 if count < 2 or count > 3:
#                     board[r][c] = 2  # mark to die
#             elif board[r][c] == 0:
#                 if count == 3:
#                     board[r][c] = 3  # mark to live
#     for r in range(rows):
#         for c in range(cols):
#             if board[r][c] == 2:
#                 board[r][c] = 0
#             elif board[r][c] == 3:
#                 board[r][c] = 1


def gameOfLife(board):
    ROWS = len(board)
    COLS = len(board[0])

    def isValid(r, c):
        return 0 <= r < ROWS and 0 <= c < COLS

    dr = [-1, 0, 1]
    dc = [-1, 0, 1]
    # 4 cases: alive->dead(1->0:2), alive->alive(1->1), dead->dead(0->0), dead->alive(0->1: 3)
    # at the end, we will change 2 to 0 (since alive->dead) and 3 to 1 (since dead->alive)
    for r in range(ROWS):
        for c in range(COLS):
            count = 0  # count living neighbors
            for i in range(3):
                for j in range(3):
                    # move up horizontal, vertical and diagonal
                    ur = r + dr[i]
                    uc = c + dc[j]
                    if i == 1 and j == 1:
                        continue  # skip if it stays at the same location
                    if isValid(ur, uc) and board[ur][uc] in [1, 2]:
                        count += 1
            # check four rules
            if board[r][c] == 1:
                if not (2 <= count <= 3):
                    board[r][c] = 2  # alive->dead(2)
            elif board[r][c] == 0:
                if count == 3:
                    board[r][c] = 3  # dead->alive(3)
    # now board will have 0, 1, 2, 3 -> convert original board to the solution
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == 3:
                board[r][c] = 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [[1, 1], [1, 0]]
print(gameOfLife(board))  # [[1,1],[1,1]]
