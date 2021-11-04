# description: https://www.hackerrank.com/challenges/find-the-running-median

import heapq

def running_median(a):
    upper_heap = []
    lower_heap = []
    heapq.heappush(upper_heap, a[0])
    medians = []
    medians.append(float(a[0]))
    for i in range(1, len(a)):
        current = a[i]
        middle = upper_heap[0]
        if current >= middle:
            heapq.heappush(upper_heap, current)
        else:
            heapq.heappush(lower_heap, -current)
        
        # balance heaps
        if len(lower_heap) > len(upper_heap):
            heapq.heappush(upper_heap, -heapq.heappop(lower_heap))
        if len(upper_heap) > len(lower_heap) + 1: # upper heap will always have more elements in case of odd number of elements
            heapq.heappush(lower_heap, -heapq.heappop(upper_heap))
            
        if (len(upper_heap) + len(lower_heap)) % 2 == 1: # odd length
            medians.append(float(upper_heap[0]))
        else: # even length
            medians.append((float(upper_heap[0]) + (-lower_heap[0]))/2)
        
    return medians

test0 = [1,2,3,4,5,6,7,8,9,10]
running_median(test0)

# Time complexity: n*O(log n)=O(n log n) to mantain both heaps
# Space complexity: O(n) elements distributed in the heaps