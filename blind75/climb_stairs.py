# https://leetcode.com/problems/climbing-stairs/description/

# we just need to know the next step
def climbStairs(n: int) -> int:
    table = [1, 2]

    if n >= 3:
        for i in range(2, n):
            step = table[i-2] + table[i-1]
            table.append(step)

    return table[n-1]