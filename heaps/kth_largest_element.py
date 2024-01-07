# description: https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

def findKthLargest(self, nums, k):
    kth_largest = 0
    negative = [-i for i in nums]
    heapq.heapify(negative)
    for i in range(k):
        kth_largest = heapq.heappop(negative)
    return -kth_largest
    
    