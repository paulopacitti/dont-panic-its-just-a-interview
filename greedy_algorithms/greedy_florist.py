# problem link: https://www.hackerrank.com/challenges/angry-children/problem
# Difficulty: Medium


# the idea is that the more expensive flowers should be bought first, one friend at a time,
# and the cheaper flowers should be bought at last, one friend at a time too. This makes the increase
# value in the purchases be less powerful in the final cost;

def getMinimumCost(k, c):
    cost = 0
    c.sort(reverse=True) # sorting prices in decreasing order
    n = len(c) # number of flowers
    previous_purchase = 0 # increase of the price 
    for i in range(n):
        cost += (previous_purchase + 1)*c[i] 
        if (i + 1) % k == 0: # it means that everyone bought one flower with the current previous_purchase value
            previous_purchase += 1 # increase the value for the next purchases
    return cost

n, k = [int(e) for e in input().split()]
c = list(map(int, input().rstrip().split()))
minimumCost = getMinimumCost(k, c)
print(minimumCost)