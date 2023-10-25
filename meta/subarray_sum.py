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
    subarrays = 0
    current_sum = 0
    previous_sum = {0: 1}

    for num in nums:
        current_sum += num
        if current_sum - k in previous_sum:
            subarrays += previous_sum[current_sum - k]
        if current_sum in previous_sum:
            previous_sum[current_sum] += 1
        else:
            previous_sum[current_sum] = 1

    return subarrays


nums = [1, 2, 3]
k = 3
subarray_sum(nums, k)
