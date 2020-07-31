# problem link: https://www.hackerrank.com/challenges/count-triplets-1/problem

def countTriplets(arr, r):
    hash_map = {}
    count = 0

    # creating the hash without 'arr.count()' -> it costs too much time 
    for e in arr:
        if e in hash_map:
            hash_map[e] += 1
        else:
            hash_map[e] = 1
    
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