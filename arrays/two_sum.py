# problem link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
def two_sum(nums, target):
    nums_hash = {}  # { <value>: <index of the value>, ... }
    result = [] # result array
    for i in range(len(nums)):
        # the second term of the addition is the difference between the target and the first term;
        second_term = target - nums[i] 
        if second_term in nums_hash:
            # if second_term is in the hash, then we can conclude 
            # that it appears early in the original "nums" array;
            result = [nums_hash[second_term], i]
            return result
        else:
            # then we add to the hash, so it can be accessed faster;
            nums_hash[nums[i]] = i

nums = [int(e) for e in input().split()]
target = int(input())
print(two_sum(nums, target))