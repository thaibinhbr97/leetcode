import time

import matplotlib.pyplot as plt
import numpy as np


def print_matrix(matrix):
    """Helper function to visualize the matrix"""
    for row in matrix:
        print(" ".join(f"{num:2}" for num in row))
    print("\n")


def plot_matrix(matrix, step, title=""):
    """Function to visualize the matrix with Matplotlib"""
    plt.clf()  # Clear previous frame
    plt.imshow(matrix, cmap="coolwarm", vmin=-1, vmax=1)  # Color map
    plt.title(f"Step {step}: {title}")
    plt.colorbar()

    # Add text labels for matrix elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            plt.text(j, i, str(matrix[i][j]), ha="center", va="center", color="black")

    plt.xticks(range(len(matrix[0])))
    plt.yticks(range(len(matrix)))
    plt.pause(1)  # Pause to show the frame


def setZeroes(matrix):
    """Modified version of the Set Matrix Zeroes algorithm to visualize steps"""
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    step = 1
    plot_matrix(matrix, step, "Initial Matrix")
    time.sleep(1)

    # Step 1: Mark rows and columns
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    step += 1
    plot_matrix(matrix, step, "Mark rows & cols")
    time.sleep(1)

    # Step 2: Apply zeroes based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    step += 1
    plot_matrix(matrix, step, "Apply zeroes")
    time.sleep(1)

    # Step 3: Handle first row and first column separately
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    step += 1
    plot_matrix(matrix, step, "Final Output")
    time.sleep(2)


# Example matrix
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

# Run animation
plt.figure(figsize=(5, 5))
setZeroes(matrix)
plt.show()
