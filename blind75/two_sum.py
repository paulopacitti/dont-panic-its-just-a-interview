def twoSum(nums, target):
    # hashtable with elments as keys and indices as elements
    nums_table = {}
    for i in range(len(nums)):
        second_term = target - nums[i]
        if second_term in nums_table:
            return [nums_table[second_term], i]
        else:
            nums_table[nums[i]] = i
    return list([])