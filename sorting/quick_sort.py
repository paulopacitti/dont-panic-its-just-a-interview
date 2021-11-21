import math

def quick_sort(array):
    quick_sort_util(array, 0, len(array)-1)
    return array

def quick_sort_util(array, left, right):
    if left >= right:
        return

    index = partition(array, left, right)
    quick_sort_util(array, left, index-1)
    quick_sort_util(array, index, right)

    return

def partition(array, left, right):
    pivot = array[math.floor((left + right)/2)]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))