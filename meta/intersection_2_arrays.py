# description: https://leetcode.com/problems/intersection-of-two-arrays/submissions/
def intersection(nums1, nums2):
    frequency = {}
    result = []
    nums1 = set(nums1)
    nums2 = set(nums2)
    for number in nums1:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    for number in nums2:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    for key in frequency:
        if frequency[key] > 1:
            result.append(key)

    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))

# Time complexity: O(n + m)
# Space complexity: O(n + m)