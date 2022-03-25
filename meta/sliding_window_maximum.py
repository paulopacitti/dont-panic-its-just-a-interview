# description: https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
def max_sliding_window(nums, k):
    left = right = 0
    queue = deque([])
    output = []
    
    while right < len(nums):
        while len(queue) > 0 and nums[queue[-1]] < nums[right]:
            queue.pop()
        
        queue.append(right)
        if queue[0] < left:
            queue.popleft()
            
        if (right - left + 1) >= k:
            output.append(nums[queue[0]])
            left += 1
        right += 1
    
    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_sliding_window(nums, k))

# Time complexity:  O(n)
# Space complexity: O(k), if k == n, O(n)