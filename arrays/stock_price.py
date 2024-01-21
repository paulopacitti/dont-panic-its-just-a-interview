# description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def maxProfit(prices):
    start = 0
    end = 1
    max_profit = 0

    while end < len(prices):
        if prices[start] < prices[end]:
            max_profit = max(max_profit, prices[end] - prices[start])
        else:
            start = end
        end += 1
    return max_profit
