# problem link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# Difficulty: Medium

def isValid(s):
    s_characters = list(s)
    hash_map = {}
    
    # creates a hash map of occurences by letter
    for e in (s_characters):
        if e in hash_map:
            hash_map[e] += 1
        else:
            hash_map[e] = 1

    # creates a hash map based on the previous one,
    # the occurences are the keys and an array of letters corresponding that occurence is the value
    reverse_hash_map = {}
    for e in hash_map.items():
        if e[1] in reverse_hash_map:
            reverse_hash_map[e[1]].append(e[0])
        else:
            reverse_hash_map[e[1]] = [e[0]]
    
    # transform the hash_map in a list of tuples and then reverse sorts by the length of the array in the value
    reverse_hash_map_list = sorted(list(reverse_hash_map.items()), key=lambda tup: len(tup[1]), reverse=True)
    if len(reverse_hash_map_list) == 1: # if it's only one type of occureence
        return 'YES'
    if len(reverse_hash_map_list) > 2 or len(reverse_hash_map_list[1][1]) > 1: # if there are more than 2 types of occurrences 
        return 'NO'                                                            # or the occurrence that happens less has more than one letter 
    if int(reverse_hash_map_list[1][0]) == 1 and len(reverse_hash_map_list[1][1]) == 1: # if the occurrence that happens less has only one letter
        return 'YES'                                                                    # and occurs only one time
    if int(reverse_hash_map_list[1][0]) - int(reverse_hash_map_list[0][0]) != 1: # if the difference between the occurrence that happens more and 
        return 'NO'                                                              # the occurrence that happens less is not 1
    return 'YES'

s = input()
print(isValid(s))
