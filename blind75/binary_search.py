# https://leetcode.com/problems/binary-search

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1