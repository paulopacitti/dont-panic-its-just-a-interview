# description: https://leetcode.com/problems/counting-bits/

def countBits(n):
    table = [0]
    current_power = 1

    for i in range(1, n + 1):
        if i == current_power*2:
            table.append(1)
            current_power = i
        else:
            table.append(1 + table[i-current_power])

    return table

# Time complexity: O(n)
# Space complexity: O(n)