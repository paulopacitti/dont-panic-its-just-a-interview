# description: https://leetcode.com/problems/subarray-sum-equals-k/submissions/
def subarray_sum_naive(nums, k):
    sums = 0
    for i in range(len(nums)):
        current = 0
        for j in range(i, len(nums)):
            current += nums[j]
            if current == k:
                sums += 1
    return sums

# Time complexity: O(n^2), where n is the number o items in the list
# Space complexity: O(1), no extra space required


def subarray_sum(nums, k):
    previous_sums_dict = {}
    sums = 0
    current = 0
   
    for i in range(len(nums)): 
        current += nums[i]
   
        if current == k: 
            sums += 1        
        if (current - k) in previous_sums_dict:
            sums += previous_sums_dict[current - k]
           
        if current in previous_sums_dict:
            previous_sums_dict[current] += 1
        else:
            previous_sums_dict[current] = 1
      
    return sums

nums = [1,2,3]
k = 3
subarray_sum(nums, k)