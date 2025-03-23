def isValidSudoku(board):
    # # Time: O(n^2), n = 9 => O(1)
    # # Space: O(n)
    # n = len(board)
    # # check each row if it contains duplicate values
    # checker = [False for i in range(n + 1)]
    # for i in range(n):
    #     tempRow = checker.copy()
    #     for j in range(n):
    #         # if digit appears previously in tempRow
    #         if board[i][j] == ".":
    #             continue
    #         if tempRow[int(board[i][j])] == True:
    #             return False
    #         tempRow[int(board[i][j])] = True
    # # check each column if it contains duplicate values
    # for i in range(n):
    #     tempCol = checker.copy()
    #     for j in range(n):
    #         # if digit appears previously in tempCol
    #         if board[j][i] == ".":
    #             continue
    #         if tempCol[int(board[j][i])] == True:
    #             return False
    #         tempCol[int(board[j][i])] = True
    # # check each sub board 3x3 if it contains duplicate values
    # for i in range(0, n, 3):
    #     for j in range(0, n, 3):
    #         tempBox = checker.copy()
    #         for k in range(3):
    #             for l in range(3):
    #                 if board[i + k][j + l] == ".":
    #                     continue
    #                 if tempBox[int(board[i + k][j + l])] == True:
    #                     return False
    #                 tempBox[int(board[i + k][j + l])] = True
    # return True

    # # Time: O(1)
    # # Space: O(1)
    # rows = [set() for _ in range(9)]
    # cols = [set() for _ in range(9)]
    # boxes = [set() for _ in range(9)]

    # for r in range(9):
    #     for c in range(9):
    #         num = board[r][c]
    #         if num == ".":
    #             continue  # skip empty cells
    #         box_index = (r // 3) * 3 + (c // 3)  # compute sub-box index
    #         # check if number already exists in row, col, or box
    #         if num in rows[r] or num in cols[c] or num in boxes[box_index]:
    #             return False
    #         rows[r].add(num)
    #         cols[c].add(num)
    #         boxes[box_index].add(num)
    # return True

    rows = [[False] * 10 for i in range(9)]
    cols = [[False] * 10 for i in range(9)]
    boxes = [[False] * 10 for i in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            num = int(num)
            box_index = (r // 3) * 3 + (c // 3)
            if rows[r][num] or cols[c][num] or boxes[box_index][num]:
                return False
            rows[r][num] = True
            cols[c][num] = True
            boxes[box_index][num] = True

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))  # true

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))  # false

board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]
print(isValidSudoku(board))  # false


board = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
print(isValidSudoku(board))  # false
