# description: https://leetcode.com/problems/product-of-array-except-self/


def product_except_self(nums):
    product_left = [nums[0]]
    product_right = [nums[-1]]
    output = []

    for i in range(1, len(nums) - 1):
        product_left.append(nums[i] * product_left[i - 1])
        product_right.append(nums[-i - 1] * product_right[i - 1])

    for i in range(len(nums)):
        if i == 0:
            output.append(product_right[-i - 1])
        elif i == len(nums) - 1:
            output.append(product_left[i - 1])
        else:
            output.append(product_left[i - 1] * product_right[-i - 1])
    return output


print(product_except_self([-1, 1, 0, -3, 3]))

# Time complexity: O(n)
# Space complexity: O(n)
