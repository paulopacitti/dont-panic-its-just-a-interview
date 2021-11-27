# description: https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def max_sum_not_adjacent_top_down(array):
    cache = [None for i in range(len(array))]
    return max_sum_not_adjacent_top_down_util(array, cache, 0, len(array))

# top-down, recursive approach
def max_sum_not_adjacent_top_down_util(array, table, i, size):
    if i >= size:
        return 0
    if table[i] != None:
        return table[i]
    
    including_previous = max_sum_not_adjacent_top_down_util(array, table, i+1, size)
    excluding_previous = array[i] + max_sum_not_adjacent_top_down_util(array, table, i+2, size)
    table[i] = max(including_previous, excluding_previous)
    return table[i]

# bottom-up, iterative
def max_sum_not_adjacent_bottom_up(array):
    cache = [0 for i in range(len(array))]
    cache[0] = array[0]
    cache[1] = max(cache[0], array[1])
    for i in range(2, len(array)):
        cache[i] = max(cache[i-1], array[i] + cache[i-2])
    return cache[-1]

# Time Complexity: O(n), where n is the number of elements in the array
# Space Complexity: O(n) for the lookup table

def max_sum_not_adjacent(array):
    including_current = array[0]
    excluding_current = 0
    for i in range(1, len(array)):
        including_previous = including_current
        including_current = excluding_current + array[i]
        excluding_current = max(excluding_current, including_previous)
    return max(including_current, excluding_current)

# Time Complexity: O(n), where n is the number of elements in the array
# Space Complexity: O(1) for the lookup table

arr = [5,  5, 10, 40, 50, 35]
print(max_sum_not_adjacent(arr))