# description: https://leetcode.com/problems/merge-k-sorted-lists/

import heapq

def merge_k_sorted_lists(lists):
    min_heap = []
    merged_list = []
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heapq.heappush(min_heap, (lists[i].pop(0), i))
    while len(min_heap) > 0:
        element, origin = heapq.heappop(min_heap)
        merged_list.append(element)
        if len(lists[origin]) > 0:
            heapq.heappush(min_heap, (lists[origin].pop(0), origin))
    return merged_list

l = [[1,4,5],[1,3,4],[19,26]]
print(merge_k_sorted_lists(l))

# Time complexity: O(n log k), where n is the length 
# Space complexity: O(k)