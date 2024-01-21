# description: https://leetcode.com/problems/k-closest-points-to-origin/

import math
import heapq

def kClosest(points, k):
    heap = []
    for p in points:
        heap.append([distance(p), p])

    heapq.heapify(heap)
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    return result

def distance(a):
    return math.sqrt((a[0] - 0)**2 + (a[1] - 0)**2)