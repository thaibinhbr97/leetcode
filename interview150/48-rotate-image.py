def rotate(matrix):
    n = len(matrix)
    # we need to transpose the matrix and reverse each row to achieve the result
    # transpose by swapping across diagonal
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for i in range(n):
        matrix[i].reverse()
    print(matrix)
    return


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))  # [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate(matrix))  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
