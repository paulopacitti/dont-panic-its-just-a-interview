# description: https://leetcode.ca/2021-04-14-1762-Buildings-With-an-Ocean-View/
# tags: greedy

def ocean_view(heights):
    best_buildings =  [len(heights)-1]
    tallest = 0
    for i in range(len(heights)-2, -1, -1):
        if heights[i] > tallest:
            best_buildings.append(i)
            tallest = heights[i]
    return best_buildings[::-1];

beach = [4,3,2,1]
print(ocean_view(beach))

# Time complexity: O(n)
# Space complexity: O(1)