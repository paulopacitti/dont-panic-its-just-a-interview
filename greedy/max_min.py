# problem link: https://www.hackerrank.com/challenges/angry-children
# Difficulty: Medium

def max_min(k, arr):
    arr.sort() # sorting the array, so we can find a miimum distance easily
    unfairness = arr[k-1] - arr[0] # initial unfairness value, the difference between 2 numbers with k distance, so we have k-2 elements between the min and max;
    for i in range(1, (len(arr) - k) + 1): # iterate thru the array to find the minimum unfairness value
        if unfairness > arr[(i+k) - 1] - arr[i]: # if we find a new minimum value of unfairness
            unfairness = arr[(i+k) - 1] - arr[i]
    return unfairness

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)
result = max_min(k, arr)
print(result)