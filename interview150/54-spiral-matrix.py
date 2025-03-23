def spiralOrder(matrix):
    # # Time: O(mxn)
    # # Space: O(mxn)
    # res = []
    # rows = len(matrix)
    # cols = len(matrix[0])
    # visited = [False for i in range(rows * cols)]
    # r = 0
    # c = 0
    # while len(res) < rows * cols:
    #     # move left to right
    #     while c < cols and not visited[r * cols + c]:
    #         res.append(matrix[r][c])
    #         visited[r * cols + c] = True
    #         c += 1
    #     c -= 1

    #     # move downwards
    #     r += 1
    #     while r < rows and not visited[r * cols + c]:
    #         res.append(matrix[r][c])
    #         visited[r * cols + c] = True
    #         r += 1
    #     r -= 1

    #     # move right to left
    #     c -= 1
    #     while c >= 0 and not visited[r * cols + c]:
    #         res.append(matrix[r][c])
    #         visited[r * cols + c] = True
    #         c -= 1
    #     c += 1

    #     # move upwards
    #     r -= 1
    #     while r >= 0 and not visited[r * cols + c]:
    #         res.append(matrix[r][c])
    #         visited[r * cols + c] = True
    #         r -= 1

    #     # modify a starting point for inner spiral order
    #     r += 1
    #     c += 1
    # return res

    rows, cols = len(matrix), len(matrix[0])
    c, r, dc, dr = 0, 0, 1, 0
    res = []
    for _ in range(rows * cols):
        res.append(matrix[r][c])
        matrix[r][c] = "."
        if (
            not 0 <= c + dc < cols
            or not 0 <= r + dr < rows
            or matrix[r + dr][c + dc] == "."
        ):
            dc, dr = -dr, dc

        r += dr
        c += dc
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))  # [1,2,3,6,9,8,7,4,5]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix))  # [1,2,3,4,8,12,11,10,9,5,6,7]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24],
]
print(
    spiralOrder(matrix)
)  # [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
