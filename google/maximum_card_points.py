# description: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Solution: sliding window approach, subtracting edge cards
def maxScore(cardPoints, k):
    left = 0
    right = len(cardPoints) - k
    total = sum(cardPoints[right:])
    max_score = total

    while right < len(cardPoints):
        total += cardPoints[left] - cardPoints[right]
        max_score = max(max_score, total)
        left += 1
        right += 1
    return max_score


a = [96, 90, 41, 82, 39, 74, 64, 50, 30]
k = 8
print(maxScore(a, k))

# Time complexity: O(k)
# Space complexity: O(1)
