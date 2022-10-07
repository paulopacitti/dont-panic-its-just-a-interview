# description: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# tags: "dynamic programming", "matrix"
# Solution:
# - We can check if we have a new square by checking if the current cell is 1 and
# if it's the bottom-right of a larger square.
# - To be part of a larger square, the top, left, and diagonal top-right must be
# nonzero. If they are, then the number of squares which the current cell is part
# of is the minimum number between these adjacent cells + 1, since  different
# values for these adjacent cells means that not all of them have are part of the
# same squares.


def is_bounded(matrix, row, column):
    expr_row = row >= 0 and (row < len(matrix))
    expr_column = column >= 0 and column < len(matrix[0])
    return expr_row and expr_column


def countSquares(matrix):
    table = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                table[i][j] = 0
            else:
                top = table[i - 1][j] if is_bounded(table, i - 1, j) else 0
                left = table[i][j - 1] if is_bounded(table, i, j - 1) else 0
                diagonal = table[i - 1][j - 1] if is_bounded(table, i - 1, j - 1) else 0
                table[i][j] = min(top, left, diagonal) + 1

    for i in range(len(table)):
        count += sum(table[i])

    return count


matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
print(countSquares(matrix))

# Time complexity: O(n*m), where n and m are the dimensions of the matrix
# Space complexity: O(n*m)
