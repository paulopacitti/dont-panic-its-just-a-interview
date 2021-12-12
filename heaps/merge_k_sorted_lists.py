# description: https://leetcode.com/problems/merge-k-sorted-lists/

import heapq

def merge_k_sorted_lists(lists):
    min_heap = []
    merged_list = []
    for _ in range(len(lists[0])):
        for k in lists:
            if len(k) > 0:
                heapq.heappush(min_heap, k.pop(0))
        for _ in range(len(min_heap)):
            merged_list.append(heapq.heappop(min_heap))

    return merged_list

l = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_sorted_lists(l))

# Time complexity: O(n log k), where n is the length 
# Space complexity: O(k)