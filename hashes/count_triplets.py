# problem link: https://www.hackerrank.com/challenges/count-triplets-1/problem
# Difficulty: Medium

def countTriplets(arr, r):
    hash_map = {}
    count = 0
    # creating the hash without 'arr.count()' -> it costs too much time 
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]].append(i)
        else:
            hash_map[arr[i]] = [i]

    for e in arr:
        second = (e * r)
        third  = (e * r)*r
        if second in hash_map and third in hash_map:
            count += hash_map[second] * hash_map[third]
    return count

n, r = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
print(countTriplets(arr, r))

# ================ INCOMPLETE ====================================