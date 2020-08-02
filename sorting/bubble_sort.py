# problem: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
# Difficulty: Easy

def countSwaps(a):
    numSwaps = 0
    # Bubble Sort
    for i in range(len(a) - 1): # better than 'len(a)', iterates less
        for j in range(len(a) - i - 1): # last i elements are already sorted
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1 # count the number of swaps
    # Print the algorithm results
    print("Array is sorted in " + str(numSwaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

n = int(input())
a = list(map(int, input().rstrip().split()))
countSwaps(a)