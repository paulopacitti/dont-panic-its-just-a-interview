# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n):
    if n == 1:
        return 1

    left = 1
    right = n
    current = (left + right) // 2

    while left <= right:
        previous_version = isBadVersion(current-1)
        current_version = isBadVersion(current)
        print(left, right, current)
        if not previous_version and current_version:
            return current
        elif not previous_version and not current_version:
            left = current + 1
            current = (right + left) // 2
        else:
            right = current - 1
            current = (right + left) // 2
