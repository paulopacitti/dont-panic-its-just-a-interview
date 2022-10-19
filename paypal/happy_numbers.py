# description: https://leetcode.com/problems/happy-number


def square_sum(number):
    total = 0
    current_number = number
    while current_number > 0:
        digit = current_number % 10
        total += digit**2
        current_number = current_number // 10
    return total


def isHappy(n):
    seen = set()
    seen.add(n)
    current_number = n
    while True:
        current_number = square_sum(current_number)
        if current_number == 1:
            return True
        if current_number in seen:
            return False
        seen.add(current_number)


# Time complexity: O(log n)
# Space complexity: O(log n)
