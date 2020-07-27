# Complete the minimumSwaps function below.
def minimumSwaps(arr):    
    # all arr are in the [1, 2, 3...] form
    swaps = 0
    for i in range(0, n - 1):
        while arr[i] != i + 1: # element is not in order, swap
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps += 1 # increase the number of swaps

    return swaps

n = input()        
arr = [int(e) for e in input().split()]
print(minimumSwaps(arr))
