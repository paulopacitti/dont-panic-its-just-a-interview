# description: https://www.hackerrank.com/challenges/find-the-running-median
#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    medians = []
    medians.append(a[0])
    current = [a[0]]
    for i in range(1, len(a)):
        current.append(a[i])
        insertion_sort(current)
        if len(current) % 2 != 0:
            medians.append(current[int(math.ceil((len(current)/2)-1))])
        else:
            value = (current[int((len(current)/2)-1)] + current[int(len(current)/2)])/2
            medians.append(value)
    return medians
            
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
            
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# Time complexity: O(n²), where n is the size of the array
# Space complexity: O(n)