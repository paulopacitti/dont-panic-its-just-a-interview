# description: https://leetcode.com/problems/min-cost-climbing-stairs/description/

def minCostClimbingStairs(cost):
    cost.append(0)

    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])

    return cost[-1]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
minCostClimbingStairs(cost)
