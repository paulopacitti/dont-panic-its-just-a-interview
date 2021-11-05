# description: https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

def find_duplicates(array):
    result = []
    for i in range(0, len(array)):
        index = array[i] % len(array) # if array[i] value already exists in the array, it will be noticeble
        array[index] = array[index] + len(array)
    for i in range(0, len(array)):
        if array[i] >= 2*len(array):
            result.append(array[i] - 2*len(array))
    return result

a = [0, 4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(a))

# Time complexity: O(n), where n is the size of the array
# Space complexity: O(1), no extra space is needed