# https://leetcode.com/problems/majority-element

def majorityElement(nums):
    frequency = {}

    for i in nums:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    
    for k, v in frequency.items():
        if v > (len(nums) // 2):
            return k
        
def majorityElementConstantSpace(nums):
    # Boyer-Moore Voting Algorithm 
    candidate = None
    count = 0

    for i in nums:
        if count == 0:
            candidate = i
        if candidate == i:
            count += 1
        else:
            count += -1
    return candidate