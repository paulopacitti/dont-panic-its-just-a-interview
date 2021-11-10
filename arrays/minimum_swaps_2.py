# description: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
def minimum_swaps(array):
    swaps = 0
    sorted_array = array.copy() # copy of the array, but sorted
    sorted_array.sort()

    dict = {} # Dictionary which stores the indexes of the input array with the value being the key
    for i in range(0,len(array)):
        dict[array[i]] = i
         
    for i in range(0,len(array)):
        if (array[i] != sorted_array[i]): # if array[i] is not in the right place
            old_value = array[i]
            # dict[sorted_array[i]] is the index of the right index for that value
            array[i], array[dict[sorted_array[i]]] = array[dict[sorted_array[i]]], array[i]
 
            # Update the indexes in the hashmap accordingly
            dict[old_value] = dict[sorted_array[i]]
            dict[sorted_array[i]] = i
            
            swaps += 1
             
    return swaps

a = [101,758,315,730,472,619,460,47]
print(minimum_swaps(a))

# Time complexity: O(nlog n) for sorting the array
# Space complexity: O(n) to build the hash and the sorted array