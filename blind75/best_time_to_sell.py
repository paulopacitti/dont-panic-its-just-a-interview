def maxProfit(prices):
    purchased = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if purchased > prices[i]:
            purchased = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - purchased)

    return max_profit

def maxProfitTwoPointers(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[left] > prices[right]:
            left = right
            right += 1
        else:
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1

    return max_profit