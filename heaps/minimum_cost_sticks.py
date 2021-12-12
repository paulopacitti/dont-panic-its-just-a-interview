# description: https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

import heapq

def minimum_cost(sticks_available):
    cost = 0
    heapq.heapify(sticks_available)
    while len(sticks_available) > 0:
        one = heapq.heappop(sticks_available)
        two = heapq.heappop(sticks_available)
        cost += one + two
        if len(sticks_available) > 0:
            heapq.heappush(sticks_available, one + two)
    return cost

a = [4,3,2,6]
print(minimum_cost(a))

# Time Complexity: O(n log n), where n is the number of sticks available in the input, because of the heap operations
# Space Complexity: O(1)