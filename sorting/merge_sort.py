def merge_sort(array):
    if len(array) == 1:
        return array
    
    first_half = merge_sort(array[:int(len(array)/2)])
    second_half = merge_sort(array[int(len(array)/2):])

    return merge(first_half, second_half)

def merge(first, second):
    i, j = 0, 0
    new_list = []

    while i < len(first) and j < len(second):
        if first[i] > second[j]:
            new_list.append(second[j])
            j += 1
        elif first[i] < second[j]:
            new_list.append(first[i])
            i += 1
        else:
            new_list.append(first[i])
            new_list.append(second[j])
            i += 1
            j += 1

    if i < len(first):
        new_list += first[i:]
    elif j < len(second):
        new_list += second[j:]
    return new_list

print(merge_sort([0,8,6,2,4,9,5,3,6,7]))
