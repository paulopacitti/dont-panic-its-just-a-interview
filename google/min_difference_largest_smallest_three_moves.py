# description: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Solution:
# - To solve the problem, we must remove 3 items from the array that will make the difference between the
# largest and the smallest the minimal as possible.
# - We say "remove" to say that we will make one of the two values (smallest and largest) to be the same as the
# other one.
# - That way, we can have the following solutions:
#   - Remove largest_1, largest_2, largest_3
#   - Remove smallest_1, smallest_2, smallest_3
#   - Remove largest_1, largest_2 and smallest_1
#   - Remove smallest_1, smallest_2 and largest_3
# - After the 3 moves, we will have the possible following differences (assume that is sorted):
#   - nums[-4] - nums[0] (4th largest - 1st smallest)
#   - nums[-3] - nums[1] (3th largest - 2nd smallest)
#   - nums[-2] - nums[2] (2nd largest - 3rd smallest)
#   - nums[-1] - nums[3] (1st largest - 4th smallest)
# - The best set of 3 moves will be the one with the minimal difference. The solution will be the minimum
# between these options.


import heapq
import math


def minDifference(nums):
    if len(nums) <= 4:
        return 0

    heapq.heapify(nums)
    smallest = heapq.nsmallest(4, nums)  # get the 4 smallest elements
    largest = heapq.nlargest(4, nums)  # get the 4 largest elements
    largest.reverse()  # sort in a ascending order

    _min = math.inf
    for i in range(4):
        _min = min(_min, largest[i] - smallest[i])
    return _min


array = [6, 6, 0, 1, 1, 4, 6]
print(minDifference(array))

# Time complexity: O(n) + O(n log 4) = O(n)
# Space complexity: O(1)
