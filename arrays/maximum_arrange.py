# description: https://www.geeksforgeeks.org/maximum-number-formed-from-array-with-k-number-of-adjacent-swaps-allowed/

def arrange(a, k):
    start = 0
    while k > 0:
        max_value = 0
        max_index = 0
        for i in range(start, start+k+1):
            if a[i] > max_value:
                max_value = a[i]
                max_index = i
        for i in range(max_index, start, -1):
            temp = a[i]
            a[i] = a[i-1]
            a[i-1] = temp
            k -= 1
        start += 1
    return a

array = [2, 5, 8, 7, 9]
k_ = 2
print(arrange(array, k_))

# Time complexity: O(n²), where n is the size of the array, since in the worst case k could be n
# Space complexity: O(1), no extra space is required
