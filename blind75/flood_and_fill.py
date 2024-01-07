# https://leetcode.com/problems/flood-fill

def floodFill(image, sr: int, sc: int, color: int):
    queue = [(sr, sc)]
    i, j = sr, sc
    old_color = image[i][j]
    visited = set()
    while queue:
        i, j = queue.pop(0)
        if not is_out_of_bounds(image, i, j) and (i,j) not in visited:
            if image[i][j] == old_color:
                image[i][j] = color
                queue.append((i + 1, j))
                queue.append((i, j + 1))
                queue.append((i - 1, j))
                queue.append((i, j - 1))
        visited.add((i, j))
    return image

def is_out_of_bounds(image, row, column):
    return (row < 0 or row >= len(image)) or (column < 0 or column >= len(image[0]))