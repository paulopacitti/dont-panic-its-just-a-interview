def quick_sort(array):
    quick_sort_util(array, 0, len(array)-1)
    return array

def quick_sort_util(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort_util(array, left, pivot-1)
        quick_sort_util(array, pivot+1, right)

def partition(array, left, right):
    pivot = right
    right -= 1
    while left < right:
        while array[left] < array[pivot]:
            left += 1
        while array[right] > array[pivot]:
            right -= 1
        
        if left < right:
            array[left], array[right] = array[right], array[left]
    array[left], array[pivot] = array[pivot], array[left]
    return left

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))