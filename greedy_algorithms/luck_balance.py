# problem link: https://www.hackerrank.com/challenges/luck-balance/problem
# Difficulty: Easy
def luckBalance(k, contests):
    hash_map = {}
    balance = 0

    # creates a hash map where the important value is the key and the array of luck values are the key
    for luck, important in contests:
        if important in hash_map:
            hash_map[important].append(luck)
        else:
            hash_map[important] = [luck]
    
    if 0 in hash_map: # lose all non important contests to increase balance
        balance += sum(hash_map[0])
    if 1 in hash_map:
        hash_map[1].sort(reverse=True) # sort in descending order
        for i in range(len(hash_map[1])):
            if i < k:
                balance += hash_map[1][i] # lose all k contests with higher luck value
            else:
                balance -= hash_map[1][i] # win remaing contests with lower luck value

    return balance
    
n, k = [int(e) for e in input().split()]
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))

result = luckBalance(k, contests)
print(result)