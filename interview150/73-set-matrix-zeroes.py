import copy


def setZeroes(matrix):
    # Time: O(m*n)
    # Space: O(m*n)
    # m, n = len(matrix), len(matrix[0])
    # temp_matrix = copy.deepcopy(matrix)
    # for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j] == 0:
    #             # zero out the row
    #             for k in range(n):
    #                 temp_matrix[i][k] = 0
    #             # zero out the col
    #             for k in range(m):
    #                 temp_matrix[k][j] = 0
    # # copy modified matrix back to the original
    # for i in range(m):
    #     for j in range(n):
    #         matrix[i][j] = temp_matrix[i][j]
    # print(matrix)
    # return

    # Using two sets to maintain indicies of rows or cols that should be zeroed
    # Time: O(m*n)
    # Space: O(m+n)
    # m = len(matrix)
    # n = len(matrix[0])
    # zero_rows = set()
    # zero_cols = set()

    # for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j] == 0:
    #             zero_rows.add(i)
    #             zero_cols.add(j)
    # # update matrix based on identified rows and cols
    # for i in range(m):
    #     for j in range(n):
    #         if i in zero_rows or j in zero_cols:
    #             matrix[i][j] = 0
    # print(matrix)
    # return

    """
    Modify the input matrix in place such that if an element is 0, its entire row and column are set to 0
    Time: O(m*n)
    Space: O(1)
    """
    m = len(matrix)
    n = len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    # step 1: mark rows and cols that should be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0  # mark col j
                matrix[i][0] = 0  # mark row i
    # step 2: zero out elements based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    # step 3: handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # step 4: handle first column
    if first_col_zero:
        for i in range(i):
            matrix[i][0] = 0
    print(matrix)
    return


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setZeroes(matrix))  # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeroes(matrix))  # [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
