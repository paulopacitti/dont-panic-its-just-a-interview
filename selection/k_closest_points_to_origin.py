# description: https://www.junhaow.com/lc/problems/heap/973_k-closest-points-to-origin.html
# tags: amazon selection select

import math
import heapq

def k_closest(points, k):
    distances = []
    final_points = []
    for i in range(len(points)):
        current_distance = math.sqrt(((points[i][0])**2) + ((points[i][1])**2))
        distances.append(current_distance)
    
    distances.sort()
    max_distance = distances[k-1]
    for i in range(len(points)):
        if len(final_points) == k:
            break
        current_distance = math.sqrt(((points[i][0])**2) + ((points[i][1])**2))
        if current_distance <= max_distance:
            final_points.append(points[i])
    return final_points

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def k_closest_2(points, k):
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
    return points[:k]

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def k_closest_heap(points, k):
    points_heap = []
    for i in range(len(points)):
        current_distance = math.sqrt(((points[i][0])**2) + ((points[i][1])**2))
        heapq.heappush(points_heap, (-current_distance, points[i]))
        if len(points_heap) > k:
            heapq.heappop(points_heap)
    return [p[1] for p in points_heap]

# Time Complexity: O(n log k), and O(n log n in the worst case)
# Space Complexity: O(k)

def k_closest_quick_select(points, k):
    points = []
    for i in range(len(points)):
        current_distance = math.sqrt(((points[i][0])**2) + ((points[i][1])**2))
        points.append((current_distance, points[i]))
    quick_select(points, 0, len(points)-1, k)
    return [points[i][1] for i in range(0, k)]

def quick_select(array, left, right, k):
    while left < right:
        pivot = partition(array, left, right)
        if pivot < k:
            left = pivot + 1
        elif pivot > k:
            right = pivot - 1
        else:
            return

def partition(array, left, right):
    pivot = array[right]
    i = left
    for j in range(left, right):
        if array[j][0] <= pivot[0]:
            array[i], array[j] = array[j], array[i] # put all of the smaller elements than pivot in the left side of the array
            i += 1
    array[i], array[right] = array[right], array[i] # place pivot as the element right next to all elements smaller than it
    return i

# Time Complexity: Theta(n) = O(n) in the average, O(n²) in the worst case
# Space Complexity: O(n), where n is the number of points (to calculate the distance)

a = [[3,3],[5,-1],[-2,4],[12,-4], [-1,-2],[3,1]]
print(k_closest_quick_select(a, 2))
