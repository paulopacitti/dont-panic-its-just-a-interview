def print_spiral(matrix):
    result = print_spiral_util(matrix, 0, 0, len(matrix), len(matrix[0]), [])
    return result

def print_spiral_util(matrix, start_row, start_column, end_row, end_column, result):
    if start_row >= end_row or start_column >= end_column:
        return
    # Print First Row
    for j in range(start_column, end_column):
        result.append(matrix[start_row][j])
 
    # Print Last Column
    for i in range(start_row + 1, end_row):
        result.append(matrix[i][end_column - 1])
 
    # Print Last Row, if Last and first Row are not same
    for j in range(end_column - 2, start_column - 1, -1):
        result.append(matrix[end_row - 1][j])
 
    # Print First Column, if Last and # First Column are not same
    for i in range(end_row - 2, start_row, -1):
        result.append(matrix[i][start_column])
 
    print_spiral_util(matrix, start_row  + 1, start_column + 1, end_row - 1, end_column - 1, result)
    return result

a = [[1, 2, 3, 4, 20],
     [5, 6, 7, 8, 21],
     [25, 26, 27, 28, 23],
     [9, 10, 11, 12, 24],
     [13, 14, 15, 16, 255]]
 
print(print_spiral(a))
