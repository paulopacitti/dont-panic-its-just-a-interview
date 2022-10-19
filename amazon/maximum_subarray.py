# description: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# cubic approach
def maximum_subarray_3(nums):
    max_sum = -10001

    for i in range(len(nums)):
        for j in range(len(nums) - i):
            max_sum = max(max_sum, sum(nums[j : j + i + 1]))

    return max_sum


# quadratic approach
def maximum_subarray_2(nums):
    max_sum = -10001

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


# linear approach, kadane's algorithm
def maximum_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        max_sum = max(current_sum, max_sum)
    return max_sum


nums = [-2, -1, -1, -1, -1]
print(maximum_subarray(nums))
