# description: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack_recursive(items, capacity):
    return knapsack_recursive_util(items, len(items), capacity)

def knapsack_recursive_util(items, n, capacity):
    if n == 0 or capacity == 0:
        return 0
    elif items[n-1][1] > capacity:
        return knapsack_recursive_util(items, n-1, capacity)
    else:
        including_item = items[n-1][0] + knapsack_recursive_util(items, n-1, capacity - items[n-1][1])
        excluding_item = knapsack_recursive_util(items, n-1, capacity)
        return max(including_item, excluding_item)

def knapsack_dp_top_down(items, capacity):
    return knapsack_dp_top_down_util(items, len(items), capacity, [[-1 for j in range(capacity+1)] for i in range(len(items)+1)])

def knapsack_dp_top_down_util(items, n, capacity, table):
    if n == 0 or capacity == 0:
        return 0
    if table[n][capacity] != -1:
        return table[n][capacity]
    if items[n-1][1] > capacity:
        return knapsack_dp_top_down_util(items, n-1, capacity, table)
    else:
        including_item = items[n-1][0] + knapsack_dp_top_down_util(items, n-1, capacity - items[n-1][1], table)
        excluding_item = knapsack_dp_top_down_util(items, n-1, capacity, table)
        table[n][capacity] = max(including_item, excluding_item)
        return table[n][capacity]

def knapsack_dp_bottom_up(items, capacity):
    table = [[0 for x in range(capacity + 1)] for x in range(len(items) + 1)]
 
    # Build table table[][] in bottom up manner
    for i in range(len(items) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif items[i-1][1] <= w:
                table[i][w] = max(items[i-1][0] + table[i-1][w-items[i-1][1]], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]
 
    return table[len(items)][W]

items = [[1,1], [6,2], [10,3], [16,5]]
W = 7
print(knapsack_dp_bottom_up(items, W))