# description: https://leetcode.com/problems/01-matrix/description/

def updateMatrix(mat):
    MAX_VALUE = 10**4 + 1
    queue = []
    coordinates = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # bottom-up: add the zeros to the queue to build distance matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = MAX_VALUE # add max-value possible because it's going to be updated with distance
    
    while queue:
        i, j = queue.pop(0)
        for c in coordinates:
            # if is bounded and the neighbor has a distance greater than a smaller distance, update and add
            # to the queue, because it can be used to update neighbours with smaller distances
            if is_bounded(mat, i + c[0], j + c[1]) and mat[i + c[0]][j + c[1]] > mat[i][j] + 1:
                mat[i + c[0]][j + c[1]] = mat[i][j] + 1
                queue.append((i + c[0], j + c[1]))
    return mat


def is_bounded(mat, i, j):
    return (i >= 0 and i < len(mat)) and (j >= 0 and j < len(mat[0]))

# Time complexity: O(m*n) (Since each cell in the matrix is processed once)
# Space complexity: O(m*n) (In the worst case, all cells might be added to the queue.)