from heapq import heapify, heappop

def heap_sort(array):
    sorted_array = []
    heapify(array)
    for i in range(len(array)):
        sorted_array.append(heappop(array))
    return array

arr = [10, 7, 8, 9, 1, 5]
print(heap_sort(arr))