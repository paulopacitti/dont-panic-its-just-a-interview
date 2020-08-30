# Problem link: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/
# Difficulty: Medium

# we must help Sunny and Johnny choose two distinct flavors such that they spend 
# their entire pool of money during each visit.
def whatFlavors(prices, money):
    prices_hash = {} # { <price>: <1-based-index> }
    prices_enum = enumerate(prices, 1) # returns a array of tuples in the form (index, element)
    for index, price in prices_enum:
        if money - price in prices_hash: # if (money - price) in hash, then we found the result
            result = sorted([index, prices_hash[money-price]]) # sorting the indexes
            print(str(result[0]) + " " + str(result[1])) # printing
            return
        else:
            prices_hash[price] = index # add the price to the hash

t = int(input())
for _ in range(t):
    money = int(input())
    n = int(input())
    prices = list(map(int, input().rstrip().split()))
    whatFlavors(prices, money)