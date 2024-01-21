# https://leetcode.com/problems/flood-fill

def floodFill( image, sr, sc, color):
    old_color = image[sr][sc]
    coordinates = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(sr, sc)]
    
    while queue:
        i, j = queue.pop(0)
        if image[i][j] == old_color:
            image[i][j] = color
        for c in coordinates:
            if is_bounded(image, i + c[0], j + c[1]) and image[i + c[0]][j + c[1]] == old_color:
                queue.append((i + c[0], j + c[1]))

    return image

def is_bounded(image, i, j):
    return i >= 0 and i < len(image) and j >= 0 and j < len(image[0])

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

floodFill(image, sr, sc, color)

# Space complexity: O(n)