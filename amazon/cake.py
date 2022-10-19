# description: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# Cij = (h[i] - h[i-1])*(w[j] - w[j-1])
def naive_maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.sort()
    verticalCuts.sort()
    horizontalCuts.append(h)
    verticalCuts.append(w)
    verticalCuts.insert(0, 0)
    horizontalCuts.insert(0, 0)
    max_cut = -(10**9) + 7

    for i in range(1, len(horizontalCuts)):
        for j in range(1, len(verticalCuts)):
            area = (horizontalCuts[i] - horizontalCuts[i - 1]) * (
                verticalCuts[j] - verticalCuts[j - 1]
            )
            max_cut = max(max_cut, area)
    return max_cut % (10**9 + 7)


# The maximum cut will always be the one with the largest height and largest width
def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.sort()
    verticalCuts.sort()
    horizontalCuts.append(h)
    verticalCuts.append(w)
    verticalCuts.insert(0, 0)
    horizontalCuts.insert(0, 0)
    max_height = 0
    max_width = 0

    for i in range(1, len(horizontalCuts)):
        max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
    for i in range(1, len(verticalCuts)):
        max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

    return (max_height * max_width) % (10**9 + 7)


h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
print(maxArea(h, w, horizontalCuts, verticalCuts))

# Time complexity: O(nlogn), sorting
# Space complexity: O(1)
